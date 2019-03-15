import turtle
v=turtle.Turtle()
def tran():
    for n in range(4):
        v.shape("turtle")
        v.right(90)
        v.backward(90)

    v.left(65)
    v.fd(100)
    v.right(127)
    v.fd(100)
tran()
turtle.done()