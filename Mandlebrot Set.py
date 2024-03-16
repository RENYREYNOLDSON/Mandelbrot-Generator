import pygame,sys,random,math
from pygame.locals import *
pygame.init()

screen=pygame.display.set_mode((1600,900))
pygame.display.set_caption("Mandelbrot Set")
clock=pygame.time.Clock()



width=4
height=2.25

class Point:
    def __init__(self,x,y,colour):
        self.x=int(x)
        self.y=int(y)
        self.colour=colour
    def draw(self):
        screen.set_at((800-self.x, 450-self.y), self.colour)


def checkValue(c):
    z=0
    for i in range(5):
        z=z**2+c
        if math.sqrt(z.real**2+z.imag**2)>2:
            return i
    return None


def setup():

    for x in range(800):
        for y in range(450):
            realValue=-(width/1600)*x###Top Left
            imagValue=(height/900)*y
            value=complex(realValue,imagValue)
            number=checkValue(value)
            if number==None:
                validPoints.append(Point(x,y,(0,0,0)))
            else:
                colour=(120-number,120-number,120-number)
                validPoints.append(Point(x,y,colour))
        for y in range(450):        ###Bottom Left
            realValue=-(width/1600)*x
            imagValue=-(height/900)*y
            value=complex(realValue,imagValue)
            number=checkValue(value)
            if number==None:
                validPoints.append(Point(x,-y,(0,0,0)))
            else:
                colour=(120-number,120-number,120-number)
                validPoints.append(Point(x,-y,colour))
                
    for x in range(800):
        for y in range(450):
            realValue=(width/1600)*x###Top Right
            imagValue=(height/900)*y
            value=complex(realValue,imagValue)
            number=checkValue(value)
            if number==None:
                validPoints.append(Point(-x,y,(0,0,0)))
            else:
                colour=(120-number,120-number,120-number)
                validPoints.append(Point(-x,y,colour))
        for y in range(450):        ###Bottom Right
            realValue=(width/1600)*x
            imagValue=-(height/900)*y
            value=complex(realValue,imagValue)
            number=checkValue(value)
            if number==None:
                validPoints.append(Point(-x,-y,(0,0,0)))
            else:
                colour=(120-number,120-number,120-number)
                validPoints.append(Point(-x,-y,colour))


    """
    for x in range(1600):
        for y in range(900):
            realValue=(width/1600)*x
            if x<800:
                realValue=-realValue
            imagValue=(height/900)*y
            if y>450:
                imagValue=-imagValue
            value=complex(realValue,imagValue)
            if checkValue(value)==True:
                validPoints.append(Point(x,y))
    """


def drawAxis():
    pygame.draw.line(screen,(0,0,0),(800,0),(800,900),4)
    pygame.draw.line(screen,(0,0,0),(0,450),(1600,450),4)


def drawPoints():
    for i in validPoints:
        i.draw()

validPoints=[]
setup()
while True:
    screen.fill((120,120,120))
    
    drawPoints()
    drawAxis()


    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()



    pygame.display.flip()
    clock.tick()
