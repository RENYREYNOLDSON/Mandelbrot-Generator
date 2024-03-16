import pygame,sys,random,time,math,colorsys
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Mandelbrot")
clock=pygame.time.Clock()

width=4
height=3

class Point:
    def __init__(self,x,y,colour):
        self.x=x
        self.y=y
        self.colour=colour
    def draw(self):
        screen.set_at((400-self.x,300-self.y),self.colour)

def drawPoints():
    for i in pointList:
        i.draw()


def checkPoint(c):
    z=0
    for i in range(200):
        z=z**2+c
        if math.sqrt(z.real**2+z.imag**2)>2:
            return i
    return None

def setup():
    for x in range(400):
        for y in range(300):
            realValue=-(width/800)*x
            imagValue=(height/600)*y
            value=complex(realValue,imagValue)
            number=checkPoint(value)
            if number==None:
                pointList.append(Point(x,y,(255,255,255)))
            else:
                r,g,b=colorsys.hsv_to_rgb(number/20,1,2)
                pointList.append(Point(x,y,(r*100,g*100,b*100)))
        for y in range(300):
            realValue=-(width/800)*x
            imagValue=-(height/600)*y
            value=complex(realValue,imagValue)
            number=checkPoint(value)
            if number==None:
                pointList.append(Point(x,-y,(255,255,255)))
            else:
                r,g,b=colorsys.hsv_to_rgb(number/20,1,2)
                pointList.append(Point(x,-y,(r*100,g*100,b*100)))
                
    for x in range(400):
        for y in range(300):
            realValue=(width/800)*x
            imagValue=(height/600)*y
            value=complex(realValue,imagValue)
            number=checkPoint(value)
            if number==None:
                pointList.append(Point(-x,y,(255,255,255)))
            else:
                r,g,b=colorsys.hsv_to_rgb(number/20,1,2)
                pointList.append(Point(-x,y,(r*100,g*100,b*100)))
        for y in range(400):
            realValue=(width/800)*x
            imagValue=-(height/600)*y
            value=complex(realValue,imagValue)
            number=checkPoint(value)
            if number==None:
                pointList.append(Point(-x,-y,(255,255,255)))
            else:
                r,g,b=colorsys.hsv_to_rgb(number/20,1,2)
                pointList.append(Point(-x,-y,(r*100,g*100,b*100)))

pointList=[]

setup()
print("setup completed")
print(len(pointList))
while True:
    screen.fill((0,0,0))

    drawPoints()


    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()






    pygame.display.update()
    clock.tick()
