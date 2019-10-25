# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 18:02:18 2019

@author: Thomas
"""

class FilmDirector():
    """
    A class  that represents the film director

    """
    def __init__(self):
        self.name = "not set"
        self.age  = 0
        self.nationality = "not set"
        
    def setdirectorName(self,n):
        self.name = n       
        """
        sets the name of the filem director
    
        """
        
    def getdirectorName(self):
        return self.name
        """
        returns the name of the filem director
    
        """
    
    def setdirectorAge(self, a):
        self.age = a
        """
        sets the age of the filem director
    
        """
    
    def getdirectorAge(self):
        return self.age
        """
        returns the age of the filem director
    
        """
    def setnationality(self, n):
        self.nationality = n
        
    def getnationality(self):
        return self.nationality
    
    
class DVD():   
    """
    A class  that represents DVD

    """
    
    def __init__(self, director):
        self.title = "not set"
        self.director  = director
        self.runningTime = 0
        self.genre = "not set"
        self.country = "not set"
        
    def settitle(self, t):
        self.title = t        
        """
        sets the title of the DVD
    
        """
        
    def gettitle(self):
        return self.title
        """
        returns the title of the DVD
    
        """
    
    def setrunningTime(self, r):
        self.runningTime = r
        """
        sets the length the DVD
    
        """
    
    def getRunningTime(self):
        self.running_time
        """
        returns the length the DVD
    
        """
    
    def setdvdgenre(self, g):
        self.genre = g
    
    def getdvdgenre(self):
        return self.genre
    
    def setdvdcountry(self, c):
        self.country = c
        
    def getdvdcountry(self):
        return self.country
    
        
    def printDVDdetails(self):
        """
        prints on the screen details of a DVD 
    
        """
    
        print("Title of DVD: " + self.title)
        print("The DVD length: {} mins".format(self.runningTime))
        print("DVD genere: " + self.genre)
        print("DVD Country: " + self.country)
        print("Film Director: " + self.director.getdirectorName())
        print("Film Director age: " + format(self.director.getdirectorAge()))
        print("Director's nationality: " + self.director.getnationality())
        
        
        
class MyDVDCollection():
    """
    A class  that represents the film director
    
    """
    def __init__(self):
        self.dvdCollection = []
        self.nameOfCollection = "not set"
        
    def setcollectionName(self, cn):
        self.nameOfCollection = cn
        """
        sets the name of the DVD Collection
    
        """
        
    def getcollectionName(self):
        return self.nameOfCollection
        """
        returns the name of the DVD Collection
    
        """
    
    def addDVD(self,d):
        """
        A function that adds DVD objects to a DVD Collection
    
        """
        if (d in self.dvdCollection) == True:
            print("This DVD is already in your " + self.nameOfCollection)
            print("\n")
  
        else:     
            self.dvdCollection.append(d)
            print("DVD added successfully to your collection '{}'" .format(self.nameOfCollection))
            print("\n")
            
    def printCollectionDetails(self):
        """
        A function that prints the details of a DVD collection
    
        """
        print("Name of DVD Collection: " + self.nameOfCollection)
        print("\n")
        for d in self.dvdCollection:
            print(d.printDVDdetails())
            print("\n")
            
    def printdvdCollectionStatus(self):
        """
        A function that prints the content status of a DVD collection
    
        """
        if (len(self.dvdCollection) != 0):
            print("DVD collection '{}'".format(self.nameOfCollection) + " is not empty!")
            print("\n")
        else:
            print("DVD collection is empty!")
            print("\n")
            
        
    
    def printDVDbyDirector(self, name):
        """
        A function that prints DVDs by a particular director
    
        """
        
        for d in self.dvdCollection:
            if (d.director.getdirectorName == name):
                print("DVDs by '{}'" .format(d.director.getdirectorName()))
                print("\n")
                d.printDVDdetails()
        
 
               
def test_1():
    """
        A general test function
    
    """
    dir1 = FilmDirector()
    dir1.setdirectorName("Tim Burton")
    dir1.setdirectorAge(55)
    dir1.setnationality("America")
    
    dir2 = FilmDirector()
    dir2.setdirectorName("James Cameron")
    dir2.setdirectorAge(60)
    dir2.setnationality("American")
    
    dir3 = FilmDirector()
    dir3.setdirectorName("Steven Spielberg")
    dir3.setdirectorAge(65)
    dir3.setnationality("British")
    
    dvd1 = DVD(dir1)
    dvd1.settitle("Ghost Bride")
    dvd1.setrunningTime(80)
    dvd1.setdvdgenre("Animation")
    
    dvd2 = DVD(dir2)
    dvd2.settitle("Terminator 2: Judgment Day")
    dvd2.setrunningTime(160)
    dvd2.setdvdgenre("ScFi")
    
    dvd3 = DVD(dir3)
    dvd3.settitle("Avatar")
    dvd3.setrunningTime(90)
    dvd3.setdvdgenre("ScFi")
    
    dvd4 = DVD(dir1)
    dvd4.settitle("Nightmare Before Christmas")
    dvd4.setrunningTime(80)
    dvd4.setdvdgenre("Animation")
    
    
    collection1 = MyDVDCollection()
    collection1.setcollectionName("Summer movies")
    
    
    collection1.addDVD(dvd1)     
    collection1.addDVD(dvd2)
    collection1.addDVD(dvd3)
    collection1.addDVD(dvd4)
    """
        A test statement that checks if a DVD is added to a collection
    
     """
    
#    collection1.printdvdCollectionStatus()
    """
        A test statement on content status of a DVD collection
    
    """
    
#    collection1.printDVDbyDirector(dir1.getdirectorName)
    """
        A test statement on DVDs by a director
    
    """
    
#    collection1.printCollectionDetails()
    """
        A test statement on details of contents of a dvd collection 
    
    """
    
    
    
    
    
    
    
                
            
    
    
        
        
        
    
    
    
    