class Esqueleto:
	""" Represneta el esqueleto interno del Gunpla """

	def __init__(self):
		self.velocidad=VELOCIDAD
		self.energia=ENERGIA
		self.movilidad=MOVILIDAD
		self.slots=SLOTS

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
		self.peso_base=PESOBASE
		self.armadura_base=ARMADURA
		self.escudo_base=ESCUDO
		self.velocidad_base=VELOCIDAD
		self.energia_base=ENERGIA
		self.armamento=[]
		self.tipo_parte=TIPO_PARTE
	def get_peso(self):
		"""
		Devuelve el peso total de la parte. 
		Una parte pesa lo que pesa la sumatoria de sus armas más el peso base de la parte
		"""
		peso_total=self.peso_base
		for arma in armamento:
			peso_total+=arma.get_peso()
		return peso_total

	def get_armadura(self):
		"""
		Devuelve la armadura total de la parte. Una parte 
		tiene tanta armadura como la sumatoria de la armadura de sus armas
		más la armadura base de la parte
		"""
		armadura_total=self.armadura_base
		for arma in armamento:
			armadura_total+=arma.get_armadura()
		return armadura_total

	def get_escudo(self):
		"""
		Devuelve el escudo total de la parte. 
		Una parte tiene tanto escudo como la sumatoria del escudo de sus 
		armas más el escudo base de la parte 
		"""
		escudo_total=self.escudo_base
		for arma in armamento:
			escudo_total+=arma.get_escudo()
		return escudo_total

	def get_velocidad(self):
		"""
		Devuelve la velocidad total de la parte. 
		Un Gunpla tiene tanta velocidad como la sumatoria de 
		las velocidades de sus partes y esqueleto
		"""
		velocidad_total=self.velocidad_base
		for arma in armamento:
			velodidad_total+=arma.get_velocidad()
		return peso_total

	def get_energia(self):
		"""
		Devuelve la energía total de la parte. 
		La parte tiene tanta energía como la sumatoria de la energía de sus 
		armas más la energía base de la parte
		"""
		energia_total=self.energia_base
		for arma in armamento:
			energia_total+=arma.get_energia()
		return peso_total

	def get_armamento(self):
		"""Devuelve una lista con todas las armas adosadas a la parte"""
		return self.armamento

	def get_tipo_parte(self):
		"""Devuelve una cadena que representa el tipo de parte."""
		return self.tipo_parte
		