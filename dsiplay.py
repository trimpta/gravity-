import pygame
from shjit import mass
from vectorshit import vector
from sys import exit
history = []
def historything(coords):
    history.append(coords)
    valuething = len(history) if len(history)<10000 else 10000
    r=g=b=0
    ra=ga=ba=1
    for i in history[-1:-valuething:-1]:
        pygame.draw.circle(screen,(r,g,b),i,1,0)
    r+=ra*5
    if r==255:
        ra=-1
    if r==0:
        ra=1
    
    g+=ga*5
    if g==255:
        ga=-1
    if g==0:
        ga=1
    
    b+=ba*5
    if b==255:
        ba=-1
    if b==0:
        ba=1
        

def trails():
    coordx,coordy=0,0
    for i in all:
        coordx+=i.displaypos()[0]
        coordy+=i.displaypos()[1]
    if len(all)==0:
        coordx,coordy=0,0
    else:
        coordx/=len(all)
        coordy/=len(all)
    historything((coordx,coordy))

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

bg=pygame.image.load('images/bg/init.jpg')
planet=pygame.image.load('images/planet.png')

all = []
font = pygame.font.SysFont('chalkduster.ttf', 40)

def lines():
    ci = 16
    for i in range(len(all)):
        for j in all[i::]:
            if all[i]!=j:
                idisp = all[i].displaypos()
                jdisp = j.displaypos()
                idis=(idisp[0]+ci,idisp[1]+ci)
                jdis=(jdisp[0]+ci,jdisp[1]+ci)
                
                pygame.draw.line(screen, (140, 146, 172),idis,jdis,width=1)
run = True
default_mass = 100000
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                default_mass/=10
            if event.key == pygame.K_UP:
                default_mass*=10E1
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousev = pygame.mouse.get_pos()
            all.append(mass(default_mass,vector(mousev[0]-h/2,mousev[1]-w/2,0)))
        if event.type == pygame.MOUSEBUTTONUP:
            initpos = vector(mousev[0],mousev[1],0)
            mofi = pygame.mouse.get_pos()
            finalpos = vector(mofi[0],mofi[1],0)
            scaledvel=finalpos-initpos
            all[-1].vel+=-scaledvel/5
        if (event.type == pygame.KEYDOWN) :
            if  ((event.key == pygame.K_UP) or (event.key == pygame.K_DOWN)):
                pass
            else:
                all.clear()
    if default_mass<0:
        default_mass=10

    screen.blit(bg,(0,0))
    lines()
    blitz()
    updatee()
    update()
    #trails()
    defm = font.render(f"Default mass:{default_mass}", False, (152, 190, 212))
    screen.blit(defm,(230,115))
    pygame.display.update()
    clock.tick(60)
