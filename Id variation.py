import math
import matplotlib.pyplot as plt
import numpy as np

Eox = (3.9 * 8.854 * (math.pow(10,-14)))
Tox = 1*math.pow(10,-9)
Mun = 13510*math.pow(10, -6)
W = 1.5
l = 0.6
#W = float(input("Enter the ’L’(In micro meters): ")) #1.5
#l = float(input("Enter the ’W’(In micro meters): ")) #0.6
#Vg = float(input("Enter voltage applied to gate: "))
#Vd = float(input("Enter voltage applied to drain: "))
Vth = 0.5
Cox = Eox/Tox

def DrainCurrent(Vds, Vgs):

    #if(Vgs<Vth):
       # id = 0
    #elif((Vds > (Vgs-Vth)).any()):
        #id= .5 * Mun * Cox * (W/l) * (Vgs-Vth)**2
    #elif((Vds < (Vgs-Vth)).any()):
    id= Mun * Cox * (W/l) * (((Vgs-Vth)*Vds)-(.5*(Vds**2)))
    #id = .5 * Mun * Cox * (W / l) * ((Vgs - Vth) * Vds)
    return id;

Vds1 = np.arange(0.0, 1.5, 0.15)
#Vds1 = np.arange(1.8, 2, 0.05)
#plt.plot(Vds1, DrainCurrent(Vds1, 1.25))
plt.plot(Vds1, DrainCurrent(Vds1, 1.5))
plt.plot(Vds1, DrainCurrent(Vds1, 1.75))
plt.plot(Vds1, DrainCurrent(Vds1, 2))
plt.plot(Vds1, DrainCurrent(Vds1, 2.25))
plt.xlabel("Vds (V)")
plt.ylabel("Id (A)")
plt.title("I V Characterisics of MOSFET")
plt.text(1, 4.7e-06, "Vgs = 1.5")
plt.text(1, 7.4e-06, "Vgs = 1.75")
plt.text(1, 1.04e-05, "Vgs = 2")
plt.text(1, 1.4e-05, "Vgs = 2.25")
plt.grid(True)
plt.show()

