NOMBRES_EQUIPO = ("Abomyzation","Ansatsu","Banshee","Bloodbane","Collapse","Cyberstein","Darkness","Defussion","Extermination","Flamecaster")


class Equipo:
	"""
	Representa un equipo de pilotos que tiene un nombre 
	y puede determinar que pilotos siguen vivos
	"""

	def __init__(self,pareja):
		"""Recibe una lista con los objetos Piloto pertenecientes al equipo"""

		self.pilotos = pareja
		self.pilotos_vivos = []
		self.nombre = random.choice(NOMBRES_EQUIPO)
	def get_pilotos_vivos(self):
		"""Devuelve una lista con los pilotos que siguen vivos"""
		for piloto in self.pilotos:
			if piloto.get_gunpla().get_energia_restante()<=0:
				continue
			self.pilotos_vivos.append()
		return self.pilotos_vivos

	def seleccionar_nombre(self):
		"""Selecciona el nombre del equipo"""
		self.nombre=random.choice(NOMBRES_EQUIPO)

	def get_nombre(self):
		"""Devuelve el nombre del equipo"""
		return self.nombre

class Participante:
	"""Representa un participante de un equipo, puede saber a que equipo pertenece"""

	def __init__(self,piloto,equipo):
		"""Recibe un objeto piloto y un objeto equipo"""
		self.piloto=piloto
		self.equipo=equipo

	def get_equipo(self):
		"""Devuelve el equipo del participante"""

		return self.equipo