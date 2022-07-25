#Filling_algos
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
        
        win = GraphWin('Output Window',800,800)
        win.setBackground("orange")
        win.setCoords(self.xVmin,self.yVmin,self.xVmax,self.yVmax)
        t=Text(Point(0,0),'(0,0)')
        t.setSize(8)
        t.draw(win)
        t=Text(Point(self.xVmax,self.yVmax),'('+str(self.xVmax)+str(self.yVmax)+')')
        t.setSize(8)
        t.draw(win)
        L1 = Line(Point(self.xVmin,0),Point(self.xVmax,0))
        L2 = Line(Point(0,self.yVmin),Point(0,self.yVmax))
        L1.setFill('blue')
        L2.setFill('blue')
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
    L1.setFill('blue')
    L2.setFill('blue')
    L1.draw(win)
    L2.draw(win)
    return win

def scanLine(edge_table,y_min,y_max,win,color="rand"):
    active_edge = []
    for curr_y in range(y_min,y_max+1):
        i=0
        #Del used
        while i<len(active_edge):
            if active_edge[i][2]==curr_y:
                active_edge.pop(i)
            else:
                i+=1
        #update x
        for e in range(len(active_edge)):
            if e%2: active_edge[e][1]+=active_edge[e][3];active_edge[e][0]=math.floor(active_edge[e][1]);
            else:	 active_edge[e][1]+=active_edge[e][3];active_edge[e][0]=math.ceil(active_edge[e][1]);
        #Add New
        active_edge+=edge_table[curr_y]
        active_edge.sort()
        #print(active_edge)
        #Fill all
        for cur in range(0,len(active_edge)-1,2):
            for x in range(active_edge[cur][0],active_edge[cur+1][0]+1):
                if color=="rand":
                    r=random.randint(0,255)
                    g=random.randint(0,255)
                    b=random.randint(0,255)
                    win.plot(x,curr_y,color=color_rgb(r,g,b))
                else:
                    win.plot(x,curr_y,color)


def boundary8Fill(pixel,stack,filled,win,fillColor='red2'):
    while(stack!=[]):		
            x,y=stack.pop()
            if((x,y) not in pixel and (x,y) not in filled):
                r=random.randint(0,255)
                g=random.randint(0,255)
                b=random.randint(0,255)
                win.plot(x,y,color=color_rgb(r,g,b))
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


def boundary4Fill(pixel,stack,filled,win,fillColor='red2'):

        while(stack!=[]):		
            x,y=stack.pop()
            if((x,y) not in pixel and (x,y) not in filled):
                r=random.randint(0,255)
                g=random.randint(0,255)
                b=random.randint(0,255)
                win.plot(x,y,color=color_rgb(r,g,b))
                stack+=[(x+1,y),(x,y+1),(x,y-1),(x-1,y)]
                filled.append((x,y))


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
 

def Universalfunc():
  new_view =ViewPort(-400,-400,400,400)	
  win = new_view.init_view()

  def getvert():
        vert = []
        p1=win.getMouse()
        p1.draw(win)
        p2=win.getMouse()
        p2.draw(win)
        p3=win.getMouse()
        p3.draw(win)
        p4=win.getMouse()
        p4.draw(win)

        ax=int(p1.x)
        ay=int(p1.y)
        bx=int(p2.x)
        by=int(p2.y)
        cx=int(p3.x)
        cy=int(p3.y)
        ex=int(p4.x)
        ey=int(p4.y)
        vert.append((ax,ay))
        vert.append((bx,by))
        vert.append((cx,cy))
        vert.append((ex,ey))
        return vert

  def menu():
       win=GraphWin('Input Menu',600,300)
       win.setBackground("yellow")
       t=Text(Point(300,50),'YOU CAN IMPLEMENT 3 ALGOS: GIVE 4 CLICKS ON MAIN WINDOW TO GIVE POLYGON VERTICES')
       g=Text(Point(300,100),'AND THEN TYPE 1 FOR 4-FILL ALGO 2 FOR 8-FILL ALGO AND 3 FOR SCAN-FILL ALGO')
       h=Text(Point(300,150),'AND PRESS 1 FOR SAME SCREEN DRAWING AND 0 FOR UNDRAW FUNCTIONALITY') 
       t.draw(win)
       g.draw(win)
       h.draw(win)

       for i in range(2):
        
            textEntry = Entry(Point(250,200),50)
            textEntry.draw(win)

            win.getMouse()
            text = textEntry.getText() 
            
            if i == 0:
                text3 = text
            elif i == 1:
                text4 = text 

       win.close()
       return text3, text4  

     
  text3, text4 = menu()
  vert = getvert()

  def decision(text3, text4, vert):
        pixel = []
        filled= []
        pixel_dict={}
        vert+=[vert[0]]
        print(vert)

        edge_table =dd(list)
        for i in range((len(vert)-1)):
                #Edge table
                x,y,x1,y1 =*vert[i],*vert[i+1]
                if y>y1:
                    x,y,x1,y1 =x1,y1,x,y 
                if y==y1:
                    continue
                if x1==x:
                    slope_inv = 0
                else:	
                    slope_inv = (x1-x)/(y1-y)
                        
                edge_table[y].append([x,x,y1,slope_inv])
                #edge_table.sort()

        y_max = max(v[1] for v in vert)
        y_min = min(v[1] for v in vert)
            
        for i in range(len(vert)-1):
                pixel+=bresenham(*vert[i],*vert[i+1])

        for i in pixel:
                x,y= i
                win.plot(*i)
                pixel_dict[(x,y)]=1
        point = win.getMouse()
        stack=[(int(point.getX()),int(point.getY()))]	
        if text3 == "1":
            print("4fill called")
            boundary4Fill(pixel_dict,stack,filled,win)
            
        elif text3 == "2": 
            print("8 fill called")
            boundary8Fill(pixel_dict,stack,filled,win)

        elif text3 == "3":
            print("scanfill called")
            scanLine(edge_table,y_min,y_max,win)

        if text4 == "1":
            print("continued with same screen")
            text3, text4 = menu()
            vert = getvert()
            decision(text3, text4, vert)

        elif text4 == "0":
            print("Undraw functionality called")
            win.getMouse()
            win.close()
            Universalfunc ()

  decision(text3, text4, vert)
     
  


   

Universalfunc()
