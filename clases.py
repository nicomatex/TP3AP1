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

class Parte:
	'''
	Representa una parte de un Gunpla.
	'''
	def __init__(self,peso,armadura,escudo_base,velocidad,energia_base,tipo_parte):
		'''
		Recibe enteros peso, armadura, escudo_base, velocidad, energia_base, y una cadena tipo_parte.
		'''
		self.armas_adosadas = {}
		self.peso = int(peso)
		self.armadura = int(armadura)
		self.escudo_base = int(escudo_base)
		self.energia_base = int(energia_base)
		self.velocidad = int(velocidad)
		self.tipo_parte = str(tipo_parte)

		#Invariantes
		self.energia = self.energia_base
		self.escudo = self.escudo_base

	