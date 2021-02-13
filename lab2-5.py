import turtle
#Exercise 5
#Composing/reusing functions

def half_Diamond(t,n,length,angle):
    """It serves as a way to cut some repetitive tasks."""
    for i in range(n):
        t.forward(length)
        t.left(angle)
        t.forward(length)
        t.right(angle)
           
def diamond_chain(t,n,length,angle):
    """It draws 'n' number of diamonds, 't' is for turtle.
       'angle' defines the initial angle openning.
       Read the print OUTPUT for more information."""
    t.right(angle/2)
    half_Diamond(t,n,length,angle)
    t.left(angle/2)
    t.right(angle/2+180)
    half_Diamond(t,n,length,angle)   
    t.left(angle/2+180)
    
def diamond_flower(t,n,length,angle,petal):
    petals=360/petal
    """The 'petals' variable divides 360(the degrees in a full circle)
       between the 'petal' argument.
       This gives the function an exact number to fit all the desired 'petals' of the flower"""
    t.speed(9)
    for i in range(petal):
        diamond_chain(t,n,length,angle)
        t.left(petals)
    print("diamon_flower draws a flower with "+str(petal)+\
         " petal(s), each petal with "+str(n)+\
         " diamond(s).'length' defines the number of pixels of every line segment in the diamond ("\
         +str(length)+"pxs). The measure of the angle openning horizontally is "\
         +str(angle)+"° degrees and the angle openning vertically is that of "\
         +str(-(angle-180))+"° degrees.")
        
diamond_flower(turtle,1,30,30,6)
diamond_flower(turtle,4,60,90,10)
diamond_flower(turtle,8,90,150,16)

