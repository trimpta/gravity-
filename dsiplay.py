import pygame
from shjit import mass
from vectorshit import vector
from sys import exit
history = []

def historything(coords):
    history.append(coords)
    valuething = len(history) if len(history)<800 else 800
    ra='yellow'
    for i in history[-1:-valuething:-1]:
        pygame.draw.circle(screen,ra,i,1,0)
    
def mouse():
    return pygame.mouse.get_pos()        
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
def update():
    for i in all:
        i.update()
def updatee():
    for i in all:
        i.netforcegravity((all))
def blitz():
    
    for i in all:
        screen.blit(planet,i.displaypos())
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

h,w= 1920,1080
i = 32
all = []
run = True
default_mass = 10E8
ccol='White'
pygame.init()
pygame.display.set_caption('??')
screen = pygame.display.set_mode((h,w))
clock = pygame.time.Clock()
bg=pygame.image.load('init.jpg')
planet=pygame.image.load('planet.png')
font = pygame.font.SysFont('chalkduster.ttf', 40)
diffa=[]
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
            if ((mouse()[0]<320 and mouse()[0]>240 and mouse()[1]<940 and mouse()[1]>860)):
                if ((mouse()[0]<320 and mouse()[0]>240 and mouse()[1]<900 and mouse()[1]>860)):
                    default_mass*=10
                if ((mouse()[0]<320 and mouse()[0]>240 and mouse()[1]<940 and mouse()[1]>900)):
                    default_mass/=10
        if event.type == pygame.MOUSEBUTTONDOWN and not (mouse()[0]<320 and mouse()[0]>240 and mouse()[1]<940 and mouse()[1]>860):
            mousev = pygame.mouse.get_pos()
            all.append(mass(default_mass,vector(mousev[0]-h/2,mousev[1]-w/2,0)))
            history.clear()
        if event.type == pygame.MOUSEBUTTONUP and not (mouse()[0]<320 and mouse()[0]>240 and mouse()[1]<940 and mouse()[1]>860):
            initpos = vector(mousev[0],mousev[1],0)
            mofi = pygame.mouse.get_pos()
            finalpos = vector(mofi[0],mofi[1],0)
            scaledvel=finalpos-initpos
            all[-1].vel+=-scaledvel/20
            if diffa!=all:
                diffa.append(all[-1])
                print(all[-1])
        if mouse()[0]<320 and mouse()[0]>240 and mouse()[1]<940 and mouse()[1]>860:
            ccol = (22, 22, 22)
        else:
            ccol = 'White'
        if (event.type == pygame.KEYDOWN) :
            if  ((event.key == pygame.K_UP) or (event.key == pygame.K_DOWN)):
                pass
            else:
                all.clear()
                history.clear()
        
    
    
    screen.blit(bg,(0,0))
    lines()
    blitz()
    updatee()
    update()
    trails()
    greatest=greater=vector(0,0,0)
    for i in all:
        if i.vel>greatest:
            greatest=i.vel
    t1 = font.render(f"Max velocity:{round(abs(greatest),3)}", False, (152, 190, 212))
    t2 = font.render(f"Max velocity:= {greatest.rval}", False, (152, 190, 212))
    t3 = font.render(f"Object counter:{len(all)}", False, (152, 190, 212))
    t4 = font.render(f"Default mass:{default_mass}", False, (152, 190, 212))
    pygame.draw.circle(screen,ccol,(280,w-180),40)
    pygame.draw.line(screen,'gray40',(240,w-180),(320,w-180),2)
    screen.blit(t1,(230,115))
    screen.blit(t2,(230,145))
    screen.blit(t3,(230,205))
    screen.blit(t4,(230,175))
    pygame.display.update()
    clock.tick(60)