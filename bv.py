import turtle
v = turtle.Turtle()
def tr(x):
    con=["red","yellow","green","pink"]
    for i in range(4):
        v.color(con[i%4])
        v.forward(x)
        v.left(90)

tr(100)
turtle.done()