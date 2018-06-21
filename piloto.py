TIPO_MUNICION_LASER = "LASER"
TIPO_MUNICION_FISICA = "FISICA"
TIPO_MUNICION_HADRON = "HADRON"
FACTOR_ARMADURA_ESCUDO = 200

class Piloto:
	'''
	Inteligencia artificial para controlar un Gunpla.
	'''

	def __init__(self):
		'''
		Inicializa un piloto.
		'''
		self.gunpla = None
		self.tipo_partes_elegidas = []
		self.partes_reservadas = {}

	def set_gunpla(self,gunpla):
		'''
		Asigna un gunpla al piloto.
		'''
		self.gunpla = gunpla

	def get_gunpla(self):
		'''
		Devuelve el gunpla del piloto.
		'''
		return self.gunpla

	def elegir_esqueleto(self,lista_esqueletos):
		'''
		Dada una lista con esqueletos, devuelve el índice del esqueleto a utilizar.
		'''
		lista_ordenada = sorted(lista_esqueletos, key=lambda esqueleto: esqueleto.get_energia(), reverse=True)

		return lista_esqueletos.index(lista_ordenada[0])

	def elegir_parte(self,partes):
		'''
		Dado un diccionario: {tipo_parte:parte}, devuelve el tipo de parte que quiere elegir.
		'''
		parte_elegida = list(partes.keys())[0]

		for tipo_parte in partes:
			if not self.partes_reservadas.get(tipo_parte,False):
				self.partes_reservadas[tipo_parte] = partes[tipo_parte]
				return tipo_parte

		for tipo_parte in partes:
			if partes[tipo_parte].get_energia()>self.partes_reservadas[tipo_parte].get_energia():
				return tipo_parte

		return parte_elegida

	def elegir_combinacion(self,partes_reservadas):
		'''
		Dada una lista con partes previamente reservadas, devuelve una lista con las partes a utilizar para construir el Gunpla. 
		'''
		partes_elegidas = []

		for parte in partes_reservadas:
			if parte in self.partes_reservadas.values():

				partes_elegidas.append(parte)

		return partes_elegidas

	def elegir_oponente(self,oponentes):
		'''
		Devuelve el índice del Gunpla al cual se decide atacar de la lista de oponentes pasada.
		'''
		oponente_elegido = oponentes[0]

		for oponente in oponentes:
			if oponente==self.get_gunpla():
				continue

			if oponente_elegido == self.get_gunpla():
				oponente_elegido=oponente
				continue

			if oponente.get_energia_restante()<oponente_elegido.get_energia_restante():
				oponente_elegido = oponente

		return oponentes.index(oponente_elegido)

	def elegir_arma(self,oponente,combinacion=False,arma_combinacion=None):
		'''
		Recibe un oponente y devuelve el arma con el cual se desea atacar al oponente. Recibe ademas opcionalmente
		un booleano Combinacion en caso de que se trate de una seleccion de arma para combinacion y un arma a partir de la cual
		surge el ataque combinado.
		'''
		armas_disponibles = [arma for arma in self.gunpla.get_armamento() if arma.esta_lista()]
		armas_hadron = [arma for arma in armas_disponibles if arma.get_tipo_municion()==TIPO_MUNICION_HADRON]
		armas_fisicas = [arma for arma in armas_disponibles if arma.get_tipo_municion()==TIPO_MUNICION_FISICA]
		armas_laser = [arma for arma in armas_disponibles if arma.get_tipo_municion()==TIPO_MUNICION_LASER]

		if not armas_disponibles:
			return None
		
		#Caso de elegir un arma para combinar
		if combinacion:
			if arma_combinacion.get_tipo()==TIPO_MUNICION_LASER:

				for arma in armas_laser:

					if arma.get_clase()==arma_combinacion.get_clase():
						return arma
				return None

			else:

				for arma in armas_fisicas:

					if arma.get_clase()==arma_combinacion.get_clase():
						return arma
				return None
				
		#Elige , en lo posible, un arma de hadron
		if any(armas_hadron):
			arma_elegida=armas_hadron[0]

			for arma in armas_hadron:
				if arma.get_daño()>arma_elegida.get_daño():
					arma_elegida = arma

			return arma

		#Decide si el oponente va a recibir mas danio fisico o mas danio laser.

		if (oponente.get_escudo()<oponente.get_armadura()/FACTOR_ARMADURA_ESCUDO or not any(armas_fisicas)) and any(armas_laser):
			arma_elegida=armas_laser[0]

			for arma in armas_laser:
				if arma.get_daño()>arma_elegida.get_daño():
					arma_elegida = arma

			return arma

		arma_elegida=armas_fisicas[0]

		for arma in armas_fisicas:
			if arma.get_daño()>arma_elegida.get_daño():
				arma_elegida = arma

		return arma