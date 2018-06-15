#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 13:47:13 2018

@author: shashidhar
"""
# Importing math module for using Square root
import math
# Defining add function for adding 2 numbers
def add(a,b):
    return (a+b)
# Defining subtract function for subtracting 2 numbers
def sub(a,b):
    return (a-b)
# Defining multiply function for multiply 2 numbers
def mul(a,b):
    return (a*b)
# Defining division function for dividing 2 numbers
def div(a,b):
    return (a/b)
# Defining square function for squaring a number
def square(a):
    return (a*a)
print('Welcome to my Calculator\n')
# Initializing the default value
result=0 

# Defining an infinite loop
while(1):
    if (result==0): # This piece of code executes for the first time (or) when result value is cleared
        try:
            result = int(input('Enter any number-')) # Taking user input of first number
        except ValueError:
            print('Please enter a valid number')
    print('''Choose any Operation:
              1.Addition
              2.Subtraction
              3.Multiplication
              4.Division
              5.Squaring
              6.Squareroot
              7.Print Result
              8.Clear Result
              9.Exit''')
    # Taking the selection from above    
    x=input() 
    if (x=='9'):
        print('Thank you for using Calculator.....') # shutting down
        break
    elif (x=='7'):
        print('Result='+str(result))  # Printing the result
    elif (x=='8'):
        result = 0
        print('Result is Cleared.........') # Clearing the result
    elif ((x=='1')or(x=='2')or(x=='3')or(x=='4')or(x=='5')or(x=='6')):
        try:
            if (x=='5'):
                result=square(result) # Squaring the input and printing the result
                print('Result='+str(result)) 
                continue # Skipping the remaining statements in the loop
            elif (x=='6'):
                result=math.sqrt(result) # Performing square root of input and printing the result
                print('Result='+str(result))
                continue # Skipping the remaining statements in the loop
            b = int(input('Enter 2nd number-')) # Taking 2nd input to perform selected operation with 1st input
            if (x=='1'):
                result=add(result,b) # Adding the numbers and printing the result
                print('Result='+str(result))
            elif (x=='2'):
                result=sub(result,b) # Subtracting the numbers and printing the result
                print('Result='+str(result))
            elif (x=='3'):
                result=mul(result,b) # Multiplying the numbers and printing the result
                print('Result='+str(result))
            else:
                result=div(result,b) # Dividing the numbers and printing the result
                print('Result='+str(result))
        except ValueError:
            print('Please enter Integer')
        except ZeroDivisionError:
            print('You are trying to divide with zero')
    else:
        print('Please Select from the options mentioned')