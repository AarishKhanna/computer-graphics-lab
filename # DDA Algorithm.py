# Simple DDA Algorithm
from graphics import *


def dda():
    win = GraphWin('Simple_DDA', 1000, 1000)
    t = Text(Point(50, 50), 'Simple_DDA')
    t.draw(win)
    win.setCoords(-1000.0, -1000.0, 1000.0, 1000.0)
    # Draw vertical lines
    Line(Point(-1000, 0), Point(1000, 0)).draw(win)
    # Draw horizontal lines
    Line(Point(0, -1000), Point(0, 1000)).draw(win)
    win.setBackground("white")

    def dda2():
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
        if abs(dx) > abs(dy):
            len = abs(dx)
        else:
            len = abs(dy)
        xinc = (dx/float(len))
        yinc = (dy/float(len))
        pt = Point(ax, ay)
        pt.setOutline('blue')
        pt.draw(win)
        for i in range(int(len)):
            ax = ax+xinc
            ay = ay+yinc
            pt = Point(int(ax), int(ay))
            pt.setOutline('blue')
            pt.draw(win)
            print(int(ax), int(ay))
        dda2()
    dda2()
    win.getMouse()


dda()
