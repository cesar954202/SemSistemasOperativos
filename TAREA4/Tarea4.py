import math
import time
from random import randrange
import msvcrt
import threading

class tecla:
	def __init__(self):
		self.teclapress = "N"

	def getTeclapress(self):
		return self.teclapress

	def captura_letra(self):
		i = 1
		while i != 0:
		   char = msvcrt.getch()
		   print "PRESIONASTE ", char
		   self.teclapress = char

class proceso:
	def __init__(self,o1,o2,NumSig,NumProce,tiempo,Quantum):
		self.operador1 = o1
		self.operador2 = o2
		self.signoNum = NumSig
		self.signo = ""
		self.resultado = 0
		self.Numproceso = NumProce
		self.estado = "n"
		self.tiempoServicio = tiempo
		self.tiempoPorcesado = 0
		self.Quantum = Quantum
		self.QuantumRecorrido = 0
		self.TiempoBloqueado = 0

	def do_operation(self):
		print "Tiempo de servicio necesario", self.tiempoServicio
		if self.tiempoPorcesado == self.tiempoServicio:
			if(self.signoNum == 1):
				self.signo = '+'
				self.resultado = self.operador1 + self.operador2
			elif(self.signoNum == 2):
				self.signo = '-'
				self.resultado = self.operador1 - self.operador2
			elif(self.signoNum == 3):
				self.signo = '*'
				self.resultado == self.operador1 * self.operador2
			elif(self.signoNum == 4):
				self.signo = '/'
				self.resultado = self.operador1 / self.operador2
			elif(self.signoNum == 5):
				self.signo = "%/residuo"
				self.resultado = self.operador1 % self.operador2
			elif(self.signoNum == 6):
				self.signo = 'raiz'
				self.operador2 = 2
				self.resultado = math.sqrt(self.operador1)
			elif(self.signoNum == 7):
				self.signo = ' porciento de '
				self.resultado = (self.operador1 * 100) / self.operador2
			self.estado = "t"
			print "Operacion: ", self.operador1 , self.signo , self.operador2, " = ", self.resultado
		else:
			self.estado = 'l'
			self.tiempoPorcesado = self.tiempoPorcesado + 1
			self.QuantumRecorrido = self.QuantumRecorrido + 1
			time.sleep(1)

	def mostrar(self,teclapress):
		print "Numero de proceso en ejecucion: ", self.Numproceso
		print "Tiempo Maximo estimado:", self.tiempoServicio, " segundos"

		if teclapress == 'e':
			print "INTERRUPCION POR ENTRADA-SALIDA"
			print ""
			self.estado = 'e'

		elif teclapress == 'w':
			print "SE DETIENE PROCESO POR ERROR"
			print ""
			self.estado = 'w'

		elif teclapress == 'p':
			char = 'p'
			while char != 'c':
				print "SE MANTIENE PROCESO EN PAUSA"
				print ""
				char = msvcrt.getch()
				print "Ingresaste ", char
				print ""

			print "PROCESO CONTINUA"
			print ""
			self.do_operation()

		elif teclapress == 'c':
			print "CONTINUA NO HAY PROCESO EN PAUSA"
			print ""
		else:
			self.do_operation()

	def sumarBloqueado(sel):
		self.self.TiempoBloqueado = self.self.TiempoBloqueado + 1
		if(self.self.TiempoBloqueado == 9):
			self.estado = 'l'
			self.TiempoBloqueado = 0
 

tiempo_inicio = time.time()
print "Realizado por Cesar Daniel Sanchez Navarro"

NumProcesos = int(input("Procesos iniciales: "))
Quantum = int(input("Quantum: "))


#Se suma uno a procesos para problema de los arreglos
NumProcesos = NumProcesos +1
print ""

#llenado de procesos
NumLotes = 1
Procesos = []
ProcesosBloqueados = []
ProcesosTerminados = []

for i in range(1,NumProcesos):
	aux = randrange(1,100)
	aux2 = randrange(1,100)
	auxS = randrange(1,7)
	auxT = randrange(1,10)
	NewProceso = proceso(aux,aux2,auxS,i,auxT,Quantum)
	Procesos.append(NewProceso)


teclado = tecla()
hilo = threading.Thread(target=teclado.captura_letra)
hilo.start()

while 0 != len(Procesos) or 0 != len(ProcesosBloqueados):
	#print "Proceso #", i+1
	#Procesos[i].mostrar(teclado.teclapress)

	for i in ProcesosBloqueados:
		i.sumarBloqueado()
	i = 0

	while i < len(ProcesosBloqueados):
		if ProcesosBloqueados[i].estado == 'l':
			aux = ProcesosBloqueados[i]
			ProcesosBloqueados.pop(i)

	if 0 != len(Procesos):
		Procesado = Procesos[0]
		Procesos.pop(0)

		while Procesado.estado != 't' and Procesado.estado != 'w' and Procesado.estado != 'e' and Procesado.QuantumRecorrido != Quantum:
			print "PID ", Procesado.Numproceso 
			print "Quantum recorrido", Procesado.QuantumRecorrido
			print "Estado ", Procesado.estado
			Procesado.mostrar(teclado.teclapress)
		Procesado.QuantumRecorrido = 0

		#movimiento de proceso
		if(Procesado.estado == 't' or Procesado.estado == 'w'):
			ProcesosTerminados.append(Procesado)
		elif(Procesado.estado == 'l'):
			Procesos.append(Procesado)
		elif(Procesado.estado == 'e'):
			ProcesosBloqueados.append(Procesado)

		print "Tiempo transcurrido:", time.time() - tiempo_inicio, " segundos"

		if teclado.teclapress == 'b':
			print "Procesos Nuevos: ===================="
			for i in Procesos:
				if i.estado == 'n':
					print "PID: ", i.Numproceso, "Estado: ", i.estado, "Tiempo en el procesador: ", i.tiempoPorcesado

			print "Procesos Listos: ===================="
			for i in Procesos:
				if i.estado == 'l':
					print "PID: ", i.Numproceso, "Estado: ", i.estado, "Tiempo en el procesador: ", i.tiempoPorcesado

			print "Procesos Bloqueados: ===================="
			for i in ProcesosBloqueados:
				print "PID: ", i.Numproceso, "Estado: ", i.estado, "Tiempo en el procesador: ", i.tiempoPorcesado

			print "Procesos Terminados: ===================="
			for i in ProcesosTerminados:
				print "PID: ", i.Numproceso, "Estado: ", i.estado, "Tiempo en el procesador: ", i.tiempoPorcesado
		if teclado.teclapress == 'n':
			aux = randrange(1,100)
			aux2 = randrange(1,100)
			auxS = randrange(1,7)
			auxT = randrange(1,10)
			NewProceso = proceso(aux,aux2,auxS,i,auxT,Quantum)
			Procesos.append(NewProceso)
			print "SE AGREGO NUEVO PROCESO"
			print ""


	teclado.teclapress = 'N'

tiempo_duracion = time.time() - tiempo_inicio
print " "
print "Duracion del programa: ", tiempo_duracion

print "Procesos Nuevos: ===================="
for i in Procesos:
	if i.estado == 'n':
		print "PID: ", i.Numproceso, "Estado: ", i.estado, "Tiempo en el procesador: ", i.tiempoPorcesado

print "Procesos Listos: ===================="
for i in Procesos:
	if i.estado == 'l':
		print "PID: ", i.Numproceso, "Estado: ", i.estado, "Tiempo en el procesador: ", i.tiempoPorcesado

print "Procesos Bloqueados: ===================="
for i in ProcesosBloqueados:
	print "PID: ", i.Numproceso, "Estado: ", i.estado, "Tiempo en el procesador: ", i.tiempoPorcesado

print "Procesos Terminados: ===================="
for i in ProcesosTerminados:
	print "PID: ", i.Numproceso, "Estado: ", i.estado, "Tiempo en el procesador: ", i.tiempoPorcesado

