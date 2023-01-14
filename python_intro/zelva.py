from turtle import exitonclick
from turtle import forward
from turtle import left
from turtle import right
from turtle import penup
from turtle import pendown
from turtle import goto
from math import sqrt

#tzv australské město

def draw_house(a):
    c = round(sqrt(2*a**2))
    forward(a)
    right(90)
    forward(a)
    right(90)
    forward(a)
    right(90)
    forward(a)

    right(90+45)
    forward(c)
    right(90)
    
    forward(c/2)
    right(90)
    forward(c/2)
    right(90)

    forward(c)
    right(45)

penup()
goto(-450, 0)
pendown()

draw_house(100)
draw_house(50)
draw_house(200)
draw_house(71)
draw_house(112)
draw_house(66)
draw_house(12)
draw_house(33)
draw_house(45)

exitonclick()