from clases import *
from Pila import *
from Cola import *
from piloto import *

CANTIDAD_ESQUELETOS = 10
CANTIDAD_PARTES = 20
CANTIDAD_ARMAS = 20
CANTIDAD_PILOTOS = 5

def generar_esqueletos():
	'''
	Devuelve una lista con CANTIDAD_ESQUELETOS de esqueletos generados de forma aleatoria.
	'''
	esqueletos = []

	for _ in range(CANTIDAD_ESQUELETOS):
		esqueletos.append(Esqueleto())

	return esqueletos

def generar_partes():
	'''
	Devuelve un diccionario cuyas claves son los tipos de partes disponibles y sus valores son pilas de partes de dicho tipo.
	'''
	partes = {}

	for _ in range(CANTIDAD_PARTES):
		parte = Parte()

		#Se adosan las armas correspondientes a la parte segun sus slots disponibles.
		for _ in range(parte.get_cantidad_slots()):
			parte.attach_arma(Arma())


		pila_tipo = partes.get(parte.get_tipo_parte(),Pila())
		pila_tipo.apilar(parte)
		partes[parte.get_tipo_parte()]=pila_tipo

	#Se generan las armas
	partes['Arma']= Pila()

	for _ in range(CANTIDAD_ARMAS):
		partes['Arma'].apilar(Arma())

	return partes

def generar_pilotos():
	'''
	Recibe un entero cantidad_pilotos y devuelve una lista de tuplas de la forma <numero de piloto, piloto> con 
	esa cantidad de pilotos.
	'''
	lista_pilotos = []

	for i in range(0,CANTIDAD_PILOTOS):
		lista_pilotos.append((i,Piloto()))

	return lista_pilotos

def elegir_esqueletos(pilotos,esqueletos):
	'''
	Recibe una lista de pilotos y una lista de esqueletos y le permite a cada piloto elegir 
	el esqueleto que quiere para su gunpla. No devuelve nada.
	'''
	
	#
	random.shuffle(pilotos)

	for _,piloto in pilotos:
		indice_esqueleto_elegido = piloto.elegir_esqueleto(esqueletos)

		#Se instancia un nuevo gunpla con el esqueleto elegido.
		piloto.set_gunpla(Gunpla(esqueletos[indice_esqueleto_elegido]))

def elegir_partes(partes,pilotos):
	'''
	Recibe un diccionario partes de la forma <tipo_parte:pila con partes de ese tipo> y una lista de 
	tuplas de la forma <numero de piloto,piloto>
	pilotos, y devuelve un diccionario de la forma
	{(numero de piloto, piloto):[Lista de partes reservadas por el piloto]}
	'''

	partes_reservadas = {piloto:[] for piloto in pilotos}

	piloto_eligiendo = 0

	todas_vacias = False

	while True:

		todas_vacias = True
		for tipo_parte in partes:
			if not partes[tipo_parte].esta_vacia():
				todas_vacias = False

		#Condicion de corte: Que esten todas las pilas vacias.
		if todas_vacias:
			break

		elector = pilotos[piloto_eligiendo]
		tipo_parte_elegida = elector[1].elegir_parte(partes)
		partes_reservadas[elector].append(partes[tipo_parte_elegida].desapilar())

		if partes[tipo_parte_elegida].esta_vacia():
			partes.pop(tipo_parte_elegida)

		piloto_eligiendo+=1

		if piloto_eligiendo>len(pilotos)-1:
			piloto_eligiendo=0

	return partes_reservadas

def equipar_gunplas(partes_reservadas):
	'''
	Recibe un diccionario de la forma {(numero de piloto,piloto):[lista de partes elegidas]}
	y equipa el gunpla de cada piloto 
	con las partes elegidas de entre las partes reservadas. No devuelve nada.
	'''

	for piloto in partes_reservadas:

		partes_seleccionadas = piloto[1].elegir_combinacion(partes_reservadas[piloto])

		for parte in partes_seleccionadas:
			if parte.get_tipo_parte()=="Arma":
				piloto[1].get_gunpla().attach_arma(parte)
			else:
				piloto[1].get_gunpla().attach_parte(parte)

def ordenar_pilotos(pilotos):
	'''
	Recibe una lista de tuplas de la forma <numero de piloto,piloto> y devuelve 
	una lista de los pilotos ordenados segun la velocidad de sus gunplas.
	'''

	lista_resultado = sorted(pilotos, key = lambda piloto: piloto[1].get_gunpla().get_velocidad(), reverse = True)

	return lista_resultado


def inicializar_turnos(pilotos):
	'''
	Recibe una lista de pilotos ordenados segun la velocidad de sus gunplas y devuelve una cola 
	de "turnos" donde el primer turno corresponde al gunpla mas rapido y el ultimo al mas lento.
	'''
	cola_turnos = Cola()

	for piloto in pilotos:
		cola_turnos.encolar(piloto)

	return cola_turnos

def calcular_dano(arma):
	'''
	Recibe un arma y calcula el danio que esta realizara al oponente.
	'''
	dano_total = 0
	for i in range(arma.get_hits()):

def main():

	pilotos = generar_pilotos()

	print(pilotos)#Debug

	partes = generar_partes()
	esqueletos = generar_esqueletos()
	elegir_esqueletos(pilotos,esqueletos)
	reservadas = elegir_partes(partes,pilotos)
	equipar_gunplas(reservadas)
	ordenados = ordenar_pilotos(pilotos)

	print(ordenados)#Debug

	turnos = inicializar_turnos(ordenados)


	gunplas_activos = [piloto[1].get_gunpla() for piloto in pilotos]

	while len(gunplas_activos)>=2:
		numero_piloto, atacante = turnos.desencolar()
		oponente_elegido = atacante.elegir_oponente(gunplas_activos)
		arma_elegida = atacante.elegir_arma(oponente)
