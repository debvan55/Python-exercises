#Lab 4 Exercise 2

import math

def is_numeric(n):
    """Takes one parameter and checks; it returns a boolean value."""
    func_input = isinstance(n,(int,float))
    if func_input:
        return func_input
    return func_input

def hypotenuse(a,b):
    """Returns length of hypotenuse of a right triangle,
       given the legths of the two legs as a arguments"""
#Returns no value under any of the following circumstances:
#Either a or b is not a number
    if is_numeric(a):
        if is_numeric(b):
            if a <= 0  or b <=0:
            #Either a or b is less than or equal to 0   
                return None
            else:
                answer = int(math.sqrt((a**2)+(b**2)))
                #print(int(math.sqrt((a**2)+(b**2))))
                #print(math.hypot(a,b))  #doble-check!
                return answer
        pass
    return None