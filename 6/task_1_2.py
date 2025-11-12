from turtle import *

shape('turtle')
color('green')
left(90)
zoom = 50
speed(30)
tracer(0)
screensize(2500, 2500)

for i in range(7):
    forward(10*zoom)
    right(120)

# создание точек
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*zoom, y*zoom)
        dot(5, 'red')

done()