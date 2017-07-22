import numpy as np	
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

h=0.01
t_0=0.0
t_max=2.0
puntos= (t_max-t_0)/(h)
t = np.zeros(int(puntos))
y1= np.zeros(int(puntos))
y2= np.zeros(int(puntos))

def funcionderiv1(t,y1,y2):
	return y2

g=9.8
l=0.8
def funcionderiv2(t,y1,y2):
	return -(g/l)*np.sin(y1)

def deriv():
	#Condiciones iniciales
	t[0]= t_0
	y1[0]= np.pi/2
	y2[0]=0.0
	for i in range(1,int(puntos)):
		k1_y1= h*funcionderiv1(t[i-1],y1[i-1], y2[i-1])
		k1_y2= h*funcionderiv2(t[i-1],y1[i-1], y2[i-1])

		k2_y1= h*funcionderiv1(t[i-1]+0.5*h, y1[i-1]+0.5*k1_y1, y2[i-1]+0.5*k1_y2)
		k2_y2= h*funcionderiv2(t[i-1]+0.5*h, y1[i-1]+0.5*k1_y1, y2[i-1]+0.5*k1_y2)

		k3_y1= h*funcionderiv1(t[i-1]+0.5*h, y1[i-1]+0.5*k2_y1, y2[i-1]+0.5*k2_y2)
		k3_y2= h*funcionderiv2(t[i-1]+0.5*h, y1[i-1]+0.5*k2_y1, y2[i-1]+0.5*k2_y2)

		k4_y1= h*funcionderiv1(t[i-1]+h, y1[i-1]+k3_y1*h, y2[i-1]+k3_y2*h)
		k4_y2= h*funcionderiv2(t[i-1]+h, y1[i-1]+k3_y1*h, y2[i-1]+k3_y2*h)

		
		slope_y1= (1.0/6.0)*(k1_y1+2.0*k2_y1+2.0*k3_y1+k4_y1)
		slope_y2= (1.0/6.0)*(k1_y2+2.0*k2_y2+2.0*k3_y2+k4_y2)

		t[i]= t[i-1]+h
		y1[i]= y1[i-1] + h*slope_y1
		y2[i]= y2[i-1] + h*slope_y2
	return t,y1,y2

xx= l*np.cos(-deriv()[1])
yy= -l*np.sin(deriv()[1]) 

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([],[], '-o')
#ln = plt.plot(xx[0], yy[0], 'ro', animated=True)

#def init():
#	ln.set_data([],[])
#	return ln


def animate(i):
	enX=[0,xx[i]]
	enY=[0,yy[i]]
	ln.set_data(enX,enY)
	return ln,

ani = FuncAnimation(fig, animate, 25,len(xx), interval=50, blit=True)
plt.show()



