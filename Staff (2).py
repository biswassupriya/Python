#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:40:58 2019

@author: aep05101
"""

class Staff:
    def __init__(self):
        self.firstName = "not set"
        self.modules = []
        self.noOfModules = 0
        
    def getFirstName(self):
        return self.firstName
    
    def setFirstName(self, n):
        self.firstName = n
    
    def addModule(self, m):
        self.modules.append(m)
        
    def printModuleListDetails(self):
        for m in self.modules:
            m.printModuleDetails()
        
class Module:
    def __init__(self):
        self.name = "not set"
        self.code = "not set"
        
    def getName(self):
        return self.name
    
    def setName(self, n):
        self.name = n
    
    def printModuleDetails(self):
        print("Name: " + self.name)
        print("Code: " + self.code)
    
        
def test():
    s1 = Staff()
    print("Name...")
    print(s1.getFirstName())
    s1.setFirstName("Kostas")
    print("New name...")
    print(s1.getFirstName())
    
def test_1():
    s1 = Staff()
    m1 = Module()
    m2 = Module()
    s1.addModule(m1)
    s1.addModule(m2)
    s1.printModuleListDetails()