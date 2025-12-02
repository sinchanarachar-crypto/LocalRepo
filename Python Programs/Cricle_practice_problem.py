import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def Area(self,radius):
        self.area= math.pi*pow(self.radius,2)
        print("Area of circle=",self.area)
    
    def Perimeter(self,radius):
        self.perimeter=2*math.pi*self.radius
        print("Perimeter of circle=",self.perimeter)

a=float(input("Enter Radius: "))
C=Circle(a)
C.Area(a)
C.Perimeter(a)