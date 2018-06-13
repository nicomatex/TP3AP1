class Nodo:
	'''
	Clase interna de Cola
	'''

	def __init__(self,dato):
		self.dato = dato
		self.proxi = None

class Cola:
	'''
	Tipo de dato abstracto cola.
	'''

	def __init__(self):
		self.primero = None
		self.ultimo = None

	def encolar(self,elemento):
		'''
		Recibe un elemento y lo encola.
		'''

		nuevo = Nodo(elemento)

		if not self.ultimo:
			self.primero = nuevo
			self.ultimo = nuevo
			return

		self.ultimo.proxi = nuevo 
		self.ultimo = nuevo

	def desencolar(self):
		'''
		Desencola el primer elemento
		'''

		if not self.primero:
			raise ValueError("La cola esta vacia")

		valor = self.primero.dato

		self.primero = self.primero.proxi

		if not self.primero:
			self.ultimo = None

		return valor

	def esta_vacia(self):
		'''
		Devuelve True si la cola esta vacia. Caso contrario, devuelve False.
		'''
		return self.primero == None
