import turtle
def multi_square (turtle , size):
    for color in ["red","blue","purple","yellow"]:
        turtle.color(color)
        turtle.forward(size)
        turtle.left(90)

window = turtle.Screen()

window.bgcolor("pink")
rocky = turtle.Turtle()
rocky.pensize(4)
value = 20

for i in range (15) :
    multi_square (rocky , value)
    value += 10 
    
    rocky.forward(10)
    rocky.left(18)

window.mainloop ()    




