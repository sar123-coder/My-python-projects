import turtle
y=str(input('what color do you like(type in lower cases): '))
w=1
e=turtle.Screen()
e.bgcolor('black')
for i in range (40):
 r = turtle.Turtle()
 r.pensize('5')
 r.color(y)
 r.speed(50)
 r.circle(75)
 r.right(w)
 w=w+20
 r.circle(75)
