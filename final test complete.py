# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class FilmDirector():
    """ Class to represent a Film Director."""
    def __init__ (self):
       self.firstName = "Sample"
       self.age= 0
       
    def setFirstName(self, firstName):
         """Gets the name of FilmDirector"""
         self.firstName = firstName
 
    def setAge(self, age):
         """Sets the age of FilmDirector"""
         self.age = age
        
    def getFirstName(self):
         """Gets the name ofFilmDirector"""
         return self.firstName
 
    def getAge(self):
         """Gets the age ofFilmDirector"""
         return self.age

class DVD():
    """Class to represent a DVD."""
     
    def __init__ (self, director):
        assert type(director) is FilmDirector, 'director is not of FilmDirector type'
        self.title= "not set"
        self.running_time = 0
        self.director = director
        
    def setTitle(self, t):
        self.title = t
        
    def getRunningTime(self):
        return self.running_time
    
    def getTitle(self):
       return self.title
    
    def setRunningTime(self, r):
        self.running_time = r
        
    def getDirector(self):
        return self.director
    
    def setDirector(self, director):
        self.director = director
    
    def printDVDdetails(self):
        print ("Title is: " + self.title)
        print ("Running time is: {} min".format(self.running_time))
        print("Director name: " + self.director.getFirstName())
         
    def __str__(self):
        return('The title is {}. The running time is {}. The director name is {}').format(self.title,self.running_time, self.director.getFirstName())
         
         
class MydvdColection():
     """
     Class to represent a colection of DVDs.
     """
    def __init__ (self):
         
        self.nameOfColection= "not set"
        self.DVDColectionlist= []
        
    def setNameOfColection(self,nameOfColection):
         self.nameOfColection= nameOfColection
     
    def setDVDColectionlist(self,DVDlist):
         self.DVDColectionlist= DVDlist
        
    def getNameOfColection(self):
         return self.nameOfColection
     
    def getDVDColectionlist(self):
         return self.DVDColectionlist
    def addDVD(self, dvd):
         if (dvd in self.DVDColectionlist):
             print("This DVD is already in yuour colection")
         else:
             self.DVDColectionlist.append(dvd)
             print("This DVD added successfully to your collection")
         
         
    def printMyDVDColectionDetails(self):
         """ 
         Prints if the DVD Colection details.
         """
         print ("DVD Collection name: " + self.nameOfColection )
         for dvd in self.DVDColectionlist:
             dvd.printDVDdetails()
    
             
             
    def emptyDVDColection(self):
         """ 
         Prints if the DVD Colection is empty or not.
         """
         if (len(self.DVDColectionlist))==0:
             print("DVD collection is empty!")
         else:
             print("DVD collection is not empty!")
    
    def directorDVD (self, director):
         for dvd in self.DVDColectionlist:
             if dvd.getDirector().getFirstName()== director:
                 dvd.printDVDdetails()

         
def test_2():
    
    filmDirector1 = FilmDirector()
    filmDirector1.setFirstName("Steven Spielberg")
    filmDirector1.setAge(50)
    
    filmDirector2 = FilmDirector()
    filmDirector2.setFirstName("Alfred Hitchcock")
    filmDirector2.setAge(50)
    
    dvd1 = DVD(filmDirector2)
    dvd1.setTitle("Titanic")
    dvd1.setRunningTime(72)
    
    dvd2 = DVD(filmDirector2)
    dvd2.setTitle("Murder! ")
    dvd2.setRunningTime(72)
       
    dvd3 = DVD(filmDirector1)
    dvd3.setTitle("Jurasic Park")
    dvd3.setRunningTime(72)
    
    dvd4 = DVD(filmDirector1)
    dvd4.setTitle("Titanic 2")
    dvd4.setRunningTime(72)
    
    colection_1 = MydvdColection()
    colection_1.setNameOfColection("Thomas Collection")
    
    colection_1.addDVD(dvd1)
    colection_1.addDVD(dvd2)
    colection_1.addDVD(dvd3)
    colection_1.addDVD(dvd4)
    colection_1.addDVD(dvd4)

    colection_1.printMyDVDColectionDetails()
    colection_1.emptyDVDColection()
    print("colection: ", colection_1.getNameOfColection())
    

    """Implement a	method	in	the	MyDVDCollection class	that	takes	a	DVD object	as
        a	parameter	and	works	according	to	the	following	specification:
If	the list already contains	the	parameter DVD object,	the	method	should	discard the	
parameter	and print the	message	 “This	DVD	is	 already	in	your	 collection!” on	 the	
screen.	Otherwise,	the	method	should	add	the	parameter	DVD object at	the	end	of	
the	list and print the	message	“DVD	added	successfully	to	your	collection!” on	the	
screen."""

def test_task4():
    filmDirector1 = FilmDirector()
    filmDirector1.setFirstName("Steven Spielberg")
    filmDirector1.setAge(50)
    
    filmDirector2 = FilmDirector()
    filmDirector2.setFirstName("Alfred Hitchcock")
    filmDirector2.setAge(50)
    
    dvd1 = DVD(filmDirector2)
    dvd1.setTitle("Titanic")
    dvd1.setRunningTime(72)
    
    dvd2 = DVD(filmDirector2)
    dvd2.setTitle("Murder! ")
    dvd2.setRunningTime(72)
       
    dvd3 = DVD(filmDirector1)
    dvd3.setTitle("Jurasic Park")
    dvd3.setRunningTime(72)
    
    colection_1 = MydvdColection()
    colection_1.setNameOfColection("Catalin DVD Collection")
    
    colection_1.addDVD(dvd1)
    colection_1.addDVD(dvd2)
    colection_1.addDVD(dvd3)
    colection_1.addDVD(dvd3)
    
        
"""Implement a	method	in	the	MyDVDCollection class	that	takes	no	parameters
and	works	according	to	the	following	specification:
The method	prints the	message	“DVD	collection	is	empty!” on	the	screen if	the	list is	
empty.	 Otherwise,	 it	 prints the	 message	 “DVD	 collection	 is	 not	 empty!” on	 the	
screen."""
def test_task5():
    filmDirector1 = FilmDirector()
    filmDirector1.setFirstName("Steven Spielberg")
    filmDirector1.setAge(50)
    
    dvd1 = DVD(filmDirector1)
    dvd1.setTitle("Titanic")
    dvd1.setRunningTime(72)
  
    colection_1 = MydvdColection()
    colection_1.setNameOfColection("Catalin DVD Collection")
    
    colection_1.emptyDVDColection()
    
    colection_1.addDVD(dvd1)

    colection_1.emptyDVDColection()
    
    
    """" Implement a	 method	 in	 the	MyDVDCollection class	 that	 takes	 a string as	 a	
parameter (the	director’s	name) and	works	according	to	the	following	specification:
The	 method prints on	 the	 screen	 the	 details	 of	 ALL DVD objects	 directed	 by	 the	
director with	the	specified	name."""
def test_task6():
    
    filmDirector1 = FilmDirector()
    filmDirector1.setFirstName("Steven Spielberg")
    filmDirector1.setAge(50)
    
    filmDirector2 = FilmDirector()
    filmDirector2.setFirstName("Alfred Hitchcock")
    filmDirector2.setAge(50)
    
    dvd1 = DVD(filmDirector2)
    dvd1.setTitle("Titanic")
    dvd1.setRunningTime(72)
    
    dvd2 = DVD(filmDirector2)
    dvd2.setTitle("Murder! ")
    dvd2.setRunningTime(72)
       
    dvd3 = DVD(filmDirector1)
    dvd3.setTitle("Jurasic Park")
    dvd3.setRunningTime(72)
    
    colection_1 = MydvdColection()
    colection_1.setNameOfColection("Catalin Collection")
    dvd_list1 = [dvd1, dvd2, dvd3]
    colection_1.setDVDColectionlist(dvd_list1)

    colection_1.directorDVD("Steven Spielberg")




    


  
        