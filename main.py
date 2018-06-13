from clases import *
from Pila import *

CANTIDAD_ESQUELETOS = 3
CANTIDAD_PARTES = 50

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