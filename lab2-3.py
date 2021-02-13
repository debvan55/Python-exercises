import turtle
#Exercise 3
#Generalization via encapsulation
       
def single_Diamond(t):
    """Draws a single diamond."""
    t.right(45)
    for i in range(4):
        t.forward(50)
        t.left(90)

def plus_One(t):
    """This function serves as link to keep adding diamonds
       to the sequence as needed."""
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.right(45)
        
def diamond_chain(t,n):
    """It draws 'n' number of diamonds"""
    for i in range(n):
        single_Diamond(t)
        plus_One(t)
    print("diamond_chain draws: "+str(n)+" diamond(s).")
    #t.done()
    
diamond_chain(turtle,2)
diamond_chain(turtle,4)
# diamond_chain(turtle,20)
# diamond_chain(turtle,4)

