import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, ifft
from scipy.io import wavfile as wav

N=1000 #Numero de puntos en el intervalo
Nf=float(N)
f= 44100.0 #Frecuencia
dt=1/(f*32) #32 muestras por unidad de frecuencia
t= np.linspace(0,(N-1)*dt,N)

y = np.cos(2 * np.pi * f * t) - 0.4 * np.sin(2 * np.pi * (2*f) * t )



fft_pack = fft(y)
freq = fftfreq(N, dt)
#plt.plot(t,funcion(t))
#plt.show()
def transformada():
	n=0
	rate=[]
	trans=[]
	while n<N:
		tr=0
		rate.append(n/Nf)
		k=0
		while k<N:
			tr+= y[k]*np.exp(-1j*2.0*np.pi*k*(n/Nf))
			k+=1
		trans.append(tr)
		n+=1	
	transform = np.array(trans)
	return transform , rate

transformadaMia = transformada()[0]
#print transPaquete
plt.plot(freq, transformadaMia)
plt.plot(freq, fft_pack, 'k')
plt.show()


wav.write('Pueva.wav', f, y)

