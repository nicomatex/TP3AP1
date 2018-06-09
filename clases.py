import random

RANGO_ARMA_PESO = (2,10)
RANGO_ARMA_ARMADURA = (-5,20)
RANGO_ARMA_ESCUDO = (-4,10)
RANGO_ARMA_VELOCIDAD = (-4,10)
RANGO_ARMA_ENERGIA = (-4,10)
RANGO_ARMA_DANO = (5,20)
RANGO_ARMA_HITS = (1,3)
RANGO_ARMA_PRECISION = (1,50)
RANGO_ARMA_TIEMPO_RECARGA = (2,30)

CLASES_ARMA = ("GN Blade","Chaos Sword", "Frostmourne","Ashbringer","Elucidator")
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
		self.peso = random.randint(RANGO_PESO[0],RANGO_PESO[1])

