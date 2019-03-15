import turtle
t=turtle.Turtle()
colors=[ "green","red","purple" ,"blue"]
t.pensize(10)
def draw_square():
    for x in range(300):
        t.pencolor(colors[x%4])
        t.width(x/100+1)
        t.forward(x)

        t.left(59)
draw_square()
turtle.done()