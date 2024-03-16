import pygame,sys,random,math
from pygame.locals import *
pygame.init()

screen=pygame.display.set_mode((1600,900))
pygame.display.set_caption("Mandelbrot Set")
clock=pygame.time.Clock()



width=4
height=2.25
loop=0

class Point:
    def __init__(self,x,y,value,colour):
        self.x=int(x)
        self.y=int(y)
        self.colour=colour
        self.value=value
        self.z=0
    def draw(self):
        screen.set_at((800-self.x, 450-self.y), self.colour)

    def iterate(self):
        if self.colour==(255,255,255):
            self.z=self.z**2+self.value
            if math.sqrt(self.z.real**2+self.z.imag**2)>2:
                self.colour=(loop*5,loop*5,loop*5)

    




def setup():

    for x in range(800):
        for y in range(450):
            realValue=-(width/1600)*x###Top Left
            imagValue=(height/900)*y
            value=complex(realValue,imagValue)

            validPoints.append(Point(x,y,value,(255,255,255)))

        for y in range(450):        ###Bottom Left
            realValue=-(width/1600)*x
            imagValue=-(height/900)*y
            value=complex(realValue,imagValue)

            validPoints.append(Point(x,-y,value,(255,255,255)))
                
    for x in range(800):
        for y in range(450):
            realValue=(width/1600)*x###Top Right
            imagValue=(height/900)*y
            value=complex(realValue,imagValue)

            validPoints.append(Point(-x,y,value,(255,255,255)))
        for y in range(450):        ###Bottom Right
            realValue=(width/1600)*x
            imagValue=-(height/900)*y
            value=complex(realValue,imagValue)

            validPoints.append(Point(-x,-y,value,(255,255,255)))




def drawAxis():
    pygame.draw.line(screen,(0,0,0),(800,0),(800,900),4)
    pygame.draw.line(screen,(0,0,0),(0,450),(1600,450),4)


def drawPoints():
    for i in validPoints:
        i.draw()
        i.iterate()

validPoints=[]
setup()
while True:
    screen.fill((0,0,0))
    print("do")
    drawPoints()

    loop+=1



    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()



    pygame.display.flip()
    clock.tick()
