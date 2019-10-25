# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 01:32:53 2019

@author: Supi
"""

class BankAccount1:
    def __init__(self):
        self.amount = 0.0
        
    def deposit(self,amount):
         print("Depositing amount : {}".format(amount))
         if amount <= 0:
           print('amount should be greater than 0. The deposit amount was: {}'.format(amount))
         else:
          self.amount += amount 
         
    def balance(self):
         print("Current Balance of : {}".format(self.amount))
    
    def withdraw(self,amount):
        print("Withdrawing amount : {}".format(amount))
        if self.amount < amount:
           print("withdraw amount is greater than current balance: {}".format(amount))
        else:
         self.amount -= amount 
         
    def transfer(self,amount, account):
        print("Transfer amount : {}".format(amount))
        if self.amount < amount:
           print("Transfer amount is greater than current Balance: {}".format(amount))
        else:
           self.withdraw(amount)
           account.deposit(amount)    
     
def test2():
  s1 = BankAccount1() 
  s1.balance()
  s1.deposit(500)
  s1.balance()  
  s1.deposit(-20)
  s1.withdraw(20)
  s1.balance()
  s1.withdraw(600)
  
  s2 = BankAccount1()
  
  
  print("\nBalance before the transfer")
  s1.balance()
  s2.balance()
  s1.transfer(200,s2)
  print("Balance after the transfer")
  s1.balance()
  s2.balance()
 
  
  
  
     
     
        