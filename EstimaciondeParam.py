import numpy as np
import matplotlib.pyplot as plt


datos = np.genfromtxt('obs_data.dat', delimiter =' ')
datosX = datos[:,0]
datosY = datos[:,1]

pasos = 20000
def modelo(datosX, M, B):
	return datosX*M + B

def chi(yobservado, yModelo):
	chis = (1.0/2.0)*sum((yobservado - yModelo)**2)
	return np.exp(-chis)

#Pasos
pasosM = []
pasosB = []
listaChi =[]
paso0M = np.random.rand()
pasosM.append(paso0M)
paso0B = np.random.rand()
pasosB.append(paso0B)


#Prueba inicial modelo
yinicial = modelo(datosX, pasosM[0], pasosB[0])
chi0 = chi(datosY, yinicial)
listaChi.append(chi0)

for i in range(pasos):
	nextpasoM = np.random.normal(loc=paso0M)
	nextpasoB = np.random.normal(loc=paso0B)
	ynueva = modelo(datosX, nextpasoM, nextpasoB)
	chinuevo = chi(datosY, ynueva)
	alpha = chinuevo/chi0
	if alpha>=1.0:
		pasosM.append(nextpasoM)
		pasosB.append(nextpasoB)
		listaChi.append(chinuevo)
		paso0M = nextpasoM
		paso0B = nextpasoB
		chi0 = chinuevo
	else:
		beta = np.random.rand()
		if beta<alpha:
			pasosM.append(nextpasoM)
			pasosB.append(nextpasoB)
			listaChi.append(chinuevo)
			paso0M = nextpasoM
			paso0B = nextpasoB
			chi0 = chinuevo
		elif beta>alpha:
			pasosM.append(paso0M)
			pasosB.append(paso0B)
			listaChi.append(chi0)
			paso0M = paso0M
			paso0B = paso0B
			chi0 = chi0


#plt.scatter(pasosB, -np.log(listaChi))
#plt.show()

maxChi = np.argmax(listaChi)
mejorM = pasosM[maxChi]
mejorB = pasosB[maxChi]

MejorY = modelo(datosX, mejorM, mejorB)
plt.scatter(datosX, datosY)
plt.plot(datosX, MejorY)
plt.show()




