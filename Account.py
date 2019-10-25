# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 00:27:49 2019

@author: Supi
"""

class Account:
    def __init__(self):
        self.amount = 200
        
    def savings(self,amount):
        print("Savings amount : {}".format(amount))
         
    def checking(self):
        print("checking Balance : {}".format(self.amount))
    
    def transfer(self,amount, account):
        print("Transfer amount : {}".format(amount))
        if self.amount < amount:
           print("Transfer amount is greater than checking Balance: {}".format(amount))
        else:
           self.amount -= amount
           account.deposit(amount)
         
    def deposit(self,amount):
        print("checking.deposit:{}".format(amount))
        
            
     
def test3():
  s1 = Account() 
  s1.savings(200) 
  s1.checking()
  s1.deposit(500)
  s1.transfer(150)
  s1.checking()
  
 