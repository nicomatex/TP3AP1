from clases import *
from Pila import *
from piloto import *

CANTIDAD_ESQUELETOS = 10
CANTIDAD_PARTES = 20
CANTIDAD_ARMAS = 20
CANTIDAD_PILOTOS = 2

def generar_esqueletos():
	'''
	Devuelve una lista con CANTIDAD_ESQUELETOS de esqueletos generados de forma aleatoria.
	'''
	esqueletos = []

	for i in range(CANTIDAD_ESQUELETOS):
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
	pilotos.shuffle()
	for _,piloto in pilotos:
		indice_esqueleto_elegido = piloto.elegir_esqueleto(esqueletos)

		#Se instancia un nuevo gunpla con el esqueleto elegido.
		piloto.set_gunpla(Gunpla(esqueletos[indice_esqueleto_elegido]))

def elegir_partes(partes,pilotos):
	'''
	Recibe un diccionario partes de la forma <tipo_parte:pila con partes de ese tipo> y una lista de 
	pilotos, y le permite a los 
	pilotos reservar partes de cada una de las pilas.
	'''

	partes_reservadas = {piloto:[] for piloto in pilotos}

	todas_vacias = False

	piloto_eligiendo = 0

	while not todas_vacias:

		todas_vacias = True

		for pila_partes in partes.values():
			if not pila_partes.esta_vacia():
				todas_vacias = False

		elector = pilotos[piloto_eligiendo]
		tipo_parte_elegida = elector[1].elegir_parte(partes)
		partes_reservadas[elector].append(partes[tipo_parte_elegida].desapilar())

		piloto_eligiendo+=1

		if piloto_eligiendo>len(pilotos):
			piloto_eligiendo=0

	return partes_reservadas