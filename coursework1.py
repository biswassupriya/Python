# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 23:07:45 2019

@author: Supi
"""


class Artist:
    """
    Class to represent the artist.
    """

    def __init__(self):
        self.artistFirstName = "not set"
        self.artistLastName = "not set"

    def setArtistFirstName(self, artistFirstName):
        """
        Set the first name of the artist.
        """
        self.artistFirstName = artistFirstName

    def getArtistFirstName(self):
        """
        Return the first name of the artist.
        """
        return self.artistFirstName

    def setArtistLastName(self, artistLastName):
        """
        Set the last name of the artist.
        """
        self.artistLastName = artistLastName

    def getArtistLastName(self):
        """
        Return the last name of the artist.
        """
        return self.artistLastName


class MusicTrack:
    """
    Class to represent the music track.
    """

    def __init__(self, artist):
        self.title = "not set"
        self.artist = artist
        self.runningTime = 0

    def setTitle(self, title):
        """
        Set the title of the music track.
        """
        self.title = title

    def getTitle(self):
        """
        Return the title of the music track.
        """
        return self.title

    def setArtist(self, artist):
        """
        Set the artist of the music track.
        """
        self.artist = artist

    def getArtist(self):
        """
        Return the artist of the music track.
        """
        return self.artist

    def setRunningTime(self, runningTime):
        """
        Set the running time of the music track.
        """
        self.runningTime = runningTime

    def getRunningTime(self):
        """
        Return the running time of the music track.
        """
        return self.runningTime

    def printMusicTrackDetail(self):
        """
        Print all the details of the music track.
        """
        print("Title: " + self.title)
        print("Artist's First name: " + self.artist.getArtistFirstName())
        print("Artist's Last name: " + self.artist.getArtistLastName())
        print("Running Time: " + format(self.runningTime) + " minutes\n")


class MyMusicTrackCollection:
    """
    Class to represent the music track collection.
    """

    def __init__(self):
        self.musicTrackCollectionName = "not set"
        self.musicTrackCollection = []

    def setMusicTrackCollectionName(self, musicTrackCollectionName):
        """
        Set the music track collection name.
        """
        self.musicTrackCollectionName = musicTrackCollectionName

    def getMusicTrackCollectionName(self):
        """
        Return the music track collection name.
        """
        return self.musicTrackCollectionName

    def getMusicTrackCollection(self):
        """
        Return the music track collection list that contains music track objects.
        """
        return self.musicTrackCollection

    def printMusicTrackCollectionDetails(self):
        """
        Print the music track collection name and the details of all music track objects contained in it.
        """
        print("Music track collection name: " + self.musicTrackCollectionName)
        for musicTrack in self.musicTrackCollection:
            musicTrack.printMusicTrackDetail()

    def addMusicTrack(self, musicTrack):
        """
        Add a music track object at the end of the music track collection list.
        """
        if (musicTrack in self.musicTrackCollection):
            print("This music track is already in your collection!")
        else:
            self.musicTrackCollection.append(musicTrack)
            print("Music Track added successfully to your collection!")

    def emptyMusicTrackCollection(self):
        """
        Check whether the music track collection is empty.
        """
        if (len(self.musicTrackCollection)) == 0:
            print("Music track collection is empty!")
        else:
            print("Music track coolection is not empty!")

    def printMusicTrackByRunningTime(self, runningTime):
        """
        Print the details of all music track objects with running time greater or equal to the specific parameter value.
        """
        for musicTrack in self.musicTrackCollection:
            if (musicTrack.getRunningTime() >= runningTime):
                musicTrack.printMusicTrackDetail()


def test_7():
    """
    Fully tests the functionality of "Assessed Task 4"
    """
    artist1 = Artist()  # create an Artist object named artist1.
    musicTrack1 = MusicTrack(artist1)  # create a music track object named musictrack1.
    musicTrack2 = MusicTrack(artist1)  # create a music track object named musictrack2.
    musicTrackCollection1 = MyMusicTrackCollection()  # create a music track collection object named musicTrackCollection1.

    musicTrackCollection1.addMusicTrack(
        musicTrack1)  # append musicTrack1 object to the end of musicTrackCollection1 list, should print "Music Track added successfully to your collection!"
    musicTrackCollection1.addMusicTrack(
        musicTrack1)  # append musicTrack1 object again to the end of musicTrackCollection1 list, should print "This music track is already in your collection!"
    musicTrackCollection1.addMusicTrack(
        musicTrack2)  # append musicTrack2 object to the end of musicTrackCollection1 list, should print "Music Track added successfully to your collection!"
    musicTrackCollection1.addMusicTrack(
        musicTrack2)  # append musicTrack2 object again to the end of musicTrackCollection1 list, should print "This music track is already in your collection!"


def test_8():
    """
    Fully tests the functionality of "Assessed Task 5"
    """
    artist1 = Artist()  # create an Artist object named artist1.
    musicTrack1 = MusicTrack(artist1)  # create a music track object named musictrack1.
    musicTrack2 = MusicTrack(artist1)  # create a music track object named musictrack2.
    musicTrackCollection1 = MyMusicTrackCollection()  # create a music track collection object named musicTrackCollection1.

    musicTrackCollection1.emptyMusicTrackCollection()  # call the emptyMusicTrackCollection() method when the list is empty, should print "Music track collection is empty!".
    musicTrackCollection1.addMusicTrack(
        musicTrack1)  # append musicTrack1 object to the end of musicTrackCollection1 list, should print "Music Track added successfully to your collection!"
    musicTrackCollection1.addMusicTrack(
        musicTrack2)  # append musicTrack2 object to the end of musicTrackCollection1 list, should print "Music Track added successfully to your collection!"
    musicTrackCollection1.emptyMusicTrackCollection()  # call the emptyMusicTrackCollection() method again, now the list is not empty, should print "Music track coolection is not empty!".


def test_9():
    """
    Fully tests the functionality of "Assessed Task 6"
    """
    artist1 = Artist()  # create an Artist object named artist1.
    musicTrack1 = MusicTrack(artist1)  # create a music track object named musictrack1.
    musicTrack2 = MusicTrack(artist1)  # create a music track object named musictrack2.
    musicTrack3 = MusicTrack(artist1)  # create a music track object named musictrack3.
    musicTrack4 = MusicTrack(artist1)  # create a music track object named musictrack4.
    musicTrackCollection1 = MyMusicTrackCollection()  # create a music track collection object named musicTrackCollection1.

    musicTrack1.setTitle("Music track 1")  # set the title of musicTrack1 object as "Music track 1".
    musicTrack2.setTitle("Music track 2")  # set the title of musicTrack2 object as "Music track 2".
    musicTrack3.setTitle("Music track 3")  # set the title of musicTrack3 object as "Music track 3".
    musicTrack4.setTitle("Music track 4")  # set the title of musicTrack4 object as "Music track 4".

    musicTrack1.setRunningTime(1)  # set the running time of musicTrack1 object to 1 minute.
    musicTrack2.setRunningTime(2)  # set the running time of musicTrack2 object to 2 minute.
    musicTrack3.setRunningTime(3)  # set the running time of musicTrack3 object to 3 minute.
    musicTrack4.setRunningTime(4)  # set the running time of musicTrack4 object to 4 minute.

    print("before calling the method printMusicTrackByRunningTime()")
    musicTrackCollection1.printMusicTrackByRunningTime(3)  # nothing should be printed.
    print("after calling the method printMusicTrackByRunningTime()")

    musicTrackCollection1.addMusicTrack(
        musicTrack1)  # append musicTrack1 object to the end of musicTrackCollection1 list, should print "Music Track added successfully to your collection!"
    print("before calling the method printMusicTrackByRunningTime()")
    musicTrackCollection1.printMusicTrackByRunningTime(3)  # nothing should be printed.
    print("after calling the method printMusicTrackByRunningTime()")

    musicTrackCollection1.addMusicTrack(
        musicTrack2)  # append musicTrack2 object to the end of musicTrackCollection1 list, should print "Music Track added successfully to your collection!"
    print("before calling the method printMusicTrackByRunningTime()")
    musicTrackCollection1.printMusicTrackByRunningTime(3)  # nothing should be printed.
    print("after calling the method printMusicTrackByRunningTime()")

    musicTrackCollection1.addMusicTrack(
        musicTrack3)  # append musicTrack3 object to the end of musicTrackCollection1 list, should print "Music Track added successfully to your collection!"
    print("before calling the method printMusicTrackByRunningTime()")
    musicTrackCollection1.printMusicTrackByRunningTime(3)  # only the details of musicTrack3 should be printed.
    print("after calling the method printMusicTrackByRunningTime()")

    musicTrackCollection1.addMusicTrack(
        musicTrack4)  # append musicTrack4 object to the end of musicTrackCollection1 list, should print "Music Track added successfully to your collection!"
    print("before calling the method printMusicTrackByRunningTime()")
    musicTrackCollection1.printMusicTrackByRunningTime(
        3)  # only the details of musicTrack3 and musicTrack4 should be printed.
    print("after calling the method printMusicTrackByRunningTime()")
