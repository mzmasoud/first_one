import turtle

wn = turtle.Screen()
te = turtle.Turtle()
wn.bgcolor("pink")
te.seth(-45)
te.pensize(7)
te.color("green")
te.speed(10)
te.hideturtle()

def tamrin(x):
     
  
  te.begin_fill() 

  for i in range(2):
    
    te.circle(x,90)
    te.circle(x//2,90)


  te.end_fill()
        
        
tamrin(200)  


 


wn.mainloop()   