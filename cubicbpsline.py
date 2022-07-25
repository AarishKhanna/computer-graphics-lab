import math
from types import NoneType
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




def universal():
    new_view = ViewPort(-400, -400, 400, 400)
    win = new_view.init_view()

    points3 = [None] * 1000
    points4 = [None] * 1000
    points5 = [None] * 1000
    points6 = [None] * 1000
    points7 = [None] * 1000
    points8 = [None] * 1000
    Total_points = 10
    Max_Steps = 100

    def Q0(u):
        return float(pow(u,2)/2)
    
    def Q1(u):
        return float(-1* pow(u,2) + u + 0.5)
    
    def Q2(u):
        return float(pow(1-u,2)/2)
    
    def L0(u):
        return float(u)
    
    def L1(u):
        return float(1-u)
    

    def C0(u):
        return float(pow(u, 3) / 6.0)

    def C1(u):
        return float((-3 * pow(u, 3) + 3 * pow(u, 2) + 3*u + 1) / 6.0)

    def C2(u):
        return float((3 * pow(u, 3) - 6 * pow(u, 2) + 4) / 6.0)

    def C3(u):
        return float((-1 * pow(u,3) + 3* pow(u,2) -  3*u + 1) / 6.0)

    
    def linearspline(x,y):
        count3 = 0
        for i in range(Total_points-1):
            for j in range(Max_Steps+1):
                u = j / Max_Steps
                Qx = L0(u)* x[i] + L1(u)* x[i + 1] 
                Qy = L0(u) * y[i] + L1(u) * y[i + 1] 
                #print(Qx,Qy)
                points7[count3] = Qx
                points8[count3] = Qy
                count3 = count3+1
        #print(count3)

    def quadbspline(x,y):
        count2 = 0
        for i in range(Total_points-2):
            for j in range(Max_Steps+1):
                u = j / Max_Steps
                Qx = Q0(u) * x[i] + Q1(u) * x[i + 1] + Q2(u) * x[i + 2] 
                Qy = Q0(u) * y[i] + Q1(u) * y[i + 1] + Q2(u) * y[i + 2] 
                #print(Qx,Qy)
                points5[count2] = Qx
                points6[count2] = Qy
                count2 = count2+1
        #print(count2)


    def calcbspline(x, y):
        count = 0
        for i in range(Total_points-3):
            for j in range(Max_Steps+1):
                u = j / Max_Steps
                Qx = C0(u) * x[i] + C1(u) * x[i + 1] + C2(u) * x[i + 2] + C3(u) * x[i + 3]
                Qy = C0(u) * y[i] + C1(u) * y[i + 1] + C2(u) * y[i + 2] + C3(u) * y[i + 3]
                #print(Qx,Qy)
                points3[count] = Qx
                points4[count] = Qy
                count = count+1
        #print(count)

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
        p5 = win.getMouse()
        p5.draw(win)
        p6 = win.getMouse()
        p6.draw(win)
        p7 = win.getMouse()
        p7.draw(win)
        p8 = win.getMouse()
        p8.draw(win)
        p9 = win.getMouse()
        p9.draw(win)
        p10 = win.getMouse()
        p10.draw(win)

        ax = int(p1.x)
        ay = int(p1.y)
        bx = int(p2.x)
        by = int(p2.y)
        cx = int(p3.x)
        cy = int(p3.y)
        ex = int(p4.x)
        ey = int(p4.y)
        sx = int(p5.x)
        sy = int(p5.y)
        fx = int(p6.x)
        fy = int(p6.y)
        tx = int(p7.x)
        ty = int(p7.y)
        ux = int(p8.x)
        uy = int(p8.y)
        ix = int(p9.x)
        iy = int(p9.y)
        ox = int(p10.x)
        oy = int(p10.y)

        points1.append((ax))
        points1.append((bx))
        points1.append((cx))
        points1.append((ex))
        points1.append((sx))
        points1.append((fx))
        points1.append((tx))
        points1.append((ux))
        points1.append((ix))
        points1.append((ox))
        points2.append((ay))
        points2.append((by))
        points2.append((cy))
        points2.append((ey))
        points2.append((sy))
        points2.append((fy))
        points2.append((ty))
        points2.append((uy))
        points2.append((iy))
        points2.append((oy))
        #print(points1,points2)
        return points1, points2

    
    def menu():
       win=GraphWin('Input Menu',500,300)
       win.setBackground("yellow")
       t=Text(Point(250,50),'YOU CAN IMPLEMENT 3 Curves: Linear, quadratic and cubic')
       g=Text(Point(250,100),'TYPE 1 FOR Linear, 2 FOR quadratic, 3 FOR cubic')
       h=Text(Point(250,150),'AND PRESS 1 FOR SAME SCREEN DRAWING AND 0 FOR UNDRAW FUNCTIONALITY') 
       t.draw(win)
       g.draw(win)
       h.draw(win)

       for i in range(2):
        
            textEntry = Entry(Point(233,200),50)
            textEntry.draw(win)

            win.getMouse()
            text = textEntry.getText() 
            
            if i == 1:
                text4 = text
            else:
                text3 = text 
            
       win.close()
       return text3, text4  

     
    

    def Draw(x, y):

        for i in range(706):
                qq = Line(Point(x[i], y[i]), Point(x[i+1], y[i+1]))
                qq.setOutline('blue')
                qq.draw(win)

        return
    
    def Draw2(x, y):

        for i in range(807):
                qq = Line(Point(x[i], y[i]), Point(x[i+1], y[i+1]))
                qq.setOutline('blue')
                qq.draw(win)

        return
    
    def Draw3(x, y):

        for i in range(908):
                qq = Line(Point(x[i], y[i]), Point(x[i+1], y[i+1]))
                qq.setOutline('blue')
                qq.draw(win)

        return



    
    text3, text4 = menu()
    def decision(text3,text4):
        if text3=="2":
            print("Quadratic")
            x,y = getpoints()
            quadbspline(x,y) 
            Draw2(points5, points6)

        elif text3 == "3":
            print("Cubic")
            x, y = getpoints()
            calcbspline(x, y)
            Draw(points3, points4)
        else:
            print("Linear")
            x,y = getpoints()
            linearspline(x,y) 
            Draw3(points7, points8)
        
        if text4 == "1":
            print("continued with same screen")
            text3, text4 = menu()
            decision(text3, text4)

        elif text4 == "0":
            print("Undraw functionality called")
            win.getMouse()
            win.close()
            universal()

    
    decision(text3, text4)





universal()

