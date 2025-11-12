from turtle import *

shape('turtle')
color('green')
left(90)
zoom = 30
speed(30)
tracer(0)
screensize(2400, 2400)

for i in range(7):
    forward(10*zoom)
    right(120)

# Построение точек
up()
for x in range(9):
    for y in range(11):
        goto(x*zoom, y*zoom)
        dot(5, 'red')

done()