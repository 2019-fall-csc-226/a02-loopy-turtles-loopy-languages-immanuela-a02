import turtle
#Your program uses the Turtle library to draw on the screen.
#Your program uses at least two turtle objects to draw.
#What you draw is something that brings a smile to your face.
#The program uses at least one loop.
#The program makes use of multiple attributes and methods of either the turtle class,
# the screen class, or both. You can explore the full lists of methods here and here, respectively.
#Your program has the standard header block used in all our programs.
#Add comments to clarify your intent on any lines that are doing something that is not immediately clear.

def smiley ():
    smile = turtle.Turtle()
    smile.pensize("30")
    wn = turtle.Screen()
    wn.bgcolor('blue')
    smile.penup()
    smile.setposition (-100,200)
    smile.pensize("30")
    smile.shape('circle')
    smile.pendown()
    for i in range (4):
        smile.forward(100)
        smile.right(45)
        smile.forward(100)
        smile.right(45)
        smile.forward (50)
    for i in range (2):
        smile.color("yellow")
        smile.right(45)
        smile.forward(50)
    smile.color("black")
    smile.penup()
    smile.setposition (-160,100)
    smile.right(-90)
    smile.forward (10)
    for i in range (2):
        smile.pendown()
        smile.forward (10)
        smile.penup()
        smile.forward (120)
    smile.down()
    smile.penup()
    smile.write("PRIVATE EYES ARE WATCHING YOU!   - Hall and Oats", move=True, align='left', font=("Arial", 15, ("bold", "normal")))
    smile.color("blue")
    wn.exitonclick()
smiley()
