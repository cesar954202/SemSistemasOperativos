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
    def __init__(self,o1,o2,NumSig,NumLot,NumProce):
        self.operador1 = o1
        self.operador2 = o2
        self.signoNum = NumSig
        self.signo = ""
        self.resultado = 0
        self.Numlote = NumLot
        self.Numproceso = NumProce
        self.estado = "N"

    def do_operation(self):
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

    def mostrar(self,teclapress):
    	print "Realizado por Cesar Daniel Sanchez Navarro"
    	print "Numero de lote en ejecucion: ", self.Numlote
    	print "Numero de proceso en ejecucion: ", self.Numproceso
    	print "Tiempo Maximo estimado: 3 segundos"

        if teclado.teclapress == 'e':
            print "Interrupcion por entrada- salida"
        elif teclado.teclapress == 'w':
            print "Error "
        elif teclado.teclapress == 'p':
            print "Pausa "
        elif teclado.teclapress == 'c':
            print "Continua"

        operacion_tiempo_inicio = time.time()
    	self.do_operation()
        
        print "Operacion: ", self.operador1 , self.signo , self.operador2, " = ", self.resultado
        print "Duracion proceso: ", time.time() - operacion_tiempo_inicio
        
tiempo_inicio = time.time()

NumProcesos = int(input("Procesos necesarios: "))
#Calculo de lotes pendientes
NumLotesPendientes = NumProcesos // 4
aux = NumProcesos % 4
if(aux > 0):
	NumLotesPendientes = NumLotesPendientes + 1

print "Numero de lotes pendientes: ", NumLotesPendientes

#Se suma uno a procesos para problema de los arreglos
NumProcesos = NumProcesos +1
print ""

#llenado de procesos
NumLotes = 1
CuentaLote = 1
Procesos = []

for i in range(1,NumProcesos):
	aux = randrange(1,100)
	aux2 = randrange(1,100)
	auxS = randrange(1,7)

	NewProceso = proceso(aux,aux2,auxS,NumLotes,i)
	Procesos.append(NewProceso)

	if(CuentaLote < 4):
		CuentaLote = CuentaLote + 1
	else:
		CuentaLote = 1
		NumLotes = NumLotes+1

teclado = tecla()
hilo = threading.Thread(target=teclado.captura_letra)
hilo.start()

procesosDone = 0
i = 0
while i < len(Procesos):
    print "Lotes pendientes: ", NumLotesPendientes - Procesos[i].Numlote
    print "Proceso #", i
    time.sleep(2)



    Procesos[i].mostrar(teclado.teclapress)
    print "Tiempo transcurrido:", time.time() - tiempo_inicio, " segundos"
    print "Tiempo restante: ", ((NumProcesos-1) - procesosDone) * 3, " segundos"
    print "Procesos Terminados: ", procesosDone+1
    print "Contador Global tiempo: ", time.time() - tiempo_inicio, " segundos"
    print ""
    procesosDone = procesosDone +1
    i = i+1
    teclado.teclapress = 'N'

tiempo_duracion = time.time() - tiempo_inicio
print " "
print "Duracion del programa: ", tiempo_duracion

