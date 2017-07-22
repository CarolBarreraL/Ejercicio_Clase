import numpy as np

ma = [[2,3,6],[1,0,5],[1,2,0]]
matriz = np.array(ma)
print matriz


def linea(i):
	return matriz[i]/matriz[i][i]


def gaus():
	matriz[0]= linea(0)
	for i in range(len(matriz)):
		for j in range(len(matriz)):
			if i>j:	
				if matriz[i][j]!= 0:
					matriz[i]= matriz[i]- matriz[i][j]*linea(0)
			if i==j:
				if matriz[i][j]!= 0:
					matriz[i]= matriz[i]/matriz[i][j]
				else:
					matriz[i] = linea(0)/matriz[0][0]
							
						

	return matriz	
 
print gaus()	


b = [0,0,0]
vect= np.array(b)






