import math
from graphics import *
from collections import defaultdict as dd
#import sys
#import random

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
    for x in range (int(dx + 1)):
        edge_points.append((x0 + x*xx + y*yx, y0 + x*xy + y*yy))
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy
    return edge_points

def drawPoly(vertices,win,color='black'):
	vert = vertices.copy()
	vert+=[vert[0]]
	for i in range(len(vert)-1):
		x1,y1,x2,y2 = *vert[i],*vert[i+1]
		#print(win,color,x1,y1,x2,y2)
		drawLine(win,color,x1,y1,x2,y2)

def drawLine(win,color='pink',x1=-1,y1=-1,x2=-1,y2=-1):

	if x2==x1==-1:
		x1,y1,x2,y2 = map(int,input('Enter Line\'s Endpoints <x1> <y1> <x2> <y2>  :').split())
	pixel=bresenham(x1,y1,x2,y2)
	for i in pixel:
		x,y= i
		win.plot(*i,color)
	return x1,y1,x2,y2

new_view = ViewPort(-400, -400, 400, 400)
win = new_view.init_view()

def main():
   

    def pointsfun():
        n = int(input("Number of edges of polygon"))
        r = int(input("Final radius of polygon"))
        desiredcircle = Circle(Point(0,0),r)
        #circ.draw(win)

        points1 = []
        for j in range (0,r,5):
            desiredcircle = Circle(Point(0,0),j)
            desiredcircle.setFill('pink')

            #desiredcircle.draw(win)
            k=0

            for i in range (0,n):
                    ax = j * (math.cos(2*math.pi*(i/n+k)))
                    ay = j * (math.sin(2*math.pi*(i/n+k)))
                    points1.append((ax, ay))
                    #p = Polygon(points1).draw(win)
                    drawPoly(points1,win,color_rgb(44,44,44))
                    drawAxis(win,new_view)
                    k=k+5

            #for q in range (0,n):
                        #for m in range (0,n):
                            #x1,y1,x2,y2 = *points1[q],*points1[m]
                            #color = 'pink'
                            #drawLine(win,color,x1,y1,x2,y2)



       
        return points1, n,r
    
    
    pointsfun()


    
            
    
    

main()
win.getMouse()
win.close()

