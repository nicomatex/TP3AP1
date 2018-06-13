from clases import *


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

		for parte in partes:

			if partes[parte].get_energia() > partes[parte_elegida].get_energia():
				parte_elegida = parte

		return parte_elegida

	def elegir_combinacion(self,partes_reservadas):
		'''
		Dada una lista con partes previamente reservadas, devuelve una lista con las partes a utilizar para construir el Gunpla. 
		'''
		partes_elegidas = []

		for parte in partes_reservadas:
			if parte.get_tipo_parte() not in [p.get_tipo_parte() for p in partes_elegidas]:
				partes_elegidas.append(parte)
				
		return partes_elegidas