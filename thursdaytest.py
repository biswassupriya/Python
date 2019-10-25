# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class FilmDirector():
     """
     Class to represent a Film Director.
     """
     def __init__ (self):
       self.firstName = "Sample"
       self.age= 0
            
     def getFirstName(self):
        return self.firstName
 
     def setFirstName(self, firstName):
        self.firstName = firstName
        
     def getAge(self):
        return self.age
 
     def setAge(self, age):
        self.age = age
        
class DVD():
     def __init__ (self, director):
        self.title= "not set"
        self.director = director
        self.running_time = 0

        
     def getTitle(self):
       return self.title
 
     def setTitle(self, t):
        self.title = t
       
     def setRunningTime(self, r):
        self.running_time = r
        
     def getRunningTime(self, r):
        return self.running_time
    
     def printDVDdetails(self):
         print ("Title is: " + self.title)
         print ("Running time is: {} min".format(self.running_time))
         print("Director name: " + self.director.getFirstName())
         
         

class MydvdColection():
     def __init__ (self):
        self.nameOfColection= "not set"
        self.MyDVDColection= []
        
     def getNameOfColection(self):
         return self.nameOfColection
     
     def setNameOfColection(self,nameOfColection):
         self.nameOfColection= nameOfColection
         
     def addDVD(self, d):
         if (d in self.MyDVDColection):
             print("This DVD is already in yuour colection")
             
         else:
             self.MyDVDColection.append(d)
             print("This DVD added successfully to your collection")
         
         
     def printMyDVDColectionDetails(self):
         print ("DVD Collection name: " + self.nameOfColection )
         print("\n")
         for d in self.MyDVDColection:
             d.printDVDdetails()
             print("\n")
             
         

         
def test_2():
    rer1 = FilmDirector()
    rer1.setFirstName("Steven Spielberg")
    rer1.setAge(50)
    
    
    m = DVD(rer1)
    m.setTitle("Titanic")
    m.setRunningTime(72)
    

    c = DVD(rer1)
    c.setTitle("Titanic")
    c.setRunningTime(72)
    
    
    rer2 = FilmDirector()
    rer2.setFirstName("Steven Spielberg")
    rer2.setAge(50)
    
    m1 = DVD(rer2)
    m1.setTitle("Titanic")
    m1.setRunningTime(72)
    

    c1 = DVD(rer2)
    c1.setTitle("Titanic1")
    c1.setRunningTime(72)
    
    obj_dvdC = MydvdColection()
    obj_dvdC.setNameOfColection("Thomas Collection")
    
    obj_dvdC.addDVD(m)
    obj_dvdC.addDVD(c)
    obj_dvdC.addDVD(m1)
    obj_dvdC.addDVD(c1)

    obj_dvdC.printMyDVDColectionDetails()
    
    

    


  
        