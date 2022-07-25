# SymmetericalDDA.py
import math
from graphics import *


def dda():
    win = GraphWin('Symmeterical_DDA', 500, 500)
    t = Text(Point(50, 50), 'Symmeterical_DDA')
    t.draw(win)
    win.setBackground("white")

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    ax = p1.x
    ay = p1.y
    bx = p2.x
    by = p2.y
    print(ax, ay, bx, by)

    dx = bx-ax
    dy = by-ay
    print(dx, dy)
    n = (math.log10(max(dx, dy))) / math.log10(2)
    n = math.ceil(n)
    temp = pow(2, n)
    len = temp
    print(n)

    xinc = dx/temp
    yinc = dy/temp

    pt = Point(ax, ay)
    pt.setOutline('blue')
    pt.draw(win)

    for i in range(int(len)):
        ax = ax+xinc
        ay = ay+yinc
        pt = Point(round(ax), round(ay))
        pt.setOutline('blue')
        pt.draw(win)
        print(round(ax), round(ay))

    win.getMouse()


dda()
