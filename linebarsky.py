import math
from graphics import *
from collections import defaultdict as dd
import sys
import random
from drawLine import main

global t1, t2
t1 = 0
t2 = 1


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


def drawPoly(vertices, win, color='black'):
    vert = vertices.copy()
    vert += [vert[0]]
    for i in range(len(vert)-1):
        x1, y1, x2, y2 = *vert[i], *vert[i+1]
        # print(win,color,x1,y1,x2,y2)
        drawLine(win, color, x1, y1, x2, y2)


def isClip(p, q):
    global t1, t2
    flag = 1
    if p < 0:
        r = q / p
        if r > t2:
            flag = 0
        elif r > t1:
            t1 = r
    elif p > 0:
        r = q/p
        if r < t1:
            flag = 0
        else:
            t2 = r
    elif q < 0:
        flag = 0
    return flag


def clip(x1, y1, x2, y2, bxmin, bymin, bxmax, bymax):
    global t1, t2
    dx = x2 - x1
    if(isClip(-dx, y1-bymin)):
        if isClip(dx, bxmax-x1):
            dy = y2-y1
            if(isClip(-dy, y1-bymin)):
                if(isClip(dy, bymax-y1)):
                    if t2 < 1:
                        x2 = x1 + t2 * dx
                        y2 = y1 + t2 * dy
                    if t1 > 0:
                        x1 += t1 * dx
                        y1 += t1 * dy

    return list(map(int, [x1, y1, x2, y2]))


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
    for x in range(dx + 1):
        edge_points.append((x0 + x*xx + y*yx, y0 + x*xy + y*yy))
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy
    return edge_points


def drawLine(win, color='red', x1=-1, y1=-1, x2=-1, y2=-1):
    if x2 == x1 == -1:
        x1, y1, x2, y2 = map(int, input(
            'Enter Line\'s Endpoints <x1> <y1> <x2> <y2>  :').split())
    pixel = bresenham(x1, y1, x2, y2)
    for i in pixel:
        x, y = i
        win.plot(*i, color)
    return x1, y1, x2, y2


def main():
    new_view = ViewPort(-400, -400, 400, 400)
    print('ViewPort :', new_view)

    win = new_view.init_view()
    x, y, x1, y1 = drawLine(win)
    print(x,y,x1,y1)
    xmin, ymin, xmax, ymax = map(int, input(
        'Enter Cliping Window\'s Endpoints <xmin> <ymin> <xmax> <ymax>  :').split())
    drawPoly([(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)], win)
    temp = clip(x, y, x1, y1, xmin, ymin, xmax, ymax)
    print(temp, x, y, x1, y1, xmin, ymin, xmax, ymax)
    if not temp:
        return
    pixel = bresenham(*temp)
    for i in pixel:
        x, y = i
        win.plot(*i, 'green')
    input('Exit?')


if __name__ == '__main__':
    main()
