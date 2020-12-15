#Carlos Yolatl Joshua Montero Cortez 
#N° 18390044
#Grupo I5U
import numpy as np
import matplotlib.pyplot as plt

plt.axis([-70, 70, -70, 70])
plt.axis('on')
plt.grid('on')
#Funcion de rotación
def rotRz(xp,yp,rz):
    Crz11 = np.cos(rz)
    Crz12 = -np.sin(rz)
    Crz21 = np.sin(rz)
    Crz22 = np.cos(rz)
    xpp = xp*Crz11+yp*Crz12
    ypp = xp*Crz21+yp-Crz22
    xg = xc + xpp
    yg = yc + ypp
    return (xg,yg)

#Creacion de variables
c = (.0,.4,.4)
p1=0*np.pi/180
p2=360*np.pi/180
dp=(p2-p1)/100
xc = 0
yc = 0
#Radio
r=4*5
#Creacion del circulo
xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)

for p in np.arange(p1,p2+dp,dp):
    xp=xc+r*np.cos(p)
    yp=xc+r*np.sin(p)
    plt.plot([xlast,xp],[ylast,yp],color=c, linewidth=1)
    xlast=xp
    ylast=yp

#Valores del Escalado
sx= 4/5
sy= 4/5    


#primer rectangulo
xp1=0 *sx
xp2=-40 *sx
xp3=-40 * sx
xp4=0 * sx
yp1=-30  *sy
yp2=-30 *sy
yp3=0 *sy
yp4=0 *sy
#plot
xg1 = xc + xp1
yg1 = yc + yp1
xg2 = xc + xp2
yg2 = yc + yp2
xg3 = xc + xp3
yg3 = yc + yp3
xg4 = xc + xp4
yg4 = yc + yp4


xg = [xg1,xg2,xg3,xg4,xg1]
yg = [yg1,yg2,yg3,yg4,yg1]
#plt.plot(xg,yg,color=c) #Original

#__________proceso y ploteo 
rz=(4*6)*np.pi/180
#--------rotar el punto 1
xp=xp1
yp=yp1
[xg1,yg1]=rotRz(xp,yp,rz)
#--------rotar el punto 2
xp=xp2
yp=yp2
[xg2,yg2]=rotRz(xp,yp,rz)
#--------rotar el punto 3
xp=xp3
yp=yp3
[xg3,yg3]=rotRz(xp,yp,rz)
#--------rotar el punto 4
xp=xp4
yp=yp4
[xg4,yg4]=rotRz(xp,yp,rz)

#-----plotear el rectangulo rotado
xg=[xg1,xg2,xg3,xg4,xg1]
yg=[yg1,yg2,yg3,yg4,yg1]
plt.plot(xg,yg,color=c) #Original


#segundo rectangulo
xc = 20
yc = 15

xp1=0 
xp2=-40 
xp3=-40 
xp4=0 

yp1=-30 
yp2=-30 
yp3=0 
yp4=0 

#plot
xg1 = xc + xp1
yg1 = yc + yp1
xg2 = xc + xp2
yg2 = yc + yp2
xg3 = xc + xp3
yg3 = yc + yp3
xg4 = xc + xp4
yg4 = yc + yp4


xg = [xg1,xg2,xg3,xg4,xg1]
yg = [yg1,yg2,yg3,yg4,yg1]
plt.plot(xg,yg,color=c) #original


plt.show()