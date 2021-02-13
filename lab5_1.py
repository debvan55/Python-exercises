#Lab 5 Exercise 1

import math

def first_pass(n):
    """Takes parameter 'n' and checks if its an integer."""
    a_pass = isinstance(n,(int))
    return a_pass

def isprime(n):
    """Using 'first_pass', a series of conditions and a loop
       defines whether the input 'n' is or NOT a prime number."""
    if first_pass(n) and n > 1:# !print statement option outputs what is the rule that defined the number.
        if n == 2 or n ==3:
            #print("It is prime! Either 2 or 3.")
            return True
        elif n % 2 == 0 or n % 3 == 0:
            #print("Evenly divisible by 2 or 3.")
            return False 
        else:
            i = 5 # 'i' is defined (very useful)
            if i == n :
                return True
                #print("It is prime! " + str(i))
            elif i < n:
                while math.sqrt(i) < n:
                    #print (i)
                    #print (math.sqrt(i))
                    i = i + 6
                    if i % 2 == 0 or i+2 % 2 == 0:
                        #print('NOT prime from check inside of loop' + str(i))
                        return False #NOT prime!
                    break # 'i' reached the point where math.sqrt(i) >= n  
                #print('Outside of the loop the result of previous conditions returns as True ' + str(n))    
                return True #It 'IS' Prime!!
            
    #print("'n' is not an integer or is not larger than 1")
    return False
           
#isprime(76577884333)
