from clases import *
from Pila import *
from Cola import *
from piloto import *

CANTIDAD_ESQUELETOS = 10
CANTIDAD_PARTES = 10
CANTIDAD_ARMAS = 10
CANTIDAD_PILOTOS = 4

TIPO_ARMA_MELEE = "MELEE"
TIPO_ARMA_RANGO = "RANGO"

PROBABILIDAD_COMBINACION_MELEE = 5
PROBABILIDAD_COMBINACION_RANGO = 5


FACTOR_DAÑO_CRITICO = 1.5
FACTOR_TURNO_BONUS = 5

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

def generar_pilotos():
	'''
	Recibe un entero cantidad_pilotos y devuelve una lista de tuplas de la forma <numero de piloto, piloto> con 
	esa cantidad de pilotos.
	'''
	lista_pilotos = []

	for i in range(0,CANTIDAD_PILOTOS):
		lista_pilotos.append((i,Piloto()))

	return lista_pilotos

def elegir_esqueletos(pilotos,esqueletos):
	'''
	Recibe una lista de pilotos y una lista de esqueletos y le permite a cada piloto elegir 
	el esqueleto que quiere para su gunpla. No devuelve nada.
	'''
	
	#
	random.shuffle(pilotos)

	for _,piloto in pilotos:
		indice_esqueleto_elegido = piloto.elegir_esqueleto(esqueletos)

		#Se instancia un nuevo gunpla con el esqueleto elegido.
		piloto.set_gunpla(Gunpla(esqueletos[indice_esqueleto_elegido]))

def elegir_partes(partes,pilotos):
	'''
	Recibe un diccionario partes de la forma <tipo_parte:pila con partes de ese tipo> y una lista de 
	tuplas de la forma <numero de piloto,piloto>
	pilotos, y devuelve un diccionario de la forma
	{(numero de piloto, piloto):[Lista de partes reservadas por el piloto]}
	'''

	partes_reservadas = {piloto:[] for piloto in pilotos}

	piloto_eligiendo = 0

	todas_vacias = False

	while True:

		todas_vacias = True
		for tipo_parte in partes:
			if not partes[tipo_parte].esta_vacia():
				todas_vacias = False

		#Condicion de corte: Que esten todas las pilas vacias.
		if todas_vacias:
			break

		elector = pilotos[piloto_eligiendo]
		tipo_parte_elegida = elector[1].elegir_parte(partes)
		partes_reservadas[elector].append(partes[tipo_parte_elegida].desapilar())

		if partes[tipo_parte_elegida].esta_vacia():
			partes.pop(tipo_parte_elegida)

		piloto_eligiendo+=1

		if piloto_eligiendo>len(pilotos)-1:
			piloto_eligiendo=0

	return partes_reservadas

def equipar_gunplas(partes_reservadas):
	'''
	Recibe un diccionario de la forma {(numero de piloto,piloto):[lista de partes elegidas]}
	y equipa el gunpla de cada piloto 
	con las partes elegidas de entre las partes reservadas. No devuelve nada.
	'''

	for piloto in partes_reservadas:

		partes_seleccionadas = piloto[1].elegir_combinacion(partes_reservadas[piloto])

		for parte in partes_seleccionadas:
			if parte.get_tipo_parte()=="Arma":
				piloto[1].get_gunpla().attach_arma(parte)
			else:
				piloto[1].get_gunpla().attach_parte(parte)

def ordenar_pilotos(pilotos):
	'''
	Recibe una lista de tuplas de la forma <numero de piloto,piloto> y devuelve 
	una lista de los pilotos ordenados segun la velocidad de sus gunplas.
	'''

	pilotos.sort(key = lambda piloto: piloto[1].get_gunpla().get_velocidad(), reverse = True)


def inicializar_turnos(pilotos):
	'''
	Recibe una lista de pilotos ordenados segun la velocidad de sus gunplas y devuelve una cola 
	de "turnos" donde el primer turno corresponde al gunpla mas rapido y el ultimo al mas lento.
	'''
	cola_turnos = Cola()

	for piloto in pilotos:
		cola_turnos.encolar(piloto)

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


		#Calculo de combinacion de armas.
		if arma.get_tipo()==TIPO_ARMA_MELEE:

			if random.random() < PROBABILIDAD_COMBINACION_MELEE/100:

				arma_elegida = piloto.elegir_arma(oponente)
				arma_elegida.usar()
				armas_usadas.append(arma_elegida)
				daño_total+= calcular_daño(arma_elegida,piloto,oponente,armas_usadas)

		elif arma.get_tipo()==TIPO_ARMA_RANGO:

			if random.random() < PROBABILIDAD_COMBINACION_RANGO/100:

				arma_elegida = piloto.elegir_arma(oponente)
				arma_elegida.usar()
				armas_usadas.append(arma_elegida)
				daño_total+= calcular_daño(arma_elegida,piloto,oponente,armas_usadas)

	return daño_total


def main():

	pilotos = generar_pilotos()

	#print(pilotos)#Debug

	partes = generar_partes()
	esqueletos = generar_esqueletos()
	elegir_esqueletos(pilotos,esqueletos)
	reservadas = elegir_partes(partes,pilotos)
	equipar_gunplas(reservadas)
	ordenar_pilotos(pilotos)

	#print(ordenados)#Debug

	turnos = inicializar_turnos(pilotos)

	gunplas_activos = [piloto[1].get_gunpla() for piloto in pilotos]
	armas_usadas = [] #Lista para almacenar las armas que estan en su tiempo de recarga.

	while len(gunplas_activos)>=2:
		
		numero_piloto, atacante = turnos.desencolar()

		#Se saltean los turnos pertenecientes a gunplas muertos.
		if atacante.get_gunpla() not in gunplas_activos:
			continue


		print("#-------------------#")
		print("Es el turno de atacar de Piloto {}!".format(numero_piloto))


		#Se actualiza el tiempo recarga de las armas
		armas_listas=[]

		for arma in armas_usadas:
			arma.recargar()

			if arma.esta_lista:
				armas_listas.append(arma)

		for arma_lista in armas_listas:
			armas_usadas.remove(arma_lista)


		indice_oponente_elegido = atacante.elegir_oponente(gunplas_activos)
		oponente_elegido = gunplas_activos[indice_oponente_elegido]

		#Se busca el piloto al cual le pertenece el gunpla elegido
		piloto_oponente= pilotos[0]

		for piloto in pilotos:
			if piloto[1].get_gunpla()==oponente_elegido:
				piloto_oponente=piloto
				break

		print("El oponente elegido por Piloto {} es Piloto {}!".format(numero_piloto,piloto_oponente[0]))
		arma_elegida = atacante.elegir_arma(oponente_elegido)
		arma_elegida.usar()
		armas_usadas.append(arma_elegida)

		daño = calcular_daño(arma_elegida,atacante,oponente_elegido,armas_usadas)
		daño_efectivo = oponente_elegido.recibir_daño(daño,arma_elegida.get_tipo_municion())

		if daño_efectivo==0:
			turnos.encolar(piloto_oponente)


		if oponente_elegido.get_energia_restante()<=0:
			print("Piloto {} fue eliminado :(".format(piloto_oponente[0]))

			if daño_efectivo > oponente_elegido.get_energia()*FACTOR_TURNO_BONUS/100:
				turnos.encolar((numero_piloto,atacante))

			gunplas_activos.remove(oponente_elegido)
			turnos.encolar((numero_piloto,atacante))
			continue

		if arma_elegida.get_tipo_municion()==TIPO_ARMA_MELEE:

			numero_piloto_contraataque,contraatacante = piloto_oponente 
			arma_contraataque = contraatacante.elegir_arma(atacante)
			arma_contraataque.usar()

			daño_contraataque = calcular_daño(arma_contraataque,contraatacante,atacante,armas_usadas,True)

			atacante.get_gunpla().recibir_daño(daño_contraataque,arma_contraataque.get_tipo_municion())

			if atacante.get_gunpla().get_energia_restante<=0:
				gunplas_activos.remove(atacante.get_gunpla())
				continue

		turnos.encolar((numero_piloto,atacante))

	#Se busca a que piloto le pertenece el gunpla vencedor.
	vencedor = pilotos[0]

	for piloto in pilotos:
		if piloto[1].get_gunpla()==gunplas_activos[0]:
			vencedor=piloto
			break

	print("EL GRAN VENCEDOR ES PILOTO {}!!".format(vencedor[0]))
main()