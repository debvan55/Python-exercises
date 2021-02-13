#Exercise 4

import math

def base_10log(x):
    return math.log10(x) #Return the base 10 logarithm of x.
    
def  log2of_(x):
    return math.log2(x) #Return the base 2 logarithm of x.
 
def radianS(x):
    return math.radians(x) #Convert angle x from degrees to radians.
      
def sq_root(x):
    return math.sqrt(x) #Return the square root of x.
    
def circ_X(x):
    return math.pi*(x**2) #Returns the area of a circle with a radius of 'x'
    
def sin_X(x):
    return math.sin(x) #Return the sine of x (measured in radians).

def tan_X(x):
    return math.tan(x) #Return the tangent of x (measured in radians).

def say_math(f,x):
    f(x)
    print('The result of '+str(f.__name__)+' applied to '+str(x)+' is '+ str(f(x)))
    
say_math(base_10log,16)
say_math(log2of_,8)
say_math(radianS,50)
say_math(sq_root,64)
say_math(circ_X,100)
say_math(sin_X,32)
say_math(tan_X,18)
