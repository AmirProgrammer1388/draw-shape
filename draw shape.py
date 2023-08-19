import turtle as t
t.speed("fast")
t.shape("turtle")
t.color("red")
t.width(3)
x=int(t.textinput("draw","Polygon ?"))
y=int(t.textinput("draw","How many times should I repeat?"))
r=int(t.textinput("draw","Rotation angle?"))
for j in range(y):
    for i in range(x):
        t.forward(100)
        t.lt(360/x)
    t.lt(r)
t.penup()
t.goto(-60,-300)
t.pendown()
t.hideturtle()
