import turtle

r=turtle.Turtle()
t=turtle.Screen()
r.shape('triangle')
r.pensize(3)
r.speed(50)
def up():
  r.setheading(90)
  r.forward(10)

def down():
  r.setheading(270)
  r.forward(10)

def right():
  r.setheading(0)
  r.forward(10)

def left():
  r.setheading(180)
  r.forward(10)

t.onkey(up, 'w')
t.onkey(down, 's')
t.onkey(right, 'd')
t.onkey(left, 'a')

t.listen()
while True:
  t.update()

t.mainloop()

