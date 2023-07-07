import pygame
from shjit import mass
from vectorshit import vector
from sys import exit
history = []
def historything(coords):
    history.append(coords)
    valuething = len(history) if len(history)<10000 else 10000
    for i in history[-1:-valuething:-1]:
        pygame.draw.circle(screen,'chocolate1',i,1,0)
h= 1920
w=1080
i = 32
def update():
    for i in all:
        i.update()
def updatee():
    for i in all:
        i.netforcegravity((all))
def blitz():
    for i in all:
        screen.blit(planet,i.displaypos())
pygame.init()
pygame.display.set_caption('??')
screen = pygame.display.set_mode((h,w))
clock = pygame.time.Clock()

bg=pygame.image.load('init.jpg')
planet=pygame.image.load('planet.png')

a = mass(1000000,vector(0,100,0),vector(0.1,0,0))
b = mass(1000000,vector(0,-100,0),vector(-0.1,0,0))
all = [a,b]
def lines():
    ci = 16
    for i in all:
        for j in all:
            if i!=j:
                idisp = i.displaypos()
                jdisp = j.displaypos()
                idis=(idisp[0]+ci,idisp[1]+ci)
                jdis=(jdisp[0]+ci,jdisp[1]+ci)
                
                pygame.draw.line(screen, (140, 146, 172),idis,jdis,width=1)
while True: 
    screen.blit(bg,(0,0))
    
    lines()
    blitz()
    updatee()
    update()
    
    pygame.display.update()
    clock.tick(60)
