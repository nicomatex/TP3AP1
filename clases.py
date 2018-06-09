import random

RANGO_ARMA_PESO = (2,10)
RANGO_ARMA_ARMADURA = (-5,20)
RANGO_ARMA_ESCUDO = (-4,10)
RANGO_ARMA_VELOCIDAD = (-4,10)
RANGO_ARMA_ENERGIA = (-4,10)
RANGO_ARMA_DANO = (5,20)
RANGO_ARMA_HITS = (1,3)
RANGO_ARMA_PRECISION = (1,50)
RANGO_ARMA_TIEMPO_RECARGA = (1,2)

CLASES_ARMA = ("GN Blade","Chaos Sword", "Frostmourne","Ashbringer","Elucidator","Daybreak")
TIPOS_MUNICION = ("FISICA","LASER","HADRON")
TIPOS_ARMA = ("MELEE","RANGO")

class Gunpla:
	'''
	Representa un Gunpla. Un Gunpla esta compuesto de un Esqueleto, un conjunto de partes y un conjunto de armas.
	'''

	def __init__(self,esqueleto):
		'''
		Recibe un esqueleto e inicializa el gunpla con ese esqueleto.
		'''
		self.esqueleto = esqueleto 
		self.partes = {}
		self.armas = []

class Arma:
	'''
	Representa un arma.
	'''
	def __init__(self):
		'''
		Inicializa un arma aleatoria.
		'''
		self.peso = random.randint(RANGO_ARMA_PESO[0],RANGO_ARMA_PESO[1])
		self.armadura = random.randint(RANGO_ARMA_ARMADURA[0],RANGO_ARMA_ARMADURA[1])
		self.escudo = random.randint(RANGO_ARMA_ESCUDO[0],RANGO_ARMA_ESCUDO[1])
		self.velocidad = random.randint(RANGO_ARMA_VELOCIDAD[0],RANGO_ARMA_VELOCIDAD[1])
		self.energia = random.randint(RANGO_ARMA_ENERGIA[0],RANGO_ARMA_ENERGIA[1])
		self.tipo_municion = random.choice(TIPOS_MUNICION)
		self.tipo = random.choice(TIPOS_ARMA)
		self.clase = random.choice(CLASES_ARMA)
		self.dano = random.randint(RANGO_ARMA_DANO[0],RANGO_ARMA_DANO[1])
		self.hits = random.randint(RANGO_ARMA_HITS[0],RANGO_ARMA_HITS[1])
		self.precision = random.randint(RANGO_ARMA_PRECISION[0],RANGO_ARMA_PRECISION[1])
		self.tiempo_recarga = random.randint(RANGO_ARMA_TIEMPO_RECARGA[0],RANGO_ARMA_TIEMPO_RECARGA[1])
		self.esta_lista = True
		self.tipo_parte = "Arma"

		def get_peso(self):
			'''
			Devuelve el peso del arma.
			'''
			return self.peso

		def get_armadura(self):
			'''
			Devuelve la armadura del arma.
			'''
			return self.armadura

		def get_escudo(self):
			'''
			Devuelve el escudo del arma.
			'''
			return self.escudo

		def get_velocidad(self):
			'''
			Devuelve la velocidad del arma.
			'''
			return self.velocidad

		def get_energia(self):
			'''
			Devuelve la energia del arma.
			'''
			return self.energia

		def get_tipo_municion(self):
			'''
			Devuelve el tipo de municion del arma.
			'''
			return self.tipo_municion

		def get_tipo(self):
			'''
			Devuelve el tipo del arma.
			'''
			return self.tipo

		def get_clase(self):
			'''
			Devuelve la clase del arma.
			'''
			return self.clase

		def get_dano(self):
			'''
			Devuelve el dano del arma.			
			'''
			return self.dano

		def get_hits(self):
			'''
			Devuelve la cantidad de veces que puede atacar un arma en un turno.
			'''
			return self.hits

		def get_precision(self):
			'''
			Devuelve la precision del arma.
			'''
			return self.precision

		def get_tiempo_recarga(self):
			'''
			Devuelve la cantidad de turnos que tarda un arma en estar lista.
			'''
			return self.tiempo_recarga

		def esta_lista(self):
			'''
			Devuelve True si el arma es capaz de ser utilizada en este turno, caso contrario devuelve False.
			'''
			return self.esta_lista

		def get_tipo_parte(self):
			'''
			Devuelve el tipo de parte.
			'''
			return self.tipo_parte