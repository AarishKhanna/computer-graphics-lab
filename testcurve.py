# beizercurve.py
import math
from graphics import *
from collections import defaultdict as dd
import sys
import random
sys.setrecursionlimit(2*10**8)


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
    pixel = []
    for x in range(dx + 1):
        pixel.append((x0 + x*xx + y*yx, y0 + x*xy + y*yy))
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy
    return pixel


new_view = ViewPort(-400, -400, 400, 400)
win = new_view.init_view()


def universal():
    def getValue(x1, x2, t):
        return x1+(x2-x1)*t

    def getpoints():
        points1 = []
        points2 = []
        p1 = win.getMouse()
        p1.draw(win)
        t = Text(p1, 'P1')
        t.draw(win)
        p2 = win.getMouse()
        e = Text(p2, 'P2')
        e.draw(win)
        p2.draw(win)
        p3 = win.getMouse()
        r = Text(p3, 'P3')
        r.draw(win)
        p3.draw(win)
        p4 = win.getMouse()
        u = Text(p4, 'P4')
        u.draw(win)
        p4.draw(win)
        #p5 = win.getMouse()
        # p5.draw(win)

        ax = int(p1.x)
        ay = int(p1.y)
        bx = int(p2.x)
        by = int(p2.y)
        cx = int(p3.x)
        cy = int(p3.y)
        ex = int(p4.x)
        ey = int(p4.y)
        #sx = int(p5.x)
        #sy = int(p5.y)
        points1.append((ax))
        points1.append((bx))
        points1.append((cx))
        points1.append((ex))
        # points1.append((sx))
        points2.append((ay))
        points2.append((by))
        points2.append((cy))
        points2.append((ey))
        # points2.append((sy))
        return points1, points2

    def Draw(x, y, num):
        if num == 3:
            x0 = getValue(x[0], x[1], i / cnt)
            y0 = getValue(y[0], y[1], i / cnt)
            x1 = getValue(x[1], x[2], i / cnt)
            y1 = getValue(y[1], y[2], i / cnt)
          #  pt = Line(Point(x0,y0), Point(x1,y1))
           # pt.setOutline('pink')
          #  pt.draw(win)
            xLast.append(getValue(x0, x1, i / cnt))
            yLast.append(getValue(y0, y1, i / cnt))
            py = Point(xLast[i], yLast[i])
            print(xLast[i], yLast[i])
            o = Text(py, '*')
            o.draw(win)
           # f=Text(py,'X')
            #f.draw(win)
         #   b=Text(py,'#')
          #  b.draw(win)
          
          #  py.setOutline('black')
          #  py.draw(win)
        else:
            xNext = []
            yNext = []
            for j in range(num-1):
                xNext.append(getValue(x[j], x[j + 1], i / cnt))
                yNext.append(getValue(y[j], y[j + 1], i / cnt))
                pz = Point(xNext[j], yNext[j])
                if j == 0:
                    continue
                else:
                    pe = Point(xNext[j-1], yNext[j-1])
                 #   pw = Line(pz, pe)
                #    pw.setOutline('pink')
                 #   pw.draw(win)

            qq = Line(Point(x[1], y[1]), Point(x[2], y[2]))
            qq.setOutline('blue')
            qq.draw(win)
            qa = Line(Point(x[0], y[0]), Point(x[1], y[1]))
            qa.setOutline('blue')
            qa.draw(win)
            qz = Line(Point(x[2], y[2]), Point(x[3], y[3]))
            qz.setOutline('blue')
            qz.draw(win)
            Draw(xNext, yNext, num-1)
        return

    xLast = []
    yLast = []
    cnt = 50
    x, y = getpoints()
    for i in range(cnt+1):
        Draw(x, y, len(x))


universal()
win.getMouse()
win.close()
