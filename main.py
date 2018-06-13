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
	Devuelve una pila con CANTIDAD_PARTES de partes generadas de forma aleatoria, con sus respectivas armas equipadas.
	'''
	partes = Pila()

	for _ in range(CANTIDAD_PARTES):
		parte = Parte()

		#Se adosan las armas correspondientes a la parte segun sus slots disponibles.
		for _ in range(parte.get_cantidad_slots()):
			parte.attach_arma(Arma())

		partes.apilar(parte)

	return partes

def generar_armas():
	'''
	Devuelve una pila con CANTIDAD_ARMAS de armas generadas aleatoriamente.
	'''
	armas = Pila()

	for _ in range(CANTIDAD_ARMAS):
		armas.apilar(Arma())

	return armas

