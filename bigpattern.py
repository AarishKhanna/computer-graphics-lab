#bigpatter.py
from graphics import *
import math
 
def dda():
    win=GraphWin('Simple_DDA',1000,1000)
    t=Text(Point(50,50),'Simple_DDA')
    t.draw(win)

    win.setCoords(-1000.0, -1000.0, 1000.0, 1000.0)
    # Draw vertical lines
    Line(Point(-1000,0), Point(1000,0)).draw(win)
    # Draw horizontal lines
    Line(Point(0,-1000), Point(0,1000)).draw(win)

    def dda2():

        # Initialising hex string
        temp = "100000001"
        temp  =  temp * 10000
        
        res = temp

        p1=win.getMouse()
        p1.draw(win)
        p2=win.getMouse()
        p2.draw(win)

        ax=p1.x
        ay=p1.y
        bx=p2.x
        by=p2.y
        print(ax,ay,bx,by)

        dx=bx-ax
        dy=by-ay
        print(dx,dy)

        if abs(dx)>abs(dy):
            len=abs(dx)
        else:
            len=abs(dy)

        xinc = (dx/float(len))
        yinc = (dy/float(len))

        pt=Point(ax,ay)
        pt.setOutline('blue')
        pt.draw(win)
        ax1 = ax
        ay1 = ay

        for i in range(int(len)):
            ax=ax+xinc
            ay=ay+yinc
            ax1=ax+xinc
            ay1=ay+yinc
            print(res[i],temp[i])
            if res[i] == '1':
                pt=Point(int(ax),int(ay))
                pt.setOutline('blue')
                pt.draw(win)
                print(int(ax),int(ay))
            else:
                continue

        dda2()

    dda2()

    win.getMouse()
        
   



dda()