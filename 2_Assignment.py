# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 19:48:44 2021

@author: Sanathanan
"""

# Assignment - 1
# Question: 2
# Write a Program to accept Uesr's First and last name and then getting them printed in the reverse 
# order with a space between first name and last name

first_name = input("Enter First Name: ") # Getting the user input of first_name
last_name = input("Enter Last Name: ") # Getting the user input of last_name

first_name = first_name[: :-1] # Reversing the first_name
last_name = last_name[: :-1] # Reversing the last_name

print(first_name,"", last_name)
