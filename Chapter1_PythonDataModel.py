from math import hypot

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)
    
    def __str__(self): # if __str__ is not defined, __repr__ will be used as fallback
        return 'str_Vector(%r, %r)' % (self.x, self.y)
    
    def __getitem__(self, key):
        return (self.x, self.y)[key]
    
    def __len__(self):
        return len((self.x, self.y))
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar):
        return self * scalar # this will call __mul__ and pass the scalar as the argument
    

a = Vector(2, 4)
print(a)
print(a[0])
print(len(a))

scalar = 3
print(a * scalar) # this will call __mul__ and pass the scalar as the argument
print(scalar * a) # this will call __rmul__




    
