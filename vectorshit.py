class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
        self.magnitude=(i*i+j*j+k*k)**0.5
    def __repr__(self):
        return f"{self.i} {self.j} {self.k}"
    def __add__(self,other):
        return vector(self.i+other.i,self.j+other.j,self.k+other.k)
    def negative(self):
        return vector(-self.i,-self.j,-self.k)
    def __sub__(self,other):
        return self+other.negative()
    def dotproduct(self,other):
        return self.i*other.i+self.j*other.j+self.k*other.k
    def __mul__(self,other):
        if isinstance(other,vector):
            return vector(self.j*other.k-self.k*other.j,-1*(self.i*other.k-self.k*other.i),self.i*other.j-self.j*other.i)
        else:
            return vector(self.i*other,self.j*other,self.k*other)
    def unit(self):
        return vector(self.i/self.magnitude,self.j/self.magnitude,self.k/self.magnitude)
