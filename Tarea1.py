import math
from timeit import timeit
from time import time

class proceso:
    def __init__(self,o1,o2,NumSig,NumLot,NumProce):
        self.operador1 = o1
        self.operador2 = o2
        self.signoNum = NumSig
        self.signo
        self.resultado = 0
        self.Numlote = NumLot
        self.Numproceso = NumProce
        self.tiempo

    def do_operation():
    	if(signoNum == 1):
    		self.signo = '+'
    		self.resultado = self.operador1 + self.operador2
    	elif(signoNum == 2):
    		self.signo = '-'
    		self.resultado = self.operador1 - self.operador2
    	elif(signoNum == 3):
    		self.signo = '*'
    		self.resultado == self.operador1 * self.operador2
    	elif(signoNum == 4):
    		self.signo = '/'
    		self.resultado = self.operador1 / self.operador2
    	elif(signoNum == 5):
    		self.signo = "%/residuo"
    		self.resultado = self.operador1 % self.operador2
    	elif(signoNum == 6):
    		self.signo = 'raiz'
    		self.operador2 = 2
    		self.resultado = sqrt(self.operador1)
    	elif(signoNum == 7):
    		self.signo = ' porciento de '
    		self.resultado = (self.operador1 * 100) / self.operador2

    def mostrar(self):
    	print "Realizado por Cesar Daniel Sanchez Navarro"
        print "Operacion: ", self.operador1 , self.signo , self.operador2, " = ", self.resultado


NumProcesos = int(input("Procesos necesarios: "))
NumLotes = NumProcesos // 4
aux = NumProcesos % 4
if(aux > 0):
	NumLotes = NumLotes + 1


print "Numero de lotes", NumLotes


###Imprimir
#Lotes pendientes
#Numero de programa
#Tiempo Maximo estimado
#Proceso en ejecucion
##Nombre
##Operacion
##Tiempo Maximo estimado
##Numeo de programa
#Procesos terminados
#Numero de programa
#Operacion y datos
#Resultado de operacion
#Contador Global


