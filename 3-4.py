#Lab 3 Exercise 4

import math

def lemme_guess():
    """Simply checks for the input being:
       either zero or a positive number"""
    
    init_num = int(input("Input a positive integer: "))
    low = int(0)
    high = init_num
    if init_num >= 0 :
        print("My turn! \n"
              "Pick a number between " +str(low)+ " and "+str(high)+", but don't tell me!")
        input("Press enter when you ready.")
        recurs_guess(low,high)
    else:
        print("Incorrect!...that is not a positive integer.")
        return
    
#######

def recurs_guess(low,high):
    """With the help of the 'math' module,
       rounds down a number between 0 and 'init_num' variable
       to try and find the number to be guessed  by the user
       using binary search."""
    
    comput_guess = math.floor((low+high)/2)
    ans = input("Is "+str(comput_guess)+" your number? \n"
                    "(Y = yes, H = too high, L = too low): ")
    if ans in ['Y']:
        print("I knew it!")
        return
    elif ans in ['L']:
        recurs_guess(comput_guess,high)
        #Too low? This number will be the new Low then!
    elif ans in ['H']:
        recurs_guess(low,comput_guess)
        #Too High? This number will be the new High then!
    else:
        recurs_guess(low,high)

lemme_guess()