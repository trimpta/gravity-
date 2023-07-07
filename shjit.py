from vectorshit import vector
class mass:
    def __init__(self,mass,pos,vel=vector(0,0,0)):
        self.mass=mass
        self.pos=pos
        self.vel=vel
        self.tpos = (self.pos.i,self.pos.j)
        self.G = 6.67430E-11
    def accelerate(self,force):
        acc=force*(1/self.mass)
        self.vel+=acc
    def update(self):
        self.pos+=self.vel
    def einstiennnewotngravityshitthing(self,other):
        diff = self.pos-other.pos
        distance=diff.magnitude
        c = -1*(self.G*self.mass*other.mass)/distance
        F = diff*c
        return F

