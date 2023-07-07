import pygame
from shjit import mass
from vectorshit import vector
from sys import exit
a = mass(10000000,vector(-100,10,0),vector(0,0,0))
b = mass(10000000,vector(-100,5000,0),vector(0,0,0))



pygame.init()
screen = pygame.display.set_mode((1920,1080))
pygame.display.set_caption('SEX')
clock = pygame.time.Clock()
font = pygame.font.Font('images/Pixeltype.ttf', 100)
sky=pygame.image.load('images/bg/init.jpg')
textsurface=font.render('Welcome', False , 'White')
planet=pygame.image.load('images/planet.png')
planet2=pygame.image.load('images/planet.png')

while True:  
    xa,ya=a.pos.i,a.pos.j
    xb,yb=b.pos.i,b.pos.j
    
    a.accelerate(a.einstiennnewotngravityshitthing(b))
    a.update()
    b.accelerate(b.einstiennnewotngravityshitthing(a))
    b.update()
    screen.blit(sky,(0,0))
    screen.blit(planet,(xa+1980/2,ya+1080/2))
    screen.blit(planet2,(xb+1980/2,yb+1080/2))
    #screen.blit(textsurface,(300,300))
    print(xa,ya,"\n",xb,yb)
    pygame.display.update()
    clock.tick(60)

  