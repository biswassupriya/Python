# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# this is the class of FilmDirector 
class FilmDirector:
   # Filmdirector class constructor/initializer
    def __init__(self):
#        data fields for the FilmDirector class 
        self.name = "not set"
        self.age = 0
        
        # methods function on the datafields
    def setname(self,n):
        self.name = n
        
    def getname(self):
        return self.name
    
    def setage(self, a):
        self.age  = a
        
    def getage(self):
        return self.age
    
class Dvd:
     def __init__(self):
        self.title = "not set"
        self.director = "should be FilmDirector class type"
        self.time = 0
     
     def setTitle(self,t):
         self.title = t
     
     def getTitle(self):
        return self.title
    
     def setdirector(self,d):
        self.director = d
        
     def getdirector(self):
        return self.director
    
     def setTime(self,s):
        self.time = s
        
     def getTime(self):
        return self.time
    
     def printDvDDetails(self):
        print("Titile: " + self.title)
        print("Director: " +self.director.getname())
        print("Time: "+self.time)
        
        
    
    
    
    
    
    
#test function
def test():
    s1 = FilmDirector()
    s1.setname("Thomas")
    s1.setage(30)
    d1 = Dvd()
    d1.setTitle("Supriya")
#    s2 = FilmDirector()
    print("DvD Title is: ", d1.getTitle(), "The name of the Director is:", s1.getname(), "and his age is ", s1.getage())
    
#def test1():
#   d1 = Dvd()
#   d1.setTitle("Biswas")
#   print("Title: ", d1.getTitle())
     
            
    
    
             
     
    