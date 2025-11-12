from turtle import *

shape('turtle')
color('green')
left(90)
zoom = 30
speed(30)
tracer(0)
screensize(2500, 2500)

for i in range(9):
    forward(22*zoom)
    right(90)
    forward(6*zoom)
    right(90)

up()
forward(1*zoom)
right(90)
forward(5*zoom)
left(90)

down()
for i in range(9):
    forward(53*zoom)
    right(90)
    forward(75*zoom)
    right(90)

# создание точек
up()
for x in range(2):
    for y in range(22):
        goto(x*zoom, y*zoom)
        dot(5, 'red')
print(19*22 - 11*13)
done()