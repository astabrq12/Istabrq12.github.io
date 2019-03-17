import turtle
v = turtle.Turtle()

def tr1():
    v.speed(20)
    v.hideturtle()
    v.begin_fill()
    v.fillcolor("yellow")
    v.circle(80)
    v.end_fill()

    v.pensize(6)
    v.begin_fill()
    v.penup()
    v.setposition(30, 80)
    v.pendown()
    v.fillcolor("black")
    v.circle(10)
    v.end_fill()

    v.begin_fill()
    v.penup()
    v.setposition(30, 87)
    v.pendown()
    v.fillcolor("white")
    v.circle(6)
    v.end_fill()

    v.pensize(6)

    v.begin_fill()
    v.penup()
    v.setposition(-30, 80)
    v.pendown()
    v.fillcolor("black")
    v.circle(10)
    v.end_fill()

    v.begin_fill()
    v.penup()
    v.setposition(-30, 87)
    v.pendown()
    v.fillcolor("white")
    v.circle(6)
    v.end_fill()

    v.penup()
    v.setposition(-35, 55)
    v.pendown()
    v.color("black")
    v.circle(-80, 50, 70)

    v.penup()
    v.setposition(30, 120)
    v.pendown()
    v.color("black")
    v.circle(50, 40)

    v.penup()
    v.setposition(-50, 120)
    v.pendown()
    v.color("black")
    v.circle(50, 40)


tr1()

turtle.done()