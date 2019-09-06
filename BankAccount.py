# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:54:21 2019
@author: ngarcia
Problem set:
    https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/05-Object%20Oriented%20Programming/04-OOP%20Challenge.ipynb

--> Creating bank account class
"""

class Account:
    
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return ('Account Owner: {}. \nAccount balance: ${}.'.format(self.owner,self.balance))
    
    def deposit(self,depo):
        self.balance = self.balance + depo
        return '{} has been deposited. Your new balance is ${}.'.format(depo,self.balance)
    
    def withdraw(self,withdrawal):
        if withdrawal > self.balance:
            return 'withdrawal exceeds balance amount. ${} is greater than ${}'.format(withdrawal,self.balance)
        elif withdrawal == self.balance:
            self.balance = self.balance - withdrawal
            return "You've withrawed the full balance, ${}".format(withdrawal)
        else:
            self.balance = self.balance - withdrawal
            return '${} has been withdrawed. Your new balance is ${}.'.format(withdrawal,self.balance)
    
  
