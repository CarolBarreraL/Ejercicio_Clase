import numpy as np
import matplotlib.pyplot as plt

datos = np.genfromtxt('temperaturas.csv', skip_header=1, usecols=(1,2,3,4), delimiter=',')

temp1= datos[:,0]
temp2= datos[:,1]
temp3= datos[:,2]
temp4= datos[:,3]

fig, temps= plt.subplots(4,1, sharex='all', sharey='all')
plt.xlabel('tiempo')
temps[0].plot(temp1, label='Temperatura 1')
temps[1].plot(temp2, label='Temperatura 2')
temps[2].plot(temp3, label='Temperatura 3')
temps[3].plot(temp4, label='Temperatura 4')

plt.legend(loc=0)
plt.suptitle("Temperaturas")
plt.savefig('temp.png')
plt.close()

#Centrar datos
c=0
while c<len(datos[0]):
	datos[:,c]= (datos[:,c]- np.mean(datos[:,c]))/np.std(datos[:,c])
	c+=1

MatrizDatos=[datos[:,0],datos[:,1],datos[:,2],datos[:,3]]

MatrizCov= np.cov(MatrizDatos)
print MatrizCov


#eigVal, eigVect = np.linalg.eig(MatrizCov)

#prop=[]
#for i in eigVal:
#	prop.append(i*100/sum(eigVal))
	
#proporcion = np.array(prop)

#Inteto de hacerlo sin ver los eigVals y su contribucion en la varianza
#numMayor1= eigVal[0]
#numMayor2= eigVal[1]
#for i in range(len(eigVal)):
#	if eigVal[i]> numMayor1:
#		numMayor1= eigVal[i]
#	while  	numMayor1!=numMayor2:
#		if eigVal[i]> numMayor2:
#			numMayor2=eigVal[i]

#print numMayor1, numMayor2






