import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq

n=128
f= 200.0
dt=1/(f*32)

def funcion(x):
	
	return np.cos(2*np.pi*x*f)

t= np.linspace(0,(n-1)*dt,n)
def transformada():
	GReal=0
	Gimg= 0
	rate=[]
	for valor in t:
		GReal+= funcion(t)*np.cos(2*np.pi*t*f)
		Gimg+= funcion(t)*np.sin(2*np.pi*t*f)
		rate.append(n/(t+1))
	return GReal, Gimg, rate


plt.plot(transformada()[0])
plt.show()
