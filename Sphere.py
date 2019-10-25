# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 00:46:24 2019

@author: Supi
"""

class Sphere:
    def __init__(self,radius):
        self.radius = radius
        
    def getradius(self):
      return self.radius
    
    def setradius():
        self.radius = radius
        
    def surfacearea(self):
        return 4*3.14*self.radius*self.radius
    
    def volume(self):
        return 4/3*3.14*self.radius*self.radius*self.radius
    
def test():
    s1 = Sphere(10)
    print("The radius of Sphere:{}".format(s1.getradius()))
    s1.surfacearea()
    print("The surface area of sphere:{}".format(s1.surfacearea()))
    s1.volume()
    print("The volume of the sphere:{}".format(s1.volume()))