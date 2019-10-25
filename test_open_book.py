# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:23:33 2019

@author: mhb19201
"""

class Artist():
    """ 
    Class to represent a Artist.
    """
    def __init__ (self):
       self.firstName = "Not set"
       self.lasttName = "Not set"
       
    def setFirstName(self, firstName):
         """
         Sets the first name of Artist
         """
         self.firstName = firstName
 
    def setLastName(self, lastName):
         """
         Sets the last name of Artist
         """
         self.lasttName = lastName
        
    def getFirstName(self):
         """
         Gets the first name of Artist
         """
         return self.firstName
        
    def getLastName(self):
         """
         Gets the last name of Artist
         """
         return self.lastName
 


class MusicTrack():
    """
    A class  that represents MusicTrack
    """
    def __init__(self, artist):
        self.title = "not set"
        self.artist  = artist
        self.runningTime = 0
        
    def settitle(self, t):
        """
        Sets the title of the MusicTrack.
        """
        self.title = t        

            
    def setRunningTime(self, r):
        """
        Sets the length of the MusicTrack.
        """
        self.runningTime = r
        
          
    def setArtist(self, artist):
        """
        Sets the artist of the MusicTrack.
    
        """
        self.artist = artist
    
    def gettitle(self):
        """
        Gets the title of the MusicTrack.
        """
        return self.title


    def getRunningTime(self):
        """
        Gets the time of the MusicTrack.
        """
        return self.running_time
   
    def getDirector(self):
        """
        Gets the artist of the MusicTrack.
        """
        return self.artist
    
        
    def printMusicTrackdetails(self):
        """
        Prints the details of a MusicTrack. 
        """
        print("Title of MusicTrack: " + self.title)
        print("The DVD length: {} mins".format(self.runningTime))
        print("Artist full name: " + self.artist.getFirstName()+ self.artist.getLasttName())

        
        
        
        
class MyMusicTrackCollection():
    """
    Class to represent a colection of MusicTrack.
    """
    def __init__ (self):
         
        self.nameOfColection= "not set"
        self.colectionlist= []
        
    def setNameOfColection(self,nameOfColection):
        """
        Sets the name of the MusicTrack Colection.
        """
        self.nameOfColection= nameOfColection
     
    def setColectionlist(self,colectionlist):
        """
        Sets the list of the MusicTrack Colection.
        """
        self.colectionlist=colectionlist
        
    def getNameOfColection(self):
         """
        Gets the name of the MusicTrack Colection.
        """
         return self.nameOfColection
     
    def getColectionlist(self):
        """
        Gets the list of the MusicTrack Colection.
        """
        return self.colectionlist
     
    def addMusicTrack(self, musicTrack):
        """
        Adds a MusicTrack to Colection list.
        """
        if (musicTrack in self.Colectionlist):
             print("This music track is already in your colection")
        else:
             self.Colectionlist.append(musicTrack)
             print("Music track added successfully to your collection")
         
         
    def printColectionDetails(self):
         """ 
         Prints if the Colection details.
         """
         print ("MusicTrack Collection name: " + self.nameOfColection )
         for musicTrack in self.Colectionlist:
             musicTrack.printMusicTrackdetails()
    
             
             
    def emptyColection(self):
         """ 
         Prints if the musicTrack Colection is empty or not.
         """
         if (len(self.Colectionlist))==0:
             print("Music track collection is empty!")
         else:
             print("Music track collection is not empty!")
    
    def checkByTime (self, runningTime ):
         for musicTrack in self.Colectionlist:
             if runningTime.getRuningTime().getFirstName():
                 musicTrack.printMusicTrackdetails()


def test_1():
    """
        A general test function
    
    """
    art1 = Artist()
    art1.setFirstName("John")
    art1.setLasttName("Galvin")
    
 
    track1 = MusicTrack(art1)
    track1.settitle("Ghost")
    track1.setrunningTime(8)
 
    track2 = MusicTrack(art1)
    track2.settitle("Avar")
    track2.setrunningTime(9)


    collection1 = MyMusicTrackCollection()
    collection1.getNameOfColection("Summer songs")
    
    collection1.emptyColection()
    
    collection1.addMusicTrack(track1)     
    collection1.addMusicTrack(track2)
    collection1.addMusicTrack(track2)

    collection1.emptyDColection()

         
            
        