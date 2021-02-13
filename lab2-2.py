import turtle
#Exercise 2
#Simple for loops to reduce repetition

turtle.right(45)
for i in range(3):
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
turtle.forward(50)
for i in range(3):
    turtle.left(90)
    turtle.forward(50)
for i in range(3):
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
turtle.left(135)
turtle.done()