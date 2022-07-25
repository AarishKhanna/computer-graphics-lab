# thicknesswithmath.py
from graphics import *
import math


def dda():
    win = GraphWin('Simple_DDA', 1000, 1000)
    win.setBackground("white")
    t = Text(Point(50, 50), 'Simple_DDA')
    t.draw(win)

    win.setCoords(-3000.0, -3000.0, 3000.0, 3000.0)
    # Draw vertical lines
    Line(Point(-3000, 0), Point(3000, 0)).draw(win)
    # Draw horizontal lines
    Line(Point(0, -3000), Point(0, 3000)).draw(win)

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
        m = dy/dx
        print(m)
        c = ay - (m)*ax
        print(c)

        t = 100

        if abs(dx) > abs(dy):
            len = abs(dx)
        else:
            len = abs(dy)

        xinc = (dx/float(len))
        yinc = (dy/float(len))

        pt = Point(ax, ay)
        pt.setOutline('blue')
        pt.draw(win)
        ax2 = ax
        ay2 = ay
        ax1 = ax
        ay1 = ay

        for i in range(int(len)):
            ax2 = ax2+xinc
            ay2 = ay2+yinc
            pt = Point(int(ax2), int(ay2))
            pt.setOutline('blue')
            pt.draw(win)
            print(int(ax2), int(ay2))

        print(ax1, ay1)
        for k in range(int(t)):
            c2 = c + k
            ay1 = ay + k
            ax1 = ax - (k/m)
            for j in range(int(len)):
                ax1 = ax1+xinc
                ay1 = ay1+yinc
                pt = Point(int(ax1), int(ay1))
                pt.setOutline('blue')
                pt.draw(win)
                print(int(ax1), int(ay1))

        dda2()

    dda2()

    win.getMouse()


dda()
