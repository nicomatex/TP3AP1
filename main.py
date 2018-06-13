from clases import *

CANTIDAD_ESQUELETOS = 3

def generar_esqueletos():
	'''
	Devuelve una lista con CANTIDAD_ESQUELETOS de esqueletos generados de forma aleatoria.
	'''
	esqueletos = []

	for i in range CANTIDAD_ESQUELETOS:
		esqueletos.append(Esqueleto())

	return esqueletos