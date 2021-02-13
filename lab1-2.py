#Exercise 2
 
import math

a = 4
b = 6
c = 2
x1 =(-b - math.sqrt( (b**2)-(4*a*c))) / (2*a)
x2 =(-b + math.sqrt( (b**2)-(4*a*c))) / (2*a)

print('The quadratic formula x values represented as: ' \
      'x =(-'+str(b)+' ± math.sqrt( ('+str(b)+'**2)-(4*'+str(a)+'*'+str(c)+'))) / (2*'+str(a)+ \
      ')  are: x1 ='+str(x1) +' & x2 ='+str(x2))

#ValueError: math domain error
#The output error is a runtime error kind I believe.
#Python library "math" can't give a complex number output.
#We could use "cmath" library, "cmath" deals with complex numbers.