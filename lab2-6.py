import turtle
#Exercise 6
#Generalization and composition with function objects

def half_Diamond(t,n,length,angle):
    """It serves as a way to cut some repetitive tasks."""
    for i in range(n):
        t.forward(length)
        t.left(angle)
        t.forward(length)
        t.right(angle)
           
def diamond_chain(t,n,length,angle):
    """It draws 'n' number of diamonds, 't' is for turtle.
       'angle' defines the initial angle openning."""
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
    #t.speed(0)
    for i in range(petal):
        diamond_chain(t,n,length,angle)
        t.left(petals)
###############################################################################
        """Sample flowers from exercise 6.3"""
def flower_0(t):
    param = [3,5,35,15]
    diamond_flower(t,param[0],param[1],param[2],param[3])
def flower_1(t):
    param = [1,25,90,6]
    diamond_flower(t,param[0],param[1],param[2],param[3])
def flower_2(t):
    param = [3,30,25,7]
    diamond_flower(t,param[0],param[1],param[2],param[3])
def flower_3(t):
    param = [2,15,75,9]
    diamond_flower(t,param[0],param[1],param[2],param[3])
    
# flower_0(turtle)
# flower_1(turtle)
# flower_2(turtle)
##############################################################################  
def stamp_grid(t,size,spacing,stamp_func):
    t.speed(0)
    for grid in range(size):
        """Innitial loop that defines the grid"""
        for i in range(size):
            """Nested loop draws 'size' number of flowers"""
            t.pendown()
            stamp_func(t)
            t.penup()
            t.forward(spacing)
        """Correction to the use of the turtle.home() built-in function."""
        t.left(180)
        t.forward((grid-size)+1*spacing)
        t.right(90)
        t.forward((grid+1)*spacing)
        """The 'grid' value of the initial loop is multiplied by the 'spacing'\
           in order to reach the grid-like output."""
        t.left(90)
        t.pendown()
###############################################################################

stamp_grid(turtle,4,40,flower_0)
turtle.clear()
stamp_grid(turtle,5,60,flower_1)
turtle.clear()
stamp_grid(turtle,2,80,flower_2)
turtle.clear()
stamp_grid(turtle,6,110,flower_3)

