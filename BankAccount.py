# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 22:47:10 2019

@author: Supi
"""

class BankAccount:
    def __init__(self):
        self.amount = 0.0
        
    def deposit(self,amount):
         print("Depositing amount : {}".format(amount))
         if amount <= 0:
           print('amount should be greater than 0. The deposit amount was: {}'.format(amount))
         else:
          self.amount += amount 
         
    def balance(self):
         print("Balance is: {}".format(self.amount))
    
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
  checking = BankAccount() 
  print("Checking Account opening Balance")
  checking.balance()
  checking.deposit(500)
  print("Checking Account Balance after depositing 500")
  checking.balance()  
  checking.deposit(-20)
  checking.withdraw(20)
  print("Checking Account Balance after withdrawing 20")
  checking.balance()
  checking.withdraw(600)
  
  savings = BankAccount()
  
  print("Checking Account Balance before transfer")
  checking.balance()
  print("Saving Account Balance before transfer")
  savings.balance()
  checking.transfer(200,savings)

  print("Checking Account Balance after transfer")
  checking.balance()
  print("savings Account Balance after transfer")
  savings.balance()
 
  
  
  
     
     
        