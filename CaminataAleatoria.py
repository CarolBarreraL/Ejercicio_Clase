import numpy as np
import matplotlib.pyplot as plt

pasos = 10000
def funcionFea(x):
	x0 = 3.0
	a = 0.01
	return np.exp(-(x**2))/((x-x0)**2 + a**2)

x=np.linspace(-4.0,4.0, 1000)
f = funcionFea(x)


#Pasos
pasosLista = []
xpaso0 = (np.random.rand()-0.5)*0.8
pasosLista.append(xpaso0)

for i in range(pasos):
	xPasoSiguiente = np.random.normal(loc=xpaso0)
	alpha = funcionFea(xPasoSiguiente)/funcionFea(xpaso0)
	if alpha>1.0:
		pasosLista.append(xPasoSiguiente)
		xpaso0 = xPasoSiguiente
	elif alpha<1.0:
		beta = np.random.rand()
		if beta<alpha:
			pasosLista.append(xPasoSiguiente)
			xpaso0 = xPasoSiguiente
		elif beta>alpha:
			pasosLista.append(xpaso0)
			xpaso0 = xpaso0


plt.hist(pasosLista, normed =True, bins =100 )
plt.plot(x,f/sum(f*(x[1]-x[0])))
plt.show()
