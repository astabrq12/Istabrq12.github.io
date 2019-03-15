import turtle
v = turtle.Turtle()
def cycle4():


    for n in range(0,2):
        for i in ["red", "purple", "hotpink", "blue","green"]:
         v.color(i)
         v.right(120)
         for n in range(0, 20):

            v.fd(40)
            v.right(100)
cycle4()
turtle.done()