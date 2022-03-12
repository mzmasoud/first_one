from cmath import pi
import turtle
import math

wn = turtle.Screen()

wn.bgcolor("pink")

mate = turtle.Turtle()
mate.shape("arrow")
mate.pensize(1)
mate.forward(50)
mate.speed(2)
mate.left(90)
mate.forward(50)

for i in range (1000):
    l = mate.distance(0,0)
    l = 50/l
    last_x,last_y=mate.pos()
    mate.setpos(0,0)
    mate.setpos(last_x,last_y)
    e = math.asin(l)
    e = e*(180)/pi
    mate.left(e)
    mate.forward(50)

    
wn.mainloop()    