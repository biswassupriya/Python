# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 23:22:59 2019

@author: Supi
"""
class FilmDirector:
    """
    This is the class FilmDirector
    """
    def __init__(self):
        """
        this method is the function constructor
        """
        self.name = "not set"
        self.age = 0
        
    def setname(self,n):
            self.name = n
            
    def getname(self):
            return self.name
        
    def setage(self,a):
            self.age=a
            
    def getage(self):
            return self.age

class DvD:
    def __init__(self):
        self.title = "not set"
        self.director ="fimfirector class type"
        self.time = 0
        
    def settitle(self,t):
        self.title = t
        
    def  gettitle(self):
        return self.title
    
    def setdirector(self,d):
        self.director=d
        
    def getdirector(self):
        return self.director
    
    def settime(self,m):
        self.time = m
        
    def gettime(self):
        return self.time    
                
def test():
   s = FilmDirector()
   s.setname("Supriya")
   s.setage(35)
   print("the name of director:")
   print(s.getname())
   print("the age :")
   print(s.getage())   
         
       
       
        
        
    


