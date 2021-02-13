import turtle
#Exercise 4
#More generalization

def half_Diamond(t,n,length,angle):
    """It serves as a way to cut some repetitive series of tasks."""
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
    
    print("diamond_chain draws: "+str(n)+" diamond(s), of "+str(length)+\
          " pixels each line segment. The measure of the angle openning horizontally is "\
          +str(angle)+"° degrees and the angle openning vertically is that of "\
          +str(-(angle-180))+"° degrees.")
    #t.done()
    
diamond_chain(turtle,2,50,45)
diamond_chain(turtle,3,70,90)
diamond_chain(turtle,4,90,150)