#Exercise 3
 
import math

def answer_quadratic(a,b,c):
    
    x1 =(-b - math.sqrt( (b**2)-(4*a*c))) / (2*a)
    x2 =(-b + math.sqrt( (b**2)-(4*a*c))) / (2*a)

    print('The quadratic formula x values represented as: ' \
          'x =(-'+str(b)+' ± math.sqrt( ('+str(b)+'**2)-(4*'+str(a)+'*'+str(c)+'))) / (2*'+str(a)+ \
          ')  are: x1 ='+str(x1) +' & x2 ='+str(x2))

answer_quadratic(4,6,2)
answer_quadratic(2,8,6)
answer_quadratic(6,15,1) #this one is fun, outputs a weird number


#print(x1)
#NameError: name 'x1' is not defined
#The output error is a syntax error kind.
#The value for x1 "exists" only inside of the function()
#By prompting the arguments to the function, we add value to the parameters.