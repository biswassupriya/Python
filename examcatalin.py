# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class FilmDirector:
     """
     Class to represent a Film Director.
     """
     def __init__ (self,):
       self.firstName = "not set"
       self.age= 0
            
     def getFirstName(self):
        return self.firstName
 
     def setFirstName(self, firstName):
        self.firstName = firstName
        
class DVD():
     def __init__ (self, director):
        self.title= "not set"
        self.director = director
        self.running_time = 0

        
     def getTitle(self):
       return self.title
 
     def setTitle(self, title):
        self.title = title
       
     def setRunningTime(self, t):
        self.running_time = t
        
     def getRunningTime(self, t):
        return self.running_time
    
     def printDVDdetails(self):
         print ("Title is: " + self.title)
         print ("Running time is: " + str(self.running_time))
         print("Director name: " + self.director.getFirstName())
        
def test_2():
    rer1 = FilmDirector()
    m = DVD(rer1)
    m.printDVDdetails()


  
        