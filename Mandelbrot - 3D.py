from mpl_toolkits import mplot3d

import math
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection="3d")
validPoints=[]

class Point:
    def __init__(self,x,z,i):
        self.x=x
        self.z=z
        self.i=i
    def draw(self):
        ax.scatter3D(self.x,self.z,self.i,cmap="hsv")


def checkValue(c):
    z=0
    for i in range(50):
        z=z**2+c
        if math.sqrt(z.real**2+z.imag**2)>0.1:
            return False
            print("False")
    return True

for x in range(10):
    for z in range(10):
        for i in range(10):
            realValue=math.sqrt(x**2+z**2)*0.01
            imagValue=i*0.01
            value=complex(realValue,imagValue)
            if checkValue(value)==True:
                validPoints.append(Point(x,z,i))

print("draw time")
for i in validPoints:
    i.draw()



print("show")
plt.show()
