import random

def generar_equipos(lista_pilotos):
	"""Recibe todos los pilotos y los divide en equipos de PILOTOS_POR_EQUIPO,devuelve una lista con todos los equipos"""

	equipos = {"equipo {}".format(i):[] for i in range(lista_pilotos)}
	
	random.shuffle(lista_pilotos)
	
	indice=0

	for piloto in lista_pilotos:
		equipos["equipo {}".format(indice)].append(piloto)
		if len(equipos["equipo {}".format(indice)])==PILOTOS_POR_EQUIPO:
			indice+=1

	return equipos