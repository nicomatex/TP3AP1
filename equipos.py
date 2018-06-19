class Equipo:
	"""Representa un equipo de pilotos"""

	def __init__(pilotos):
		"""Recibe una lista con los objetos Piloto pertenecientes al equipo"""

		self.pilotos = pilotos
		self.pilotos_vivos = []
	def get_pilotos_vivos():

		for _,piloto in self.pilotos:
			if piloto.get_gunpla().get_energia_restante()<=0:
				continue
			self.pilotos_vivos.append()
		return self.pilotos_vivos

