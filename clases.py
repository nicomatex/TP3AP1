import random

RANGO_ARMA_PESO = (2,10)
RANGO_ARMA_ARMADURA = (-5,20)
RANGO_ARMA_ESCUDO = (-4,10)
RANGO_ARMA_VELOCIDAD = (-4,10)
RANGO_ARMA_ENERGIA = (-4,10)
RANGO_ARMA_DAÑO = (5,20)
RANGO_ARMA_HITS = (1,3)
RANGO_ARMA_PRECISION = (30,90)
RANGO_ARMA_TIEMPO_RECARGA = (2,4)

RANGO_ESQUELETO_VELOCIDAD = (-4,10)
RANGO_ESQUELETO_ENERGIA = (0,50)
RANGO_ESQUELETO_MOVILIDAD = (100,200)
ESQUELETO_SLOTS = 20

RANGO_PARTE_PESO = (1,10)
RANGO_PARTE_ARMADURA = (-4,10)
RANGO_PARTE_ESCUDO = (-2,10)
RANGO_PARTE_VELOCIDAD = (-2,10)
RANGO_PARTE_ENERGIA = (2,20)
RANGO_PARTE_SLOTS = (2,4)

GUNPLA_SLOTS = 4

TIPOS_PARTE = ("Backpack","Chestplate","Legplates","Boots","Helmet","Belt","Wrists")

CLASES_ARMA = ("GN Blade","Chaos Sword", "Frostmourne","Ashbringer","Elucidator","Daybreak")
TIPOS_MUNICION = ("FISICA","LASER","HADRON")
TIPOS_ARMA = ("MELEE","RANGO")

PROBABILIDAD_ESQUIVAR = 0

class Gunpla:
	'''
	Representa un Gunpla. Un Gunpla esta compuesto de un Esqueleto, un conjunto de partes y un conjunto de armas.
	'''

	def __init__(self,esqueleto):
		'''
		Recibe un esqueleto e inicializa el gunpla con ese esqueleto.
		'''
		self.esqueleto = esqueleto 
		self.partes = {}
		self.slots = GUNPLA_SLOTS
		self.peso = 0
		self.escudo = 0
		self.armadura = 0
		self.velocidad = esqueleto.get_velocidad()
		self.energia = esqueleto.get_energia()
		self.energia_restante = self.energia

	def get_peso(self):
		'''
		Devuelve el peso total del Gunpla. Un Gunpla pesa lo que pesa la sumatoria de sus partes y armas.
		'''
		return self.peso

	def get_armadura(self):
		'''
		Devuelve la armadura total del Gunpla. Un Gunpla tiene tanta armadura como la sumatoria de la armadura de sus partes y armas.
		'''

		return self.armadura

	def get_escudo(self):
		'''
		Devuelve el escudo total del Gunpla. Un Gunpla tiene tanto escudo como la sumatoria del escudo de sus partes y armas.
		'''

		return self.escudo


	def get_velocidad(self):
		'''
		Devuelve la velocidad total del Gunpla. Un Gunpla tiene tanta velocidad como 
		la sumatoria de las velocidades de sus partes y esqueleto.
		'''

		return self.velocidad

	def get_energia(self):
		'''
		Devuelve la energía total del Gunpla. Un Gunpla tiene tanta energía como
		la sumatoria de la energía de sus partes, armas y esqueleto.
		'''

		return self.energia


	def get_energia_restante(self):
		'''
		Devuelve la energía que le resta al Gunpla.
		'''

		return self.energia_restante

	def get_movilidad(self):
		'''
		Devuelve la movilidad de un Gunpla. 
		'''

		base = self.esqueleto.get_movilidad()
		peso = self.get_peso()
		velocidad = self.get_velocidad()

		movilidad = (base - (peso/2) + (velocidad *3)) / base
		
		if movilidad>1:
			return 1
		elif movilidad<0:
			return 0

		return movilidad

	def get_armamento(self):
		'''
		Devuelve una lista con todas las armas adosadas al Gunpla (Se incluyen las armas disponibles en las partes).
		'''
		armas = []

		for arma in self.esqueleto.get_armamento():
			armas.append(arma)

		for parte in self.partes.values():
			for arma in parte.get_armamento():
				armas.append(arma)

		return armas

	def attach_parte(self,parte):
		'''
		Recibe una parte y se la adosa al gunpla.
		'''

		self.partes[parte.get_tipo_parte()]=parte

		self.armadura+= parte.get_armadura()
		self.energia+= parte.get_energia()
		self.energia_restante+= parte.get_energia()
		self.peso+= parte.get_peso()
		self.escudo+= parte.get_escudo()
		self.velocidad+= parte.get_velocidad()

		for arma in parte.get_armamento():
			self.armadura+= arma.get_armadura()
			self.energia+= arma.get_energia()
			self.energia_restante+= arma.get_energia()
			self.peso+= arma.get_peso()
			self.escudo+= arma.get_escudo()
			self.velocidad+= arma.get_velocidad()

	def attach_arma(self,arma):
		'''
		Recibe un arma y si hay slots disponibles, se la adosa al gunpla. Caso contrario, levanta una excepcion.
		'''

		self.esqueleto.attach_arma(arma)

		self.armadura+= arma.get_armadura()
		self.energia+= arma.get_energia()
		self.energia_restante+= arma.get_energia()
		self.peso+= arma.get_peso()
		self.escudo+= arma.get_escudo()
		self.velocidad+= arma.get_velocidad()

	def get_cantidad_slots(self):
		'''
		Devuelve la cantidad de slots disponibles para armas en el gunpla.
		'''
		return self.esqueleto.get_cantidad_slots()

	def recibir_daño(self,daño,tipo_municion):
		'''
		Recibe una cantidad de daño y un tipo de daño y le resta al gunpla la energia 
		correspondiente segun la reduccion que corresponda.
		'''
		if random.random() < (self.get_movilidad()*PROBABILIDAD_ESQUIVAR)/100:
			return 0

		if tipo_municion=="HADRON":
			self.energia_restante-=daño
			return daño
		
		if tipo_municion=="FISICA":

			daño_recibido = daño-self.armadura #Calculo de reduccion de daño.

			self.energia_restante-=daño_recibido
			if daño_recibido<0:
				return 0
			return daño_recibido

		if tipo_municion=="LASER":

			daño_recibido = daño- daño*self.escudo #Calculo de reduccion de daño.
			self.energia_restante-=daño_recibido
			if daño_recibido<0:
				return 0
			return daño_recibido

class Arma:
	'''
	Representa un arma.
	'''
	def __init__(self):
		'''
		Inicializa un arma aleatoria.
		'''
		self.peso = random.randint(RANGO_ARMA_PESO[0],RANGO_ARMA_PESO[1])
		self.armadura = random.randint(RANGO_ARMA_ARMADURA[0],RANGO_ARMA_ARMADURA[1])
		self.escudo = random.randint(RANGO_ARMA_ESCUDO[0],RANGO_ARMA_ESCUDO[1])
		self.velocidad = random.randint(RANGO_ARMA_VELOCIDAD[0],RANGO_ARMA_VELOCIDAD[1])
		self.energia = random.randint(RANGO_ARMA_ENERGIA[0],RANGO_ARMA_ENERGIA[1])
		self.tipo_municion = random.choice(TIPOS_MUNICION)
		self.tipo = random.choice(TIPOS_ARMA)
		self.clase = random.choice(CLASES_ARMA)
		self.daño = random.randint(RANGO_ARMA_DAÑO[0],RANGO_ARMA_DAÑO[1])
		self.hits = random.randint(RANGO_ARMA_HITS[0],RANGO_ARMA_HITS[1])
		self.precision = random.randint(RANGO_ARMA_PRECISION[0],RANGO_ARMA_PRECISION[1])
		self.tiempo_recarga = random.randint(RANGO_ARMA_TIEMPO_RECARGA[0],RANGO_ARMA_TIEMPO_RECARGA[1])
		self.tiempo_recarga_restante = 0
		self.estado = True
		self.tipo_parte = "Arma"

	def get_peso(self):
		'''
		Devuelve el peso del arma.
		'''
		return self.peso

	def get_armadura(self):
		'''
		Devuelve la armadura del arma.
		'''
		return self.armadura

	def get_escudo(self):
		'''
		Devuelve el escudo del arma.
		'''
		return self.escudo

	def get_velocidad(self):
		'''
		Devuelve la velocidad del arma.
		'''
		return self.velocidad

	def get_energia(self):
		'''
		Devuelve la energia del arma.
		'''
		return self.energia

	def get_tipo_municion(self):
		'''
		Devuelve el tipo de municion del arma.
		'''
		return self.tipo_municion

	def get_tipo(self):
		'''
		Devuelve el tipo del arma.
		'''
		return self.tipo

	def get_clase(self):
		'''
		Devuelve la clase del arma.
		'''
		return self.clase

	def get_daño(self):
		'''
		Devuelve el dano del arma.			
		'''
		return self.daño

	def get_hits(self):
		'''
		Devuelve la cantidad de veces que puede atacar un arma en un turno.
		'''
		return self.hits

	def get_precision(self):
		'''
		Devuelve la precision del arma.
		'''
		return self.precision

	def get_tiempo_recarga(self):
		'''
		Devuelve la cantidad de turnos que tarda un arma en estar lista.
		'''
		return self.tiempo_recarga

	def usar(self):
		'''
		Establece tiempo_recarga_restante en tiempo_recarga turnos.
		'''
		self.tiempo_recarga_restante = self.tiempo_recarga

	def recargar(self):
		'''
		Reduce en una unidad al tiempo de recarga restante.
		'''
		self.tiempo_recarga_restante-=1

		if self.tiempo_recarga_restante==0:
			self.tiempo_recarga_restante=0

	def reiniciar(self):
		'''
		Reinicia el tiempo de recarga del arma(lo pone en cero y la deja lista para ser usada).
		'''

		self.tiempo_recarga_restante = 0

	def esta_lista(self):
		'''
		Devuelve True si el arma es capaz de ser utilizada en este turno, caso contrario devuelve False.
		'''
		return self.tiempo_recarga_restante==0

	def get_tipo_parte(self):
		'''
		Devuelve el tipo de parte.
		'''
		return self.tipo_parte

class Esqueleto:
	""" Represneta el esqueleto interno del Gunpla """

	def __init__(self):
		'''
		Inicializa un esqueleto con atributos aleatorios.
		'''
		self.velocidad = random.randint(RANGO_ESQUELETO_VELOCIDAD[0],RANGO_ESQUELETO_VELOCIDAD[1])
		self.energia = random.randint(RANGO_ESQUELETO_ENERGIA[0],RANGO_ESQUELETO_ENERGIA[1])
		self.movilidad = random.randint(RANGO_ESQUELETO_MOVILIDAD[0],RANGO_ESQUELETO_MOVILIDAD[1])
		self.slots = ESQUELETO_SLOTS
		self.armas = []

	def get_velocidad(self):
		"""Devuelve la velocidad del esqueleto"""
		return self.velocidad

	def get_energia(self):
		"""Devuelve la energia del esqueleto"""
		return self.energia

	def get_movilidad(self):
		"""Devuelve la movilidad del esqueleto"""
		return self.movilidad

	def get_cantidad_slots(self):
		"""Devuelve la cantidad de slots para armas que tiene el esqueleto"""
		return self.slots


	def get_armamento(self):
		'''
		Devuelve una lista con las armas del gunpla.
		'''
		armas = []
		for arma in self.armas:
			armas.append(arma)

		return armas
 
	def attach_arma(self,arma):
		'''
		Recibe un arma y, si quedan slots disponibles, se la adosa al esqueleto.
		'''

		if len(self.armas)==self.slots:
			raise ValueError("Ya no hay slots disponibles.")

		self.armas.append(arma)

class Parte:
	"""Representa una parte del Gunpla"""

	def __init__(self):
		'''
		Inicializa una parte con atributos aleatorios.\
		'''
		self.peso_base = random.randint(RANGO_PARTE_PESO[0],RANGO_PARTE_PESO[1])
		self.armadura_base = random.randint(RANGO_PARTE_ARMADURA[0],RANGO_PARTE_ARMADURA[1])
		self.escudo_base = random.randint(RANGO_PARTE_ESCUDO[0],RANGO_PARTE_ESCUDO[1])
		self.velocidad = random.randint(RANGO_PARTE_VELOCIDAD[0],RANGO_PARTE_VELOCIDAD[1])
		self.energia_base = random.randint(RANGO_PARTE_ENERGIA[0],RANGO_PARTE_ENERGIA[1])
		self.tipo_parte = random.choice(TIPOS_PARTE)
		self.slots = random.randint(RANGO_PARTE_SLOTS[0],RANGO_PARTE_SLOTS[1])
		self.armamento = []
		
	def get_peso(self):
		"""
		Devuelve el peso total de la parte. 
		Una parte pesa lo que pesa la sumatoria de sus armas más el peso base de la parte
		"""
		peso_total = self.peso_base

		for arma in self.armamento:
			peso_total += arma.get_peso()

		return peso_total

	def get_armadura(self):
		"""
		Devuelve la armadura total de la parte. Una parte 
		tiene tanta armadura como la sumatoria de la armadura de sus armas
		más la armadura base de la parte
		"""
		armadura_total = self.armadura_base

		for arma in self.armamento:
			armadura_total += arma.get_armadura()

		return armadura_total

	def get_escudo(self):
		"""
		Devuelve el escudo total de la parte. 
		Una parte tiene tanto escudo como la sumatoria del escudo de sus 
		armas más el escudo base de la parte 
		"""

		escudo_total = self.escudo_base

		for arma in self.armamento:
			escudo_total += arma.get_escudo()

		return escudo_total

	def get_velocidad(self):
		"""
		Devuelve la velocidad total de la parte.
		"""

		return self.velocidad

	def get_energia(self):
		"""
		Devuelve la energía total de la parte. 
		La parte tiene tanta energía como la sumatoria de la energía de sus 
		armas más la energía base de la parte
		"""

		energia_total = self.energia_base

		for arma in self.armamento:
			energia_total += arma.get_energia()

		return energia_total

	def get_armamento(self):
		"""Devuelve una lista con todas las armas adosadas a la parte"""
		armamento = []

		for arma in self.armamento:
			armamento.append(arma)

		return armamento

	def get_tipo_parte(self):
		"""Devuelve una cadena que representa el tipo de parte."""
		return self.tipo_parte

	def get_cantidad_slots(self):
		'''
		Devuelve la cantidad de slots disponibles para adosar armas en la parte.
		'''
		return self.slots

	def attach_arma(self,arma):
		'''
		Si hay espacio disponible, le adosa un arma al gunpla. Caso contrario, levanta una excepcion.
		'''

		if len(self.armamento)==self.slots:
			raise ValueError("Esta parte no tiene mas slots disponibles para armas.")

		self.armamento.append(arma)