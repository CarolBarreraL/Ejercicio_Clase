import numpy as np
import matplotlib.pyplot as plt

def funderiv(x):
	return np.cos(x)

#Funcion a comparar
def derivadaFija(x):
	return -np.sin(x)

a=0
b=8
N=2
listah=[0]
ListaerrorFD=[]
ListaerrorBD=[]
ListaerrorCD=[]
ListaerrorED=[]

def derivadas():
	while N < 100:
	t= np.linspace(a,b,N)
	h = (b-a)/(N-1)
	listah.append(h)
	DerivAnalitica = derivadaFija(t)
	#FD
	derivadaFD = np.array((funderiv(t+h)- funderiv(t))/(h))
	errorFD = derivadaFD[10] - derivAnalitica[10]
	ListaerrorFD.append(errorFD)

	#BD
	derivadaBD = np.array((funderiv(t)- funderiv(t-h))/(h))
	errorBD = derivadaBD[10] - derivAnalitica[10]	
	ListaerrorBD.append(errorBD)

	#CD
	derivadaCD = np.array((funderiv(t+h/2.0)- funderiv(t-h/2.0))/(h))
	errorCD = derivadaCD[10] - derivAnalitica[10]
	ListaerrorCD.append(errorCD)

	#ED
	derivadaED = np.array((4.0*((funderiv(t+h/4.0)- funderiv(t-h/4.0))/(h/2.0))+ (funderiv(t+h/2.0)- funderiv(t-h/2.0))/(h))/3.0)
	errorED = derivadaED[10] - derivAnalitica[10]
	ListaerrorED.append(errorED)
	N+=1

plt.plot(listah, ListaerrorFD, c='b', label='FD')	
plt.plot(listah, ListaerrorBD, c='b', label='FD')
plt.plot(listah, ListaerrorCD, c='b', label='FD')
plt.plot(listah, ListaerrorED, c='b', label='FD')
plt.label()
plt.show()


