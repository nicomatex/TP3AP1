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
		
		'''