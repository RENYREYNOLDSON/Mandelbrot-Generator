import pygame,sys,random,time,math,colorsys
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Mandelbrot")
clock=pygame.time.Clock()

font=pygame.font.Font('freesansbold.ttf', 50)
width=4
height=3

realPos=-0.1
imagPos=0.95

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
    for i in range(100):
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

pointList=[[]]




iteration=0
count=0
while True:
    screen.fill((0,0,0))
    pointList=[[]]
    setup()
    width=width*0.9
    height=height*0.9
    drawPoints()
    
    #text=font.render(str(width),True,(0,0,0))
    #screen.blit(text,(350,540))
    #pygame.draw.line(screen,(0,0,0),(10,585),(790,585),4)
    
    pygame.image.save(screen,"Mandelbrot_Images9/images/image"+str(count)+".png")
    count+=1
    #pygame.draw.rect(screen,(255,255,255),(400,300,2,2),0)

    if count==300:
        import cv2
        import os

        image_folder = 'Mandelbrot_Images9/images'
        video_name = 'video.avi'

        images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
        frame = cv2.imread(os.path.join(image_folder, images[0]))
        height, width, layers = frame.shape

        video = cv2.VideoWriter(video_name, 0, 1, (width,height))

        for image in images:
            video.write(cv2.imread(os.path.join(image_folder, image)))

        cv2.destroyAllWindows()
        video.release()


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
