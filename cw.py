import turtle
m=turtle.Turtle()
color=['red','green','yellow','blue']
for i in range(100):
    m.color(color[i%4])
    m.forward(i)
    m.right(90)

turtle.done()