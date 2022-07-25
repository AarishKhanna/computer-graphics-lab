# transformations
import math
from graphics import *
from collections import defaultdict as dd
import sys
import random


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


def drawLine(win, color='pink', x1=-1, y1=-1, x2=-1, y2=-1):
    if x2 == x1 == -1:
        x1, y1, x2, y2 = map(int, input(
            'Enter Line\'s Endpoints <x1> <y1> <x2> <y2>  :').split())
    pixel = bresenham(x1, y1, x2, y2)
    for i in pixel:
        x, y = i
        win.plot(*i, color)
    return x1, y1, x2, y2


def translation(vert, x, y, win):
    #if f:input("translate by"+str(x)+str(y))
    #vert = [i+[1] for i in vert]
    print(vert)

    # Translation matrix
    trans = [[1, 0, 0], [0, 1, 0], [-x, -y, 1]]

    result = [[int(sum(a*b for a, b in zip(A_row, B_col)))
               for B_col in zip(*trans)] for A_row in vert]
    result = [i[:-1] for i in result]
    print(result)

    # drawPoly(result,win,'blue')

    return result


def rotation(vert, x, y, angle, win):
    vert = translation(vert, x, y, win)
    vert = only_rotation(vert, x, y, angle, win)
    result = translation(vert, -x, -y, win)
    return result


def only_rotation(vert, x, y, angle, win):
    #input("Rotate at"+str(x)+str(y)+" by"+str(angle)+"?")

    angle = (math.pi*angle/180)
    #vert = [i+[1] for i in vert]

    # Rotation matrix
    trans = [[math.cos(angle), math.sin(angle), 0],
             [-math.sin(angle), math.cos(angle), 0], [0, 0, 1]]

    result = [[int(sum(a*b for a, b in zip(A_row, B_col)))
               for B_col in zip(*trans)] for A_row in vert]
    result = [i[:-1] for i in result]

    # drawPoly(result,win,'green2')
    return result


def scale(vert, x, y, sx, sy, win):
    vert = translation(vert, x, y, win)
    result = only_scale(vert, x, y, sx, sy, win)
    result = translation(result, -x, -y, win)
    return result


def only_scale(vert, x, y, sx, sy, win):
    #input("Scale at "+str(x)+str(y)+" by"+str(sx)+str(sy)+"?")

    #vert = [i+[1] for i in vert]

    # Scale matrix
    trans = [[sx, 0, 0], [0, sy, 0], [0, 0, 1]]

    result = [[int(sum(a*b for a, b in zip(A_row, B_col)))
               for B_col in zip(*trans)] for A_row in vert]
    result = [i[:-1] for i in result]

    # drawPoly(result,win,'red2')

    return result


def reflection(vert, x, y, angle, win):
    vert = translation(vert, x, y, win)
    vert = only_rotation(vert, x, y, angle, win)

    #vert = [i+[1] for i in vert]

    # Reflection matrix
    trans = [[-1, 0, 0], [0, 1, 0], [0, 0, 1]]

    result = [[int(sum(a*b for a, b in zip(A_row, B_col)))
               for B_col in zip(*trans)] for A_row in vert]
    result = [i[:-1] for i in result]

    # drawPoly(result,win,'green2')
    result = only_rotation(result, x, y, -angle, win)
    result = translation(result, -x, -y, win)
    return result


def shear_x(vert, shx, win):
    #vert = [i+[1] for i in vert]

    # Shear matrix
    trans = [[1, 0, 0], [shx, 1, 0], [0, 0, 1]]
    result = [[int(sum(a*b for a, b in zip(A_row, B_col)))
               for B_col in zip(*trans)] for A_row in vert]
    result = [i[:-1] for i in result]
    return result


def shear_y(vert, shy, win):
   # vert = [i+[1] for i in vert]

    # Shear matrix
    trans = [[1, shy, 0], [0, 1, 0], [0, 0, 1]]
    result = [[int(sum(a*b for a, b in zip(A_row, B_col)))
               for B_col in zip(*trans)] for A_row in vert]
    result = [i[:-1] for i in result]
    return result


def universal():
    sourceFile = open('demo2.txt', 'w')

    def menu():
        win = GraphWin('Input Menu', 600, 300)
        win.setBackground("yellow")
        t = Text(Point(
            300, 50), 'Press UP, LEFT, RIGHT, DOWN KEY FOR TRANSLATION')
        g = Text(Point(
            300, 100), 'PRESS R, r FOR ROTATION, F, f FOR REFLECTION ')
        h = Text(Point(
            300, 150), 'PRESS X,x,Y,y FOR SHEAR, S,s FOR SCALING')
        j = Text(Point(
            300, 200), '1 FOR SAME CANVAS DRAWING AND 0 TO UNDRAW')
        t.draw(win)
        g.draw(win)
        h.draw(win)
        j.draw(win)

    menu()
    new_view = ViewPort(-400, -400, 400, 400)
    win = new_view.init_view()

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
        points1.append((ax, ay))
        points1.append((bx, by))
        points1.append((cx, cy))
        points1.append((ex, ey))
        points2.append((ax, ay, 1))
        points2.append((bx, by, 1))
        points2.append((cx, cy, 1))
        points2.append((ex, ey, 1))
        return points1, points2

    vert, points3 = getpoints()
    print(vert, file=sourceFile)
    drawPoly(vert, win)

    def decision(vert, points3):
        while 1:
            k = win.getKey()
            if k == "Left":
                print("Translated left", file=sourceFile)
                drawPoly(vert, win, color_rgb(44, 44, 44))
                drawAxis(win, new_view)
                vert = translation(points3, 10, 0, win)
                drawPoly(vert, win, "red")
            elif k == "Right":
                print("Translated right", file=sourceFile)
                drawPoly(vert, win, color_rgb(44, 44, 44))
                drawAxis(win, new_view)
                vert = translation(points3, -10, 0, win)
                drawPoly(vert, win, "red")
            elif k == "Up":
                print("Translated up", file=sourceFile)
                drawPoly(vert, win, color_rgb(44, 44, 44))
                drawAxis(win, new_view)
                vert = translation(points3, 0, -10, win)
                drawPoly(vert, win, "red")
            elif k == "Down":
                print("Translated down", file=sourceFile)
                drawPoly(vert, win, color_rgb(44, 44, 44))
                drawAxis(win, new_view)
                vert = translation(points3, 0, 10, win)
                drawPoly(vert, win, "red")
            elif k == "s":
                print("Scaled by factor 2,2", file=sourceFile)
                drawPoly(vert, win, color_rgb(44, 44, 44))
                drawAxis(win, new_view)
                vert = scale(points3, 0, 0, 2, 2, win)
                drawPoly(vert, win, "red")
            elif k == "S":
                print("Scaled by factor 0.5,0.5", file=sourceFile)
                drawPoly(vert, win, color_rgb(44, 44, 44))
                drawAxis(win, new_view)
                vert = scale(points3, 0, 0, 0.5, 0.5, win)
                drawPoly(vert, win, "red")
            elif k == "r":
                print("Rotated anticlockwise", file=sourceFile)
                drawPoly(vert, win, color_rgb(44, 44, 44))
                drawAxis(win, new_view)
                vert = rotation(points3, 0, 0, 15, win)
                drawPoly(vert, win, "red")
            elif k == "R":
                print("Rotated clockwise", file=sourceFile)
                drawPoly(vert, win, color_rgb(44, 44, 44))
                drawAxis(win, new_view)
                vert = rotation(points3, 0, 0, -15, win)
                drawPoly(vert, win, "red")
            elif k == "f":
                print("Reflected Anticlockwise", file=sourceFile)
                drawPoly(vert, win, color_rgb(44, 44, 44))
                drawAxis(win, new_view)
                vert = reflection(points3, 0, 0, 45, win)
                drawPoly(vert, win, "red")
            elif k == "F":
                print("Reflected Clockwise", file=sourceFile)
                drawPoly(vert, win, color_rgb(44, 44, 44))
                drawAxis(win, new_view)
                vert = reflection(points3, 0, 0, -45, win)
                drawPoly(vert, win, "red")
            elif k == "x":
                print("Sheared by 1 in x direction", file=sourceFile)
                drawPoly(vert, win, color_rgb(44, 44, 44))
                drawAxis(win, new_view)
                vert = shear_x(points3, 1, win)
                drawPoly(vert, win, "red")
            elif k == "X":
                print("Sheared by -1 in x direction", file=sourceFile)
                drawPoly(vert, win, color_rgb(44, 44, 44))
                drawAxis(win, new_view)
                vert = shear_x(points3, -1, win)
                drawPoly(vert, win, "red")
            elif k == "y":
                print("Sheared by 1 in y direction", file=sourceFile)
                drawPoly(vert, win, color_rgb(44, 44, 44))
                drawAxis(win, new_view)
                vert = shear_y(points3, 1, win)
                drawPoly(vert, win, "red")
            elif k == "Y":
                print("Sheared by -1 in y direction", file=sourceFile)
                drawPoly(vert, win, color_rgb(44, 44, 44))
                drawAxis(win, new_view)
                vert = shear_y(points3, -1, win)
                drawPoly(vert, win, "red")
            else:
                break

    decision(vert, points3)
    sourceFile.close()


universal()
