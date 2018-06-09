arma
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

class Esqueleto:
	""" Represneta el esqueleto interno del Gunpla """

	def __init__(self):
		self.velocidad = VELOCIDAD
		self.energia = ENERGIA
		self.movilidad = MOVILIDAD
		self.slots = SLOTS

	def get_velocidad(self):
		"""Devuelve la velocidad del esqueleto"""
		return self.velocidad

	def get_energia(self):
		"""Devuelve la energia del esqueleto"""
		return self.energia

	def get_movilidad(self):
		"""Devuelve la movilidad del esqueleto"""
		return self.movilidad

	def get_cantidad_slots(self):
		"""Devuelve la cantidad de slots para armas que tiene el esqueleto"""

class Parte:
	"""Representa una parte del Gunpla"""
	def __init__(self):
		self.peso_base = PESOBASE
		self.armadura_base = ARMADURA
		self.escudo_base = ESCUDO
		self.velocidad_base = VELOCIDAD
		self.energia_base = ENERGIA
		self.armamento = []
		self.tipo_parte = TIPO_PARTE
	def get_peso(self):
		"""
		Devuelve el peso total de la parte. 
		Una parte pesa lo que pesa la sumatoria de sus armas más el peso base de la parte
		"""
		peso_total = self.peso_base
		for arma in armamento:
			peso_total += arma.get_peso()
		return peso_total

	def get_armadura(self):
		"""
		Devuelve la armadura total de la parte. Una parte 
		tiene tanta armadura como la sumatoria de la armadura de sus armas
		más la armadura base de la parte
		"""
		armadura_total = self.armadura_base
		for arma in armamento:
			armadura_total += arma.get_armadura()
		return armadura_total

	def get_escudo(self):
		"""
		Devuelve el escudo total de la parte. 
		Una parte tiene tanto escudo como la sumatoria del escudo de sus 
		armas más el escudo base de la parte 
		"""
		escudo_total = self.escudo_base
		for arma in armamento:
			escudo_total += arma.get_escudo()
		return escudo_total

	def get_velocidad(self):
		"""
		Devuelve la velocidad total de la parte. 
		Un Gunpla tiene tanta velocidad como la sumatoria de 
		las velocidades de sus partes y esqueleto
		"""
		velocidad_total = self.velocidad_base
		for arma in armamento:
			velodidad_total += arma.get_velocidad()
		return peso_total

	def get_energia(self):
		"""
		Devuelve la energía total de la parte. 
		La parte tiene tanta energía como la sumatoria de la energía de sus 
		armas más la energía base de la parte
		"""
		energia_total = self.energia_base
		for arma in armamento:
			energia_total += arma.get_energia()
		return peso_total

	def get_armamento(self):
		"""Devuelve una lista con todas las armas adosadas a la parte"""
		return self.armamento

	def get_tipo_parte(self):
		"""Devuelve una cadena que representa el tipo de parte."""
		return self.tipo_parte
master