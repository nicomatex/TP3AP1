from clases import *
from Pila import *
from Cola import *
from piloto import *
from equipos import *
import time

TIEMPO_PRINTS = 0

CANTIDAD_ESQUELETOS = 10
CANTIDAD_PARTES = 30
CANTIDAD_ARMAS = 20

CANTIDAD_EQUIPOS = 2
PIOLOTOS_POR_EQUIPO = 4

TIPO_ARMA_MELEE = "MELEE"
TIPO_ARMA_RANGO = "RANGO"

PROBABILIDAD_COMBINACION_MELEE = 25
PROBABILIDAD_COMBINACION_RANGO = 15

FACTOR_DAÑO_CRITICO = 1.5
FACTOR_TURNO_BONUS = 0

PROBABILIDAD_DAÑO_CRITICO = 25

def generar_esqueletos():
	'''
	Devuelve una lista con CANTIDAD_ESQUELETOS de esqueletos generados de forma aleatoria.
	'''
	esqueletos = []

	for _ in range(CANTIDAD_ESQUELETOS):
		esqueletos.append(Esqueleto())

	return esqueletos

def generar_partes():
	'''
	Devuelve un diccionario cuyas claves son los tipos de partes disponibles y sus valores son pilas de partes de dicho tipo.
	'''
	partes = {}

	for _ in range(CANTIDAD_PARTES):
		parte = Parte()

		#Se adosan las armas correspondientes a la parte segun sus slots disponibles.
		for _ in range(parte.get_cantidad_slots()):
			parte.attach_arma(Arma())


		pila_tipo = partes.get(parte.get_tipo_parte(),Pila())
		pila_tipo.apilar(parte)
		partes[parte.get_tipo_parte()]=pila_tipo

	#Se generan las armas
	partes['Arma']= Pila()

	for _ in range(CANTIDAD_ARMAS):
		partes['Arma'].apilar(Arma())

	return partes

def generar_equipos():
	'''
	Genera los respectivos pilotos y los sortea dentro de equipos. Devuelve una lista con 
	los equipos.
	'''
	equipos = []
	nombres_ocupados = []

	for _ in range(CANTIDAD_EQUIPOS):

		equipo = Equipo()
		equipo.asignar_nombre(nombres_ocupados)
		nombres_ocupados.append(equipo.get_nombre())

		for _ in range(PIOLOTOS_POR_EQUIPO):
			equipo.agregar_participante(Participante(Piloto(),equipo))

		equipos.append(equipo)
	return equipos

def determinar_participantes(equipos):
	'''Recibe una lista con equipos y devuelve una lista con todos los participantes'''

	participantes = []
	nombres_ocupados = []

	for equipo in equipos:
		for participante in equipo.get_participantes():

			participante.asignar_nombre(nombres_ocupados)
			nombres_ocupados.append(participante.get_nombre())
			participantes.append(participante)

	return participantes

def elegir_esqueletos(participantes,esqueletos):
	'''
	Recibe una lista de participantes y una lista de esqueletos y le permite a cada participante elegir 
	el esqueleto que quiere para su gunpla. No devuelve nada.
	'''
	
	pilotos = [participante.get_piloto() for participante in participantes]
	random.shuffle(pilotos)

	for piloto in pilotos:
		indice_esqueleto_elegido = piloto.elegir_esqueleto(esqueletos)

		#Se instancia un nuevo gunpla con el esqueleto elegido.
		piloto.set_gunpla(Gunpla(esqueletos[indice_esqueleto_elegido]))

def elegir_partes(pila_partes,participantes):
	'''
	Recibe un diccionario partes de la forma <tipo_parte:pila con partes de ese tipo> y una lista de 
	tuplas de la forma <numero de piloto,piloto>
	pilotos, y devuelve un diccionario de la forma
	{(numero de piloto, piloto):[Lista de partes reservadas por el piloto]}
	'''
	pilotos = []
	

	for participante in participantes:
		pilotos.append(participante.get_piloto())

	partes_reservadas = {piloto:[] for piloto in pilotos}

	todas_vacias = False
	piloto_eligiendo = 0

	while True:
		partes = {}
		todas_vacias = True

		for tipo_parte in pila_partes:
			if not pila_partes[tipo_parte].esta_vacia():
				todas_vacias = False
				partes[tipo_parte] = pila_partes[tipo_parte].ver_tope()

		#Condicion de corte: Que esten todas las pilas vacias.
		if todas_vacias:
			break


		elector = pilotos[piloto_eligiendo]
		tipo_parte_elegida = elector.elegir_parte(partes)
		partes_reservadas[elector].append(pila_partes[tipo_parte_elegida].desapilar())

		if pila_partes[tipo_parte_elegida].esta_vacia():
			pila_partes.pop(tipo_parte_elegida)

		piloto_eligiendo+=1

		if piloto_eligiendo>len(pilotos)-1:
			piloto_eligiendo=0

	return partes_reservadas

def equipar_gunplas(partes_reservadas):
	'''
	Recibe un diccionario de la forma {piloto:[lista de partes elegidas]}
	y equipa el gunpla de cada piloto con las partes elegidas de entre las partes reservadas. No devuelve nada.
	'''

	for piloto in partes_reservadas:

		partes_seleccionadas = piloto.elegir_combinacion(partes_reservadas[piloto])

		for parte in partes_seleccionadas:

			if parte.get_tipo_parte()=="Arma":
				piloto.get_gunpla().attach_arma(parte)
			else:
				piloto.get_gunpla().attach_parte(parte)


def determinar_oponentes_validos(participante_atacante,equipos):

	'''
	Recibe el participante para el cual se desea determinar los oponentes validos y una lista de equipos, 
	y devuelve una lista de gunplas validos para atacar.
	'''

	oponentes_validos = []

	for equipo in equipos:

		if equipo == participante_atacante.get_equipo():
			continue
		for participante in equipo.get_participantes_vivos():
			oponentes_validos.append(participante.get_piloto().get_gunpla())

	return oponentes_validos

def ordenar_participantes(participantes):
	'''
	Recibe una lista de participantes y los ordena segun la velocidad de sus gunplas.
	'''

	participantes.sort(key = lambda participante: participante.get_piloto().get_gunpla().get_velocidad(), reverse = True)


def inicializar_turnos(participantes):
	'''
	Recibe una lista de participantes ordenados segun la velocidad de sus gunplas y devuelve una cola 
	de "turnos" donde el primer turno corresponde al gunpla mas rapido y el ultimo al mas lento.
	'''
	cola_turnos = Cola()

	for participante in participantes:
		cola_turnos.encolar(participante)

	return cola_turnos

def calcular_daño(arma,piloto,oponente,armas_usadas,contraataque=False):
	'''
	Recibe un arma, un piloto y un gunpla oponente y devuelve el daño que esta realizara al gunpla oponente. 
	Recibe opcionalmente un parametro booleano contraataque. 
	'''
	daño_total = 0

	for i in range(arma.get_hits()):

		if random.random() < arma.get_precision()/100:
			if random.random() < (arma.get_precision()*PROBABILIDAD_DAÑO_CRITICO)/100:
				daño_total+= arma.get_daño()*FACTOR_DAÑO_CRITICO
			else:
				daño_total+= arma.get_daño()

		if contraataque:
			continue

		tipo = arma.get_tipo()

		#Calculo de combinacion de armas.
		if tipo==TIPO_ARMA_MELEE or tipo==TIPO_ARMA_RANGO:

			if random.random() < (PROBABILIDAD_COMBINACION_MELEE if tipo==TIPO_ARMA_MELEE else PROBABILIDAD_COMBINACION_RANGO)/100:
				arma_elegida = piloto.elegir_arma(oponente,True,arma)

				if not arma_elegida:
					daño_total+=0
				else:
					arma_elegida.usar()
					armas_usadas.append(arma_elegida)
					daño_total+= calcular_daño(arma_elegida,piloto,oponente,armas_usadas)

	return daño_total

def actualizar_armas(armas_usadas):
	'''
	Recibe una lista de armas usadas y actualiza sus tiempos de recarga.
	'''
	armas_listas=[]

	for arma in armas_usadas:

		arma.recargar()

		if arma.esta_lista():
			armas_listas.append(arma)

	for arma_lista in armas_listas:
		armas_usadas.remove(arma_lista)

def reiniciar_armas(armas_usadas):
	'''
	Recibe una lista de las armas usadas y las setea a todas listas para usar.
	'''
	for arma in armas_usadas:
		arma.reiniciar()
	armas_usadas.clear()

def determinar_equipos_vivos(equipos):
	'''
	Recibe una lista de equipos y devuelve una lista con aquellos que tengan al menos un piloto cuyo gunpla este vivo.
	'''
	equipos_vivos = []

	for equipo in equipos:

		'''for participante in equipo.get_participantes():

			if participante.get_piloto().get_gunpla().get_energia_restante()>0:
				equipos_vivos.append(equipo)
				break'''
		if equipo.get_participantes_vivos():
			equipos_vivos.append(equipo)

	return equipos_vivos

def determinar_gunplas_activos(equipos):
	'''
	Recibe una lista de equipos y devuelve una lista con todos los gunpals activos de todos los equipos.
	'''
	gunplas_activos = []

	for equipo in equipos:

		participantes_vivos = equipo.get_participantes_vivos()

		for participante in participantes_vivos:
			gunplas_activos.append(participante.get_piloto().get_gunpla())

	return gunplas_activos

def contraatacar(participante_oponente,atacante,armas_usadas):
	'''
	Recibe un participante oponente, el atacante y una lista de armas usadas 
	devuelve False si el oponente no tiene arams para contraataar, en caso contrario
	contraataca y devuelve True
	'''
	contraatacante = participante_oponente.get_piloto()
	arma_contraataque = contraatacante.elegir_arma(atacante.get_gunpla())
	nombre_oponente = participante_oponente.get_nombre()

	if not arma_contraataque:
		print("{} no tiene armas para contraatacar".format(nombre_oponente))
		time.sleep(TIEMPO_PRINTS)
		return False

	arma_contraataque.usar()
	daño_contraataque = calcular_daño(arma_contraataque,contraatacante,atacante.get_gunpla(),armas_usadas,True)
	daño_efectivo_contraataque = atacante.get_gunpla().recibir_daño(daño_contraataque,arma_contraataque.get_tipo_municion())
	print("{} contraataca, causando {} de daño".format(nombre_oponente,daño_contraataque))
	time.sleep(TIEMPO_PRINTS)

	return True

def elegir_oponente(participante_atacante,participantes,equipos):
		'''
		Recibe un participante atacante, una lista de participantes y una lista de equipos, y devuelve el gunpla oponente elegido, 
		el nombre del piloto, el equipo al que pertenece y el objeto participante correspondiente al piloto.
		'''

		oponentes_posibles = determinar_oponentes_validos(participante_atacante,equipos)
		atacante = participante_atacante.get_piloto()
		
		indice_oponente_elegido = atacante.elegir_oponente(oponentes_posibles)
		gunpla_oponente_elegido = oponentes_posibles[indice_oponente_elegido]

		#Se busca a que participante pertenece el oponente gunpla elegido.
		for participante in participantes:
			if participante.get_piloto().get_gunpla()==gunpla_oponente_elegido:
				participante_oponente = participante
				break

		nombre_oponente = participante_oponente.get_nombre()
		equipo_oponente = participante_oponente.get_equipo().get_nombre()
		
		return gunpla_oponente_elegido, nombre_oponente, equipo_oponente,participante_oponente

def eliminar_gunpla(equipos,participante_oponente,daño_efectivo,gunpla_oponente_elegido,nombre_atacante):
	'''
	Recibe una lista de equipos, el objeto participante oponente, el daño efectivo realizado, el objeto gunpla del oponente, y el nombre del atacante. Devuelve
	la lista actualizada de gunplas activos, de equipos vivos, de participantes vivos, y un booleano overkill.
	'''
	overkill= False

	nombre_oponente = participante_oponente.get_nombre()

	print("{} fue eliminado".format(nombre_oponente))
	time.sleep(TIEMPO_PRINTS)

	gunplas_activos = determinar_gunplas_activos(equipos)
	equipos_vivos = determinar_equipos_vivos(equipos)
	participantes_vivos = participante_oponente.get_equipo().get_participantes_vivos()


	if daño_efectivo > gunpla_oponente_elegido.get_energia()*FACTOR_TURNO_BONUS/100:
		overkill = True
		print("¡¡¡OVERKILL!!! {} recibe un turno adicional".format(nombre_atacante))
		time.sleep(TIEMPO_PRINTS)

	return gunplas_activos,equipos_vivos,participantes_vivos,overkill


def ciclo_juego(equipos,turnos,participantes):
	'''
	Recibe una lista de equipos, una cola de turnos y una lista de participantes. Es el ciclo principal del juego.
	'''

	equipos_vivos = determinar_equipos_vivos(equipos)
	gunplas_activos = determinar_gunplas_activos(equipos)

	armas_usadas = [] #Lista para almacenar las armas que estan en su tiempo de recarga.

	turno = 0

	while len(determinar_equipos_vivos(equipos))>=2:

		participante_atacante = turnos.desencolar()
		
		nombre_atacante = participante_atacante.get_nombre()

		atacante = participante_atacante.get_piloto()
		#Se saltean los turnos pertenecientes a gunplas muertos.
		if atacante.get_gunpla() not in gunplas_activos:
			continue

		turno += 1
		
		print("[~~~~~~~~~~~~~~~~~~~~~~{{{}}}~~~~~~~~~~~~~~~~~~~~~~]".format(turno))
		time.sleep(TIEMPO_PRINTS)
		print("Es el turno de {} del equipo {}".format(nombre_atacante,participante_atacante.get_equipo().get_nombre()))
		time.sleep(TIEMPO_PRINTS)

		#Se actualiza el tiempo recarga de las armas
		actualizar_armas(armas_usadas)

		gunpla_oponente_elegido, nombre_oponente, equipo_oponente,participante_oponente = elegir_oponente(participante_atacante,participantes,equipos)
		
		participantes_vivos = participante_oponente.get_equipo().get_participantes_vivos()
		
		print("Va a atacar a {} del equipo {}".format(nombre_oponente,equipo_oponente))
		time.sleep(TIEMPO_PRINTS)
		#Se elige con que arma atacar
		arma_elegida = atacante.elegir_arma(gunpla_oponente_elegido)

		if not arma_elegida:
			#reiniciar_armas(armas_usadas)
			turnos.encolar(participante_atacante)
			print("{} no tiene armas disponibles y pierde su turno...".format(nombre_atacante))
			time.sleep(TIEMPO_PRINTS)

			continue

		#Se establece el tiempo de recarga del arma
		arma_elegida.usar()
		armas_usadas.append(arma_elegida)

		#Se calcula el daño y el daño efectivo 
		daño = calcular_daño(arma_elegida,atacante,gunpla_oponente_elegido,armas_usadas)
		daño_efectivo = gunpla_oponente_elegido.recibir_daño(daño,arma_elegida.get_tipo_municion())
		print("{} ataca a {} con {} y causa {} puntos de daño".format(nombre_atacante,nombre_oponente,arma_elegida.get_clase(),daño))
		time.sleep(TIEMPO_PRINTS)

		if daño_efectivo==0:
			turnos.encolar(participante_oponente)

		if gunpla_oponente_elegido.get_energia_restante()<=0:
			print("{} fue eliminado".format(nombre_oponente))
			time.sleep(TIEMPO_PRINTS)

			gunplas_activos,equipos_vivos,participantes_vivos,overkill = eliminar_gunpla(equipos,participante_oponente,daño_efectivo,gunpla_oponente_elegido,nombre_atacante)

			if overkill:
				turnos.encolar(participante_atacante)

			print("Al equipo {} le quedan {} participantes vivos".format(equipo_oponente,len(participantes_vivos)))	

			turnos.encolar(participante_atacante)
			continue

		#Se calcula el contraataque.
		if arma_elegida.get_tipo()==TIPO_ARMA_MELEE:

			if not contraatacar(participante_oponente,atacante,armas_usadas): #Comprobacion de arma disponible para contraatacar.
				turnos.encolar(participante_atacante)
				gunplas_activos = determinar_gunplas_activos(equipos)
				continue


		gunplas_activos = determinar_gunplas_activos(equipos)

		turnos.encolar(participante_atacante)

def main():

	equipos = generar_equipos()
	participantes = determinar_participantes(equipos)
	partes = generar_partes()
	esqueletos = generar_esqueletos()
	elegir_esqueletos(participantes,esqueletos)
	reservadas = elegir_partes(partes,participantes)
	equipar_gunplas(reservadas)
	ordenar_participantes(participantes)
	turnos = inicializar_turnos(participantes)

	ciclo_juego(equipos,turnos,participantes)
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print()
	print("El equipo ganador es {}".format(determinar_equipos_vivos(equipos)[0].get_nombre()))

main()