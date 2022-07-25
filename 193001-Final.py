import math
from graphics import *
from collections import defaultdict as dd
import numpy as np


class ViewPort:
    def __init__(self, xVmin, yVmin, xVmax, yVmax):
        self.xVmin, self.yVmin, self.xVmax, self.yVmax = xVmin, yVmin, xVmax, yVmax

    def __repr__(self):
        return 'ViewPort(%s, %s, %s, %s)' % (self.xVmin, self.yVmin, self.xVmax, self.yVmax)

    def init_view(self):

        win = GraphWin('Output Window', 800, 800)
        win.setBackground("white")
        win.setCoords(self.xVmin, self.yVmin, self.xVmax, self.yVmax)
        t = Text(Point(0, 0), '(0,0)')
        t.setSize(8)
        t.draw(win)
        t = Text(Point(self.xVmax, self.yVmax),
                 '('+str(self.xVmax)+str(self.yVmax)+')')
        t.setSize(8)
        t.draw(win)
        L1 = Line(Point(self.xVmin, 0), Point(self.xVmax, 0))
        L2 = Line(Point(0, self.yVmin), Point(0, self.yVmax))
        L1.setFill('blue')
        L2.setFill('blue')
        L1.setArrow("last")
        L2.setArrow("last")
        L1.draw(win)
        L2.draw(win)
        return win


class Window:
    def __init__(self, xwmin, ywmin, xwmax, ywmax):
        self.xwmin, self.ywmin, self.xwmax, self.ywmax = xwmin, ywmin, xwmax, ywmax

    def __repr__(self):
        return 'Window(%s, %s, %s, %s)' % (self.xwmin, self.ywmin, self.xwmax, self.ywmax)

    def map_to(self, x_win, y_win, ViewPort):
        x_view = (x_win-self.xwmin)*(ViewPort.xVmax - ViewPort.xVmin) / \
            (self.xwmax-self.xwmin) + ViewPort.xVmin
        y_view = (y_win-self.ywmin)*(ViewPort.yVmax - ViewPort.yVmin) / \
            (self.ywmax-self.ywmin) + ViewPort.yVmin
        return int(x_view), int(y_view)


def drawAxis(win, new_view):
    L1 = Line(Point(new_view.xVmin, 0), Point(new_view.xVmax, 0))
    L2 = Line(Point(0, new_view.yVmin), Point(0, new_view.yVmax))
    L1.setFill('blue')
    L2.setFill('blue')
    L1.draw(win)
    L2.draw(win)
    return win


def bresenham(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2*dy - dx
    y = 0
    edge_points = []
    for x in range(int(dx + 1)):
        edge_points.append((x0 + x*xx + y*yx, y0 + x*xy + y*yy))
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy
    return edge_points


def drawPoly(vertices, win, color='black'):
    vert = vertices.copy()
    vert += [vert[0]]
    for i in range(len(vert)-1):
        x1, y1, x2, y2 = *vert[i], *vert[i+1]
        # print(win,color,x1,y1,x2,y2)
        drawLine(win, color, x1, y1, x2, y2)


def drawLine(win, color='pink', x1=-1, y1=-1, x2=-1, y2=-1):

    if x2 == x1 == -1:
        x1, y1, x2, y2 = map(int, input(
            'Enter Line\'s Endpoints <x1> <y1> <x2> <y2>  :').split())
    pixel = bresenham(x1, y1, x2, y2)
    for i in pixel:
        x, y = i
        win.plot(*i, color)
    return x1, y1, x2, y2


new_view = ViewPort(-400, -400, 400, 400)
win = new_view.init_view()


def main():

    def incrementpoints(x, y, ang):
        th = math.pi * ang / 180

        # rotating by radian th
        a = np.matrix([[math.cos(th), math.sin(th), 0],
                      [-math.sin(th), math.cos(th), 0], [0, 0, 1]])
        b = np.matrix([x, y, 1]).T

        final = np.matmul(a, b)
        return final[0, 0], final[1, 0]

    def pointsfun():
        n = int(input("Number of edges of polygon"))
        r = int(input("Final radius of polygon"))
        desiredcircle = Circle(Point(0, 0), r)

        k = 5
        for j in range(0, r, 2):
            desiredcircle = Circle(Point(0, 0), j)
            desiredcircle.setFill('pink')

           
            points1 = []
            points2 = []

            for i in range(0, n):
                # initial points
                ax = (j * (math.cos(2*(math.pi*(i/n)))))
                ay = (j * (math.sin(2*(math.pi*(i/n)))))

                bx, by = incrementpoints(ax, ay, k)
                points2.append(Point(bx, by))

            k = k+3  # incrementing k so that polygon is rotated
            p5 = Polygon(points2).draw(win)

    pointsfun()


main()
win.getMouse()
win.close()