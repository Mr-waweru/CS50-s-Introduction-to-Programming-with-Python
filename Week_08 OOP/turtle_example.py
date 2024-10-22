from turtle import *

# t1 = Turtle()
# t2 = Turtle()

# t1.color("orange")
# t2.color("purple")

# t1.forward(50)
# t1.left(90)

# t2.left(90)
# t2.forward(50)

# done()

t1 = Turtle()
t1.color("blue")
t1.width(5)

t1.begin_fill()
for i in range(5):
    t1.forward(150)
    t1.left(144)
t1.end_fill()

done()