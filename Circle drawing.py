# Mid-Point Circle Drawing Algorithm
from graphics import *
import time
import math


def midPointCircleDraw():
    win = GraphWin('Circle Drawing', 1000, 1000)
    t = Text(Point(50, 50), 'Circle Drawing')
    t.draw(win)
    win.setBackground("white")

    win.setCoords(-3000.0, -3000.0, 3000.0, 3000.0)
    # Draw vertical lines
    Line(Point(-3000, 0), Point(3000, 0)).draw(win)
    # Draw horizontal lines
    Line(Point(0, -3000), Point(0, 3000)).draw(win)

    def midPointCircleDraw2():
        p1 = win.getMouse()
        p1.draw(win)
        p2 = win.getMouse()
        p2.draw(win)
        ax = p1.x
        ay = p1.y
        bx = p2.x
        by = p2.y

        temp1 = bx-ax
        temp1 = temp1*temp1
        temp2 = by - ay
        temp2 = temp2*temp2

        r = temp1+temp2
        r = math.sqrt(r)
        x_centre = ax
        y_centre = ay

        x = r
        y = 0

        P = 1 - r

        while x > y:

            y += 1

            if P <= 0:
                P = P + 2 * y + 1

            else:
                x -= 1
                P = P + 2 * y - 2 * x + 1

            if (x < y):
                break

            x1 = x + x_centre
            y1 = y + y_centre

            x2 = -x + x_centre
            y2 = y + y_centre

            x3 = x + x_centre
            y3 = -y + y_centre

            x4 = -x + x_centre
            y4 = -y + y_centre
            PutPixle(win, x1, y1)
            PutPixle(win, x2, y2)
            PutPixle(win, x3, y3)
            PutPixle(win, x4, y4)

            if x != y:
                x1 = y + x_centre
                y1 = x + y_centre

                x2 = -y + x_centre
                y2 = x + y_centre

                x3 = y + x_centre
                y3 = -x + y_centre

                x4 = -y + x_centre
                y4 = -x + y_centre

                PutPixle(win, x1, y1)
                PutPixle(win, x2, y2)
                PutPixle(win, x3, y3)
                PutPixle(win, x4, y4)

        midPointCircleDraw2()

    midPointCircleDraw2()
    win.getMouse()
    win.close()


def PutPixle(win, x, y):
    pt = Point(x, y)
    pt.draw(win)


midPointCircleDraw()
