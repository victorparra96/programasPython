import turtle

window = turtle.Screen()

colors=['red','white','red','white','red','white']

t = turtle.Pen()
t.speed(0)
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+2)
    t.forward(x)
    t.left(59)

turtle.mainloop()