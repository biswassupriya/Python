class Sphere:
     def __init__(self,radius):
            self.radius = radius
            
     def getRadius(self):
        return self.radius
            
     def setRadius(self,radius):
         self.radius = radius
    
     def surfaceArea(self):
         return 4 * 3.14 * self.radius * self.radius
     
     def volume(self):
         return 4 / 3 * 3.14 * self.radius * self.radius * self.radius
            
    

def test():
    s1 = Sphere(10)
    print("Radius of sphere is:{}".format(s1.getRadius()))
   # s1.getRadius()
    #s1.surfaceArea()
    print ("Surface Area of Sphere.{}".format(s1.surfaceArea()))
    print ("Volume of Sphere.{}".format(s1.volume()))
   

         