global h
global w
global i
h = 1920
w = 1080
i = 16
from vectorshit import vector
class mass:

    def __init__(self,mass,pos,vel=vector(0,0,0)):
        self.mass=mass
        self.pos=pos
        self.vel=vel
        self.G = 6.67430E-11
    

    def accelerate(self,force):
        acc=force/self.mass
        self.vel+=acc
    
    def update(self):
        self.pos=self.pos+self.vel

    def gravity(self,other):
        diff = self.pos-other.pos
        distance=diff.magnitude
        if distance!=0:
            c = -1*(self.G*self.mass*other.mass)/distance
            F = diff*c
            return F
        else:
            return vector(0,0,0)

    def netforcegravity(self,all):
        for i in all:
            if self != i:
                self.accelerate(self.gravity(i))
    def displaypos(self):
        return ((self.pos.i-i/2+h/2),(self.pos.j-i/2+w/2))
