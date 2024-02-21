from turtle import *
from colorsys import *

bgcolor('black')
tracer(2)
pensize(2)
h = 0
for i in range(500):
    c = hsv_to_rgb(h,1,1)
    h += 0.005
    color(c)
    up()
    goto(-8,25)
    down()
    fd(i)
    rt(89)
    fillcolor(c)
    begin_fill()
    circle(90,100)
    end_fill()
    lt(100)
    bk(i/2)
    lt(6)
done()