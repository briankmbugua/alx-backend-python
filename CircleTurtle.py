import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("white")

# while True:
#  for i in range(4):
#      t.forward(80)
#      t.right(90)
#  t.right(20)

a = 0
b = 0
while True:
    t.forward(a)
    t.right(b)
    a += 3
    b += 1
    if b == 210:
        break
t.hideturtle()

turtle.done()