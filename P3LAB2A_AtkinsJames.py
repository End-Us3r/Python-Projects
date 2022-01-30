#James Atkins
#CTI-110 P3LAB2A
#10-08-2021
#This program draws shapes with turtle graphics

import turtle
turtle.shape("turtle")
#Square
for i in [0,1,2,4]:
    turtle.forward(50)
    turtle.left(90)
#Triangle
turtle.left(120)
for i in [0,1,2]:
    turtle.forward(80)
    turtle.left(120)
         
turtle.exitonclick()
