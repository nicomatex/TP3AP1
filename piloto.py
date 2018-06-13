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