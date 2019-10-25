# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 10:11:35 2019

@author: Supi
"""

class Cube:
    def __init__(self,length):
        self.length = length
       
    def getLength(self):
       return self.length
        
    def setLength(self,area):
        self.length = length
        
    def surfaceArea(self):
        return 6*self.length*self.length
    
    def volume(self):
        return self.length * self.length * self.length

def test1():
     s1 = Cube(20)
     print("The volume of cube is :{}".format(s1.getLength()))
     print("The surfacearea of cube is :{}".format(s1.surfaceArea()))
     print("The volume of cube is :{}".format(s1.volume()))
        
        
        
        