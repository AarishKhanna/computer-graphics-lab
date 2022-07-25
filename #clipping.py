# clipping
import math
from graphics import *
from collections import defaultdict as dd
import sys
import random


def liangBarsky(x1, y1, x2, y2, x_min, y_min, x_max, y_max):
    dx = x2-x1
    dy = y2-y1
    p1 = -dx
    p2 = dx
    p3 = -dy
    p4 = dy
    q1 = x1 - x_min
    q2 = x_max - x1
    q3 = y1 - y_min
    q4 = y_max - y1
    t1 = q1/p1
    t2 = q2/p2
    t3 = q3/p3
    t4 = q4/p4
    t_max = 0
    t_min = 1
    if(p1 == 0 or p2 == 0 or p3 == 0 or p4 == 0):
        print("line is parallel")
        print("\n")
    if(p1 != 0):
        if(p1 < 0):
            t_max = max(t_max, t1)
        elif(p1 > 0):
            t_min = min(t_min, t1)
    if(p2 != 0):
        if(p2 < 0):
            t_max = max(t_max, t2)
        elif(p2 > 0):
            t_min = min(t_min, t2)
    if(p3 != 0):
        if(p3 < 0):
            t_max = max(t_max, t3)
        elif(p3 > 0):
            t_min = min(t_min, t3)
    if(p4 != 0):
        if(p4 < 0):
            t_max = max(t_max, t4)
        elif(p4 > 0):
            t_min = min(t_min, t4)
    if(t_max > t_min):
        print("Line is completely outside")
        print("\n")
    if(t_max < t_min):
        x_1 = x1 + (t_max * dx)
        y_1 = y1 + (t_max * dy)
        x_2 = x1 + (t_min * dx)
        y_2 = y1 + (t_min * dy)
    print("Line will be accepted from (%.2f, %.2f) to (%.2f, %.2f)" %
          (x_1, y_1, x_2, y_2))
    return list(map(int, [x_1, y_1, x_2, y_2]))


class ViewPort:
    def __init__(self, xVmin, yVmin, xVmax, yVmax):
        self.xVmin, self.yVmin, self.xVmax, self.yVmax = xVmin, yVmin, xVmax, yVmax

    def __repr__(self):
        return 'ViewPort(%s, %s, %s, %s)' % (self.xVmin, self.yVmin, self.xVmax, self.yVmax)

    def init_view(self):

        win = GraphWin('Output Window', 800, 800)
        win.setBackground("orange")
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
    for x in range(dx + 1):
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


def drawLine(win, color='red', x1=-1, y1=-1, x2=-1, y2=-1):
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
sourceFile = open('demo4.txt', 'w')


def pointClip(Xmin, Ymin, Xmax, Ymax):
    points = []
    q1 = win.getMouse()
    q2 = win.getMouse()
    q3 = win.getMouse()
    q4 = win.getMouse()
    qx = int(q1.x)
    qy = int(q1.y)
    wx = int(q2.x)
    wy = int(q2.y)
    sx = int(q3.x)
    sy = int(q3.y)
    rx = int(q4.x)
    ry = int(q4.y)

    points.append((qx, qy))
    points.append((wx, wy))
    points.append((sx, sy))
    points.append((rx, ry))
    print(points, file=sourceFile)

    print("\n\nPoint inside the viewing pane:")
    for i in range(4):
        if ((points[i][0] > Xmin) and (points[i][0] < Xmax) and (points[i][1] > Ymin) and (points[i][1] < Ymax)):
            print("[", points[i][0], ", ", points[i][1],
                  "]", sep="", end=" ", file=sourceFile)
            pt1 = Point(points[i][0], points[i][1])
            pt1.draw(win)
    return points


def universal():

    def menu():
        win = GraphWin('Input Menu', 600, 300)
        win.setBackground("yellow")
        t = Text(Point(
            300, 50), 'Press A for Point Clipping and then S for same window for next, else N for new ')
        g = Text(Point(
            300, 100), 'Press B for line-barsky line clipping and then S for same window for next, else N for new')
        t.draw(win)
        g.draw(win)
        for i in range(2):

            textEntry = Entry(Point(233, 200), 50)
            textEntry.draw(win)

            win.getMouse()

            if i == 1:
                text2 = textEntry.getText()
            else:
                text = textEntry.getText()

        win.close()
        return text, text2

    def getpoints():
        points1 = []
        points2 = []
        p1 = win.getMouse()
        p1.draw(win)
        p2 = win.getMouse()
        p2.draw(win)
        p3 = win.getMouse()
        p3.draw(win)
        p4 = win.getMouse()
        p4.draw(win)

        ax = int(p1.x)
        ay = int(p1.y)
        bx = int(p2.x)
        by = int(p2.y)
        cx = int(p3.x)
        cy = int(p3.y)
        ex = int(p4.x)
        ey = int(p4.y)
        points1.append((ax))
        points1.append((bx))
        points1.append((cx))
        points1.append((ex))
        points2.append((ay))
        points2.append((by))
        points2.append((cy))
        points2.append((ey))
        return points1, points2

    points3, points4 = getpoints()
    vert = list(zip(points3, points4))
    print(vert, file=sourceFile)
    drawPoly(vert, win)
    text, text2 = menu()

    def decision(vert, points3, points4, text, text2):
        Xmin = min(points3)
        Ymin = min(points4)
        Xmax = max(points3)
        Ymax = max(points4)
        print(Xmin, Ymin, Xmax, Ymax, file=sourceFile)
        if text == "A":
            print("Point Clipping was done", file=sourceFile)
            drawAxis(win, new_view)
            result1 = pointClip(Xmin, Ymin, Xmax, Ymax)
        elif text == "B":
            print("Line Clipping was done", file=sourceFile)
            drawAxis(win, new_view)
            z1 = win.getMouse()
            z1.draw(win)
            z2 = win.getMouse()
            z2.draw(win)
            vx = int(z1.x)
            vy = int(z1.y)
            nx = int(z2.x)
            ny = int(z2.y)
            color = 'red'
            drawLine(win, color, vx, vy, nx, ny)
            temp = liangBarsky(vx, vy, nx, ny, Xmin, Ymin, Xmax, Ymax)
            print(temp, vx, vy, nx, ny, Xmin, Ymin,
                  Xmax, Ymax, file=sourceFile)
            pixel = bresenham(*temp)
            for i in pixel:
                x, y = i
                win.plot(*i, 'white')

        if text2 == "N":
            points3, points4 = getpoints()
            vert = list(zip(points3, points4))
            print(vert, file=sourceFile)
            drawPoly(vert, win)

        text, text2 = menu()
        decision(vert, points3, points4, text, text2)

    decision(vert, points3, points4, text, text2)
    sourceFile.close()


universal()
win.getMouse()
win.close()
