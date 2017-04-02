#Importamos lo paquetes necesarios para resolver el problema
import numpy as np
import matplotlib.pyplot as plt
#Definimos la clase de planeta que se inicializa con un valor de masa, un vector de velocidad inicial y uno de posicion inicial
class planet:
	#Este es la funcion de iteracion de la clase.  
	def __init__(self,M,v0,r0):
		self.m = M
		self.v = v0
		self.r = r0
		self.rM = [r0]
		self.vM = [v0]
		self.aM = []
	#Esta funcion calcula el vector de posicion relativa normalizada entre un planeta y otro.
	def relative_norm(self,planet0):
		rel = planet0.r-self.r
		norm = np.linalg.norm(rel)
		return rel/norm
	#Esta funcion calcula la fuerza entre la iteracion de la clase y dos planetas mas que se introducen como parametro, y la guarda en la matriz de fuerza que se tiene como atributo.Ademas calcula la acelaracion y la guarda en la matriz de aceleracion.
	def getForce(self,planet1,planet2):
		pl1 = np.array([[0.],[0.]])
		pl2 = np.array([[0.],[0.]])
		if planet1!=0: pl1 = ((planet1.m*self.m)/(np.linalg.norm(planet1.r-self.r)**2))*self.relative_norm(planet1)
		if planet2!=0: pl2 = ((planet2.m*self.m)/(np.linalg.norm(planet2.r-self.r)**2))*self.relative_norm(planet2)
		self.aM.append((pl1+pl2)/self.m)
		return pl1+pl2


	#Esta funcion actualiza la posicion del planeta, recibe un inetrvalo de tiempo sobre el cual iterar y una posicion en la cual actuar
	def move(self, i, h):
		if (i==0):	
			self.v = h*self.aM[0]+self.v
			self.vM.append(self.v)
			self.r = h*self.vM[0]+self.r
			self.rM.append(self.r)
		if (i>=1):
			self.v = self.vM[i-1]+2*h*self.aM[i]
			self.vM.append(self.v)	
			self.r = self.rM[i-1]+2*h*self.vM[i]
			self.rM.append(self.r)
		return 0.


#Funcion que integra las ecuaciones de movimento de cada uno de los tres planetas que recibe como parametro.
def integrate(p1,p2,p3):
	h = 0.1
	tmax = 200.
	n_points = int(tmax/h)
	p1.getForce(p3,p2)
	p2.getForce(p1,p3)
	p3.getForce(p2,p1)
	for i in range(n_points-1):
		p1.move(i,h)
		p2.move(i,h)
		p3.move(i,h)
		p1.getForce(p3,p2)
		p2.getForce(p1,p3)
		p3.getForce(p2,p1)
	x1=[]
	x2=[]
	x3=[]
	y1=[]
	y2=[]
	y3=[]	
	for i in range(len(p1.rM)):
		x1.append(p1.rM[i][0][0])
		x2.append(p2.rM[i][0][0])		
		x3.append(p3.rM[i][0][0])
		y1.append(p1.rM[i][1][0])
		y2.append(p2.rM[i][1][0])
		y3.append(p3.rM[i][1][0])
	
	
	return [x1,y1,x2,y2,x3,y3]

def relative (xp,yp, xt, yt):
	xr =[]
	yr=[]
	for i in range(len(xp)):
		xr.append(xt[i]-xp[i])
		yr.append(yt[i]-yp[i])
	return [xr, yr]
	

	

x = 100*np.cos(np.pi/3)
y = 100*np.sin(np.pi/3)
vx = -3.23*np.cos(np.pi/6)
vy = 3.23*np.sin(np.pi/6)


star = planet(1047.,np.array([[0.],[0.]]),np.array([[0.],[0.]]))
planet1 = planet(1.,np.array([[0.],[3.23]]),np.array([[100.],[0.]]))
troyan = planet(0.005,np.array([[vx],[vy]]),np.array([[x],[y]]))
R1 = integrate(star,planet1,troyan)

star = planet(1047.,np.array([[0.],[0.]]),np.array([[0.],[0.]]))
planet1 = planet(1.,np.array([[0.],[3.23]]),np.array([[100.],[0.]]))
ptroyan = planet(0.005,np.array([[vx],[vy]]),np.array([[x+5.],[y+5.]]))
R2 = integrate(star,planet1,ptroyan)

star = planet(1047.,np.array([[0.],[0.]]),np.array([[0.],[0.]]))
planet2 = planet(10.,np.array([[0.],[3.23]]),np.array([[100.],[0.]]))
troyan = planet(0.005,np.array([[vx],[vy]]),np.array([[x],[y]]))
R3 = integrate(star,planet2,troyan)

star = planet(1047.,np.array([[0.],[0.]]),np.array([[0.],[0.]]))
planet3 = planet(20.,np.array([[0.],[3.23]]),np.array([[100.],[0.]]))
troyan = planet(0.005,np.array([[vx],[vy]]),np.array([[x],[y]]))
R4 = integrate(star,planet3,troyan)

star = planet(1047.,np.array([[0.],[0.]]),np.array([[0.],[0.]]))
planet4 = planet(30.,np.array([[0.],[3.23]]),np.array([[100.],[0.]]))
troyan = planet(0.005,np.array([[vx],[vy]]),np.array([[x],[y]]))
R5 = integrate(star,planet4,troyan)

star = planet(1047.,np.array([[0.],[0.]]),np.array([[0.],[0.]]))
planet5 = planet(40.,np.array([[0.],[3.23]]),np.array([[100.],[0.]]))
troyan = planet(0.005,np.array([[vx],[vy]]),np.array([[x],[y]]))
R6 = integrate(star,planet5,troyan)




f, (ax1, ax2, ax3) = plt.subplots(3, sharex = True)
ax1.grid(True)
ax1.set_title("Posicion de los cuerpos relativa al origen")
ax1.scatter(R1[0],R1[1],color='y',label='$m1=1047$')
ax1.legend(loc=0)
ax2.grid(True)
ax2.scatter(R1[2],R1[3],color='b',label='$m2=1.0$')
ax2.legend(loc=0)
ax3.grid(True)
ax3.scatter(R1[4],R1[5],color='g',label='$m3=0.005$')
ax3.legend(loc=0)
plt.savefig("OrbitsPLOT.pdf")
plt.close()

r1 = relative(R1[2],R1[3],R1[4],R1[5])
r2 = relative(R2[2],R2[3],R2[4],R2[5])
plt.grid(True)
plt.title("Posicion relativa del troyano")
plt.xlim(-150,150)
plt.ylim(-150,150)
plt.plot(r1[0],r1[1],label="Sin perturbacion")
plt.plot(r2[0],r2[1],label="Con perturbacion")
plt.savefig("Troyano.pdf")

f, (ax1, ax2, ax3, ax4) = plt.subplots(4, sharex = True)
ax1.grid(True)
ax1.set_title("Posicion del troyano con diferente masa del planeta")
ax1.scatter(R3[4],R3[5],color='y',label='$m2=10$',s=2)
ax1.legend(loc=0)
ax2.grid(True)
ax2.scatter(R4[4],R4[5],color='b',label='$m2=20$',s=2)
ax2.legend(loc=0)
ax3.grid(True)
ax3.scatter(R5[4],R5[5],color='g',label='$m2=20$',s=2)
ax3.legend(loc=0)
ax4.grid(True)
ax4.scatter(R6[4],R6[5],color='r',label='$m2=20$',s=2)
ax4.legend(loc=0)
plt.savefig("MassPLOT.pdf")
plt.close()






























