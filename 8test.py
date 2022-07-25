from collections import defaultdict as dd
import sys,random
sys.setrecursionlimit(2*10**8)
from graphics import *
import math

class ViewPort:
    def __init__(self,xVmin,yVmin,xVmax,yVmax):
        self.xVmin,self.yVmin,self.xVmax,self.yVmax  =xVmin,yVmin,xVmax,yVmax
    def __repr__(self): 
        return 'ViewPort(%s, %s, %s, %s)' % (self.xVmin,self.yVmin,self.xVmax,self.yVmax) 
    def init_view(self):
        
        win = GraphWin('Drawing Window',600,600)
        win.setBackground("white")
        win.setCoords(self.xVmin,self.yVmin,self.xVmax,self.yVmax)
        t=Text(Point(0,0),'(0,0)')
        t.setSize(8)
        t.draw(win)
        t=Text(Point(self.xVmax,self.yVmax),'('+str(self.xVmax)+str(self.yVmax)+')')
        t.setSize(8)
        t.draw(win)
        L1 = Line(Point(self.xVmin,0),Point(self.xVmax,0))
        L2 = Line(Point(0,self.yVmin),Point(0,self.yVmax))
        L1.setFill('black')
        L2.setFill('black')
        L1.setArrow("last")
        L2.setArrow("last")
        L1.draw(win)
        L2.draw(win)
        return win
        
    
class Window:
    def __init__(self, xwmin,ywmin,xwmax,ywmax):
        self.xwmin,self.ywmin,self.xwmax,self.ywmax = xwmin,ywmin,xwmax,ywmax
    def __repr__(self): 
        return 'Window(%s, %s, %s, %s)' % (self.xwmin,self.ywmin,self.xwmax,self.ywmax) 
    def map_to(self,x_win,y_win,ViewPort):
                    x_view = (x_win-self.xwmin)*(ViewPort.xVmax - ViewPort.xVmin)/(self.xwmax-self.xwmin)  + ViewPort.xVmin
                    y_view = (y_win-self.ywmin)*(ViewPort.yVmax - ViewPort.yVmin)/(self.ywmax-self.ywmin)  + ViewPort.yVmin
                    return int(x_view),int(y_view)

def drawAxis(win,new_view):
    L1 = Line(Point(new_view.xVmin,0),Point(new_view.xVmax,0))
    L2 = Line(Point(0,new_view.yVmin),Point(0,new_view.yVmax))
    L1.setFill('black')
    L2.setFill('black')
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
    pixel=[]
    for x in range(dx + 1):
        pixel.append((x0 + x*xx + y*yx, y0 + x*xy + y*yy))
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy
    return pixel

def boundaryFill(pixel,stack,filled,win,fillColor='red2'):
	while(stack!=[]):		
			x,y=stack.pop()
			if((x,y) not in pixel and (x,y) not in filled):
				win.plot(x,y,color='blue')
				stack+=[(x+1,y),(x,y+1),(x,y-1),(x-1,y)]
		
				if((x+1,y) not in pixel) and ((x,y+1) not in pixel):
					stack.append((x+1,y+1))
					
				if((x+1,y) not in pixel) and ((x,y-1) not in pixel):
					stack.append((x+1,y-1))
					
				if((x-1,y) not in pixel) and ((x,y-1) not in pixel):
					stack.append((x-1,y-1))
					
				if((x-1,y) not in pixel) and ((x,y+1) not in pixel):
					stack.append((x-1,y+1))
				filled.append((x,y))

def Draw():
  vert = [] 
  new_view =ViewPort(-400,-400,400,400)	
  win = new_view.init_view()

  for i in range(4):
        x,y=map(int,input('Enter Next vert?').split())
        vert.append((x,y))
        print(x,y,i)
  pixel = []
  filled= []
  pixel_dict={}
  
  vert+=[vert[0]]
  for i in range(len(vert)-1):
        pixel+=bresenham(*vert[i],*vert[i+1])

  for i in pixel:
        x,y= i
        win.plot(*i)
        pixel_dict[(x,y)]=1
  point = win.getMouse()
  stack=[(int(point.getX()),int(point.getY()))]		
    
  boundaryFill(pixel_dict,stack,filled,win)	
  win.getMouse()
  win.close()

Draw()