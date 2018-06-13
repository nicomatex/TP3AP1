class Pila:
	'''
	Es el tipo de dato abstracto pila.
	'''

	def __init__(self):
		'''
		Inicia una lista vacia.
		'''
		self.datos = []

	def apilar(self,dato):
		'''
		Apila el dato en la pila.
		'''
		self.datos.append(dato)

	def desapilar(self):
		'''
		Desapila el ultimo dato.
		'''
		return self.datos.pop()

	def esta_vacia(self):
		'''
		Devuelve True si la pila esta vacia, sino devuelve False.
		'''
		return len(self.datos)==0

	def ver_tope(self):
		'''
		Devuelve el elemento que esta en el tope, pero no lo desapila.
		'''

		return self.datos[-1] 
