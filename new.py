import turtle
v=turtle.Turtle()
v.speed(25)
def cycle1(x,y,z):
 v.hideturtle()
 turtle.bgcolor("pink")

 v.lt(x)
 v.fd(y)

 v.rt(90)

 v.color(z)
 v.circle(50)
 v.pencolor("red")
 v.home()

v.begin_fill()
cycle1(120,50,"red")
v.end_fill()
v.begin_fill()
cycle1(70,50,"green")
v.end_fill()
v.begin_fill()
cycle1(80,160,"blue")
v.end_fill()
v.begin_fill()
cycle1(105,210,"yellow")
v.end_fill()
turtle.done()
