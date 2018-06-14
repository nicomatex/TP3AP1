from clases import *
from Pila import *

CANTIDAD_ESQUELETOS = 3
CANTIDAD_PARTES = 20
CANTIDAD_ARMAS = 20

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
