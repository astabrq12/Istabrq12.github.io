import turtle
import math
george =turtle.Turtle()
# Set the background color
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Create our turtle
george.shape("turtle")
george.speed(50)


# Define a funtion to draw and fill a rectangle with the given
# dimensions and color
def drawRectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()


# Define a function to draw and fill an equalateral right
# triangle with the given hypotenuse length and color.  This
# is used to create a roof shape.
def drawTriangle(t, length, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.right(135)
    t.forward(length / math.sqrt(2))
    t.right(90)
    t.forward(length / math.sqrt(2))
    t.right(135)
    t.end_fill()


# Define a function to draw and fill a parallelogram, used to
# draw the side of the house
def drawParallelogram(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.left(30)
    t.forward(width)
    t.left(60)
    t.forward(height)
    t.left(120)
    t.forward(width)
    t.left(60)
    t.forward(height)
    t.left(90)
    t.end_fill()


# Define a function to draw four sun rays of the given length,
# for the sun of the given radius.  The turtle starts in the
# center of the circle.
def drawFourRays(t, length, radius):
    for i in range(4):
        t.penup()
        t.forward(radius)
        t.pendown()
        t.forward(length)
        t.penup()
        t.backward(length + radius)
        t.left(90)

# Tree base
george.left(90)
def draw2(l):
    if l<10:
        return
    else :

        george.pencolor("green")
        george.forward(l)
        george.left(30)
        draw2(3*l/4)
        george.color("brown")
        george.right(60)
        draw2(3*l/4)
        george.color("brown")
        george.left(30)
        george.backward(l)
        george.pencolor("")
def draw3(l):
    if l<10:
        return
    else :
        george.forward(l)
        george.left(30)
        draw2(3*l/4)
        george.color("brown")
        george.right(60)
        draw2(2*l/4)
        george.color("brown")
        george.left(30)
        george.backward(l)
        george.color("brown")

# Put down some labels
george.color("black")
george.penup()
george.goto(-150, 70)
george.pendown()
george.penup()
george.goto(130, 150)
george.pendown()
george.penup()
george.goto(-250,-120)
george.pendown()

#raw2(100)
george.penup()
def drawSun():
    george.setheading(0)
    george.fillcolor("yellow")
    george.penup()
    george.goto(-650, 250)
    george.pendown()
    #george.color("black")
    george.begin_fill()
    george.circle(30)
    george.end_fill()


def drawCloud():
    george.setheading(90)
    george.fillcolor("white")
    george.penup()
    george.pendown()
    george.begin_fill()

    george.color("white")
    for x in range(7):
        george.circle(20)
        george.right(50)
        george.forward(10)
    george.end_fill()
    george.setheading(90)
    george.penup()

#######
george.goto(500, 250)
drawCloud()
drawSun()
george.penup()
#george.goto(300, 250)
george.pendown()
drawCloud()
#george.goto(250,250)
drawCloud()
george.penup()
george.goto(450,250)
george.pendown()
drawCloud()
george.penup()
george.goto(300, 250)
george.pendown()
drawCloud()
george.goto(250,250)
drawCloud()
george.penup()
#garden
george.penup()
george.goto(8,-80)
george.begin_fill()
george.right(90)
george.pendown()
george.color("green")
george.forward(770)
george.right(90)
george.forward(300)
george.right(90)
george.forward(920)
george.right(110)
george.forward(270)
george.end_fill()
#garden2
george.penup()
george.goto(-150,-80)
george.begin_fill()
george.color("green")
george.pendown()
george.left(110)
george.forward(620)
george.left(90)
george.forward(300)
george.left(90)
george.forward(430)
george.left(55)
george.forward(315)
george.end_fill()
# Draw and fill the front of the house
def drawBush( x, y):
    george.setheading(90)
    george.fillcolor("darkgreen")
    george.width(5)
    george.penup()
    george.goto(x, y)
    george.pendown()
    george.begin_fill()

    george.color("darkgreen")
    for x in range(10):
        george.circle(15)
        george.right(36)
        george.forward(10)
    george.end_fill()
    george.setheading(90)
drawBush(30,10)
def drawPath():
    george.setheading(90)
    george.color("tan")
    george.fillcolor()
    george.penup()
    george.goto(-350, -385)
    george.begin_fill()
    george.pendown()
    george.right(30)
    george.forward(300)
    george.right(60)
    george.forward(150)
    george.right(80)
    george.forward(260)
    george.right(80)
    george.end_fill()
    george.setheading(90)
drawPath()
def drawHouse():
    george.color("white")
    george.penup()
    george.goto(-250, -150)
    george.pendown()
    george.setheading(90)
    george.fillcolor("white")
    george.begin_fill()
    george.forward(250)
    roof1 = george.position()
    george.right(90)
    george.forward(300)
    roof2 = george.position()
    george.right(90)
    george.forward(250)
    george.right(90)
    george.forward(300)
    george.right(90)
    george.end_fill()

    # roof
    george.penup()
    george.goto(roof1)
    george.color("black")
    george.begin_fill()
    george.pendown()
    george.goto(-150, 200)
    george.goto(roof2)
    george.goto(roof1)
    george.end_fill()
    george.setheading(90)
drawHouse()
def drawDoor( x, y):
    # door
    george.penup()
    george.goto(x, y)
    george.color("orange")
    george.begin_fill()
    george.setheading(90)

    for x in range(2):
        george.forward(90)
        george.right(90)
        george.forward(40)
        george.right(90)

    george.end_fill()

    # handle
    george.begin_fill()
    george.color("yellow")
    george.penup()
    george.goto(x-80, y + 40)
    george.begin_fill()
    george.circle(4)
    george.end_fill()
drawDoor(-120,-150)
def drawWindow( x, y, z):
    george.width(4)
    george.color("black")
    george.fillcolor("lightblue")

    if z == "square":
        george.penup()
        george.goto(x, y)
        george.pendown()
        george.begin_fill()

        for y in range(4):
            for x in range(4):
                george.forward(20)
                george.right(90)
            george.left(90)
        george.end_fill()
    else:
        george.penup()
        george.goto(x, y)
        george.pendown()
        george.backward(20)
        george.right(90)
        george.begin_fill()
        george.circle(20)
        george.end_fill()
        george.goto(x, y)

        for x in range(2):
            george.forward(20)
            george.backward(40)
            george.forward(20)
            george.right(90)

drawWindow(-90,50,"circle")
drawWindow(-180,50,"square")
drawWindow(5,50,"square")
drawWindow(-180,-90,"square")
drawWindow(-5,-90,"square")
george.penup()
george.goto(-600, -120)
george.pendown()
drawRectangle(george, 100, 110, "blue")

# Draw and fill the front door
george.penup()
george.goto(-600, -170)
george.pendown()
drawRectangle(george, 40, 60, "lightgreen")

# Front roof
george.penup()
george.goto(-600, -120)
george.pendown()
drawTriangle(george, 100, "magenta")

# Side of the house
george.penup()
george.goto(-545, -90)
george.pendown()
drawParallelogram(george, 60, 110, "yellow")

# Window
george.penup()
george.goto(-560, -110)
george.pendown()
drawParallelogram(george, 20, 30, "brown")

# Side roof
george.penup()
george.goto(-595, -122)
george.pendown()
george.fillcolor("orange")
george.begin_fill()
george.right(45)
george.forward(77)
george.right(100)
george.forward(100 / math.sqrt(2))
george.right(77)
george.forward(79)
george.right(100)
george.forward(100 / math.sqrt(2))
george.right(45)
george.end_fill()
george.penup()
#tree trunk
def trunk():
    george.begin_fill()
    george.color("brown")
    george.penup()
    george.goto(-350,-15)
    george.pendown()
    george.left(95)
    george.forward(100)
    george.left(90)
    george.forward(38)
    george.left(90)
    george.forward(100)
    george.left(90)
    george.forward(38)
    george.end_fill()

trunk()
drawBush(-350,0)
george.penup()
george.goto(150, -150)
george.pendown()
draw2(100)
george.penup()
george.goto(-450,-230)
george.pendown()
draw3(100)





turtle.done()