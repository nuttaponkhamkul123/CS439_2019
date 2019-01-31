import math
class Isosceles(object):
    def __init__(self , w=0 ,h=0):
       self.w = w
       self.h = h
    def perimeter(self):
        param = ((self.w/2)**2)+((self.h)**2)
        return math.sqrt(param)
    def __str__(self):
        #print(f'Perimeter function : {self.perimeter()}' );
        return (f'สามเหลี่ยมหน้าจั่ว : {((self.perimeter()*2)+self.w)}')
class Equilateral(Isosceles):
    def __init__(self , w=0):
       self.w = w
    def perimeter(self):
        return self.w*3
    def __str__(self):
        return (f'สามเหลี่ยมหน้าด้านเท่า : {self.perimeter()}')
    
    
