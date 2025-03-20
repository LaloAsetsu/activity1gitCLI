"""Code of a game of paint in Python, in where is necesary to finish some activities"""
"""Autors: Eduardo Antonio Mora Hernandez & Emiliano López Torres"""
"""Date: 20/03/2025"""

from turtle import *
from freegames import vector
import math

def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle from start to end."""
    radius = math.sqrt((end.x - start.x) ** 2 + (end.y - start.y) ** 2)
    up()
    goto(start.x, start.y - radius)
    down()
    begin_fill()
    angle = 360 / 1000
    step = 2 * math.pi * radius / 1000
    for _ in range(1000):
        forward(step)
        left(angle)
    end_fill()


def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    width = end.x - start.x
    height = end.y - start.y

    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)

    end_fill()

    pass 


def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    base = end.x - start.x
    height = end.y - start.y

    forward(base)       
    left(120)           
    forward((base**2 + height**2)**0.5)  
    left(120)
    forward((base**2 + height**2)**0.5)  
    left(120)

    end_fill()

    pass


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
