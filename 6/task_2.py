from turtle import *

shape('turtle')
color('green')
left(90)
zoom = 30
speed(30)
tracer(0)
screensize(2400, 2400)

for i in range(2):
    forward(8*zoom)
    right(90)
    forward(18*zoom)
    right(90)

up()
forward(4*zoom)
right(90)
forward(10*zoom)
left(90)

down()
for i in range(2):
    forward(17*zoom)
    right(90)
    forward(7*zoom)
    right(90)

# Построение точек
up()
for x in range(19):
    for y in range(22):
        goto(x*zoom, y*zoom)
        dot(5, 'red')

print(19*22 - 11*13)
done()