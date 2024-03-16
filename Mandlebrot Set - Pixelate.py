import pygame,sys,random,math
from pygame.locals import *
pygame.init()

screen=pygame.display.set_mode((1600,900))
pygame.display.set_caption("Mandelbrot Set")
clock=pygame.time.Clock()



width=4
height=2.25

pixels=0.01

class Point:
    def __init__(self,x,y,colour):
        self.x=int(x)
        self.y=int(y)
        self.colour=colour
    def draw(self):
        pygame.draw.rect(screen,self.colour,(800-self.x,450-self.y,1/pixels,1/pixels),0)
        #screen.set_at((800-self.x, 450-self.y), self.colour)


def checkValue(c):
    z=0
    for i in range(100):
        z=z**2+c
        if math.sqrt(z.real**2+z.imag**2)>2:
            return i
    return None


def setup():

    for x in range(int(800*pixels)):
        for y in range(int(450*pixels)):
            realValue=-(width/(1600*pixels))*x###Top Left
            imagValue=(height/(900*pixels))*y
            value=complex(realValue,imagValue)
            number=checkValue(value)
            if number==None:
                validPoints.append(Point(x/pixels,y/pixels,(0,0,0)))
            else:
                colour=(120-number,120-number,120-number)
                validPoints.append(Point(x/pixels,y/pixels,colour))
        for y in range(int(450*pixels)):        ###Bottom Left
            realValue=-(width/(1600*pixels))*x
            imagValue=-(height/(900*pixels))*y
            value=complex(realValue,imagValue)
            number=checkValue(value)
            if number==None:
                validPoints.append(Point(x/pixels,-y/pixels,(0,0,0)))
            else:
                colour=(120-number,120-number,120-number)
                validPoints.append(Point(x/pixels,-y/pixels,colour))
                
    for x in range(int(800*pixels)):
        for y in range(int(450*pixels)):
            realValue=(width/(1600*pixels))*x###Top Right
            imagValue=(height/(900*pixels))*y
            value=complex(realValue,imagValue)
            number=checkValue(value)
            if number==None:
                validPoints.append(Point(-x/pixels,y/pixels,(0,0,0)))
            else:
                colour=(120-number,120-number,120-number)
                validPoints.append(Point(-x/pixels,y/pixels,colour))
        for y in range(int(450*pixels)):        ###Bottom Right
            realValue=(width/(1600*pixels))*x
            imagValue=-(height/(900*pixels))*y
            value=complex(realValue,imagValue)
            number=checkValue(value)
            if number==None:
                validPoints.append(Point(-x/pixels,-y/pixels,(0,0,0)))
            else:
                colour=(120-number,120-number,120-number)
                validPoints.append(Point(-x/pixels,-y/pixels,colour))



def drawAxis():
    pygame.draw.line(screen,(0,0,0),(800,0),(800,900),4)
    pygame.draw.line(screen,(0,0,0),(0,450),(1600,450),4)


def drawPoints():
    for i in validPoints:
        i.draw()

validPoints=[]
#setup()
while True:
    screen.fill((120,120,120))
    setup()
    drawPoints()
    drawAxis()
    pixels+=0.001


    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()



    pygame.display.flip()
    clock.tick()
