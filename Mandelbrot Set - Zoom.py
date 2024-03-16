import pygame,sys,random,time,math,colorsys
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Mandelbrot")
clock=pygame.time.Clock()

width=4
height=3

realPos=-1.6
imagPos=0

iteration=0

class Point:
    def __init__(self,x,y,colour):
        self.x=x
        self.y=y
        self.colour=colour
    def draw(self):
        screen.set_at((400-self.x,300-self.y),self.colour)

def drawPoints():
    for i in pointList[iteration]:
        i.draw()


def checkPoint(c):
    z=0
    for i in range(40):
        z=z**2+c
        if math.sqrt(z.real**2+z.imag**2)>2:
            return i
    return None

def setup():
    for x in range(400):
        for y in range(300):
            realValue=-(width/800)*x+realPos
            imagValue=(height/600)*y+imagPos
            value=complex(realValue,imagValue)
            number=checkPoint(value)
            if number==None:
                pointList[iteration].append(Point(x,y,(0,0,0)))
            else:
                r,g,b=colorsys.hsv_to_rgb(number/20,1,2)
                pointList[iteration].append(Point(x,y,(r*100,g*100,b*100)))
        for y in range(300):
            realValue=-(width/800)*x+realPos
            imagValue=-(height/600)*y+imagPos
            value=complex(realValue,imagValue)
            number=checkPoint(value)
            if number==None:
                pointList[iteration].append(Point(x,-y,(0,0,0)))
            else:
                r,g,b=colorsys.hsv_to_rgb(number/20,1,2)
                pointList[iteration].append(Point(x,-y,(r*100,g*100,b*100)))
                
    for x in range(400):
        for y in range(300):
            realValue=(width/800)*x+realPos
            imagValue=(height/600)*y+imagPos
            value=complex(realValue,imagValue)
            number=checkPoint(value)
            if number==None:
                pointList[iteration].append(Point(-x,y,(0,0,0)))
            else:
                r,g,b=colorsys.hsv_to_rgb(number/20,1,2)
                pointList[iteration].append(Point(-x,y,(r*100,g*100,b*100)))
        for y in range(400):
            realValue=(width/800)*x+realPos
            imagValue=-(height/600)*y+imagPos
            value=complex(realValue,imagValue)
            number=checkPoint(value)
            if number==None:
                pointList[iteration].append(Point(-x,-y,(0,0,0)))
            else:
                r,g,b=colorsys.hsv_to_rgb(number/20,1,2)
                pointList[iteration].append(Point(-x,-y,(r*100,g*100,b*100)))
zooms=5

pointList=[]
for i in range(zooms):
    pointList.append([])

for i in range(zooms):
    setup()
    width=width/2
    height=height/2
    iteration+=1
print("setup done")
iteration=0
while True:
    screen.fill((0,0,0))

    drawPoints()

    


    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==KEYDOWN:
            if event.key==K_a and iteration<zooms-1:
                iteration+=1
            elif event.key==K_s and iteration>0:
                iteration-=1





    pygame.display.update()
    clock.tick()
