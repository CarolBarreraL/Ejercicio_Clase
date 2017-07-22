import numpy as np
import matplotlib.pyplot as plt

datos= np.genfromtxt("temperaturas.csv", delimiter=',', skip_header=1, usecols=(1,2,3,4))

a=(len(datos[0]),len(datos[0]))
MatrizCov=np.ones(a)

MatrizT = np.transpose(datos)
MatrizDatos = np.cov(MatrizT)
print MatrizDatos

for j in range(len(datos[0])):
	for i in range(len(datos[0])):
		cov=0
		k=1
		while k< len(datos):
			cov+= ((datos[k][i]- datos[:,i].mean())*(datos[k][j]- datos[:,j].mean()))/(len(datos)-1)
			k+=1
		MatrizCov[i][j]= cov

print MatrizCov

#print np.shape(datos)




