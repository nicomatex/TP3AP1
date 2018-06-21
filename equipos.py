import random

NOMBRES_EQUIPO = ("Abomyzation","Ansatsu","Banshee","Bloodbane","Collapse","Cyberstein","Darkness","Defussion","Extermination","Flamecaster")

class Equipo:
	'''
	Representa un equipo de participantes que tiene un nombre 
	y puede determinar que participantes siguen vivos
	'''

	def __init__(self):
		'''Recibe una lista con los objetos participante pertenecientes al equipo'''

		self.participantes = []
		self.nombre = ""
		
	def get_participantes_vivos(self):
		'''Devuelve una lista con los participantes que siguen vivos'''

		participantes_vivos = []

		for participante in self.participantes:
			if participante.get_piloto().get_gunpla().get_energia_restante()>0:
				participantes_vivos.append(participante)
		return participantes_vivos

	def get_participantes(self):
		'''
		Devuelve una lista con todos los participantes pertenecientes al equipo.
		'''
		return self.participantes

	def asignar_nombre(self,nombres_ocupados):
		'''Selecciona el nombre del equipo'''
		nombres_disponibles = [nombre for nombre in NOMBRES_EQUIPO if nombre not in nombres_ocupados]
		self.nombre=random.choice(NOMBRES_EQUIPO)
		return self.nombre

	def get_nombre(self):
		'''Devuelve el nombre del equipo'''
		return self.nombre

	def agregar_participante(self,participante):
		'''
		Recibe un participante y lo agrega al equipo.
		'''
		self.participantes.append(participante)

class Participante:
	'''Representa un participante de un equipo, puede saber a que equipo pertenece'''

	def __init__(self,piloto,equipo):
		'''Recibe un objeto participante y un objeto equipo'''
		self.piloto = piloto
		self.equipo = equipo

	def get_piloto(self):
		'''
		Devuelve el piloto al cual representa el participante.
		'''
		return self.piloto
		
	def get_equipo(self):
		'''Devuelve el equipo del participante'''

		return self.equipo