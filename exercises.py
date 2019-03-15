import turtle
n = turtle.Turtle()
def c1(x,z):
    n.speed(25)

    for i in range(180):
        n.forward(100)
        n.color(z)
        n.right(30)
        n.forward(20)
        n.left(60)
        n.color(x)
        n.forward(50)
        n.color(x)
        n.right(30)
        n.penup()
        n.setposition(0, 0)
        n.pendown()
        n.right(2)
c1("red","black")

turtle.done()