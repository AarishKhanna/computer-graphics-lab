# DDA Algorithm 
from graphics import *
import time
 
def BresenhamLine(): 
   # creating the window
   win = GraphWin('Brasenham Line', 600, 480)
   t=Text(Point(50,50),'Brasenham Line')
   t.draw(win)

   p1=win.getMouse()
   p1.draw(win)
   p2=win.getMouse()
   p2.draw(win)

   ax=p1.x
   ay=p2.y
   bx=p2.x
   by=p2.y

   dx = abs(bx - ax)
   dy = abs(by - ay)
   slope = dy/float(dx)
   x,y = ax, ay

   # checking the slope if slope > 1
   # then interchange the role of x and y
   if slope > 1:
       dx, dy = dy, dx 
       ax, ay = ay, ax
       bx, by = by, bx
   # initialization of the inital disision parameter
   p = 2 * dy - dx
  
   pt=Point(x,y)
   pt.setOutline('blue')
   pt.draw(win)

   for i in range(ax, bx+1):
       if p > 0:
           y = y + 1 if y < by else y - 1
           p = p + 2*(dy - dx)
       else:
           p = p + 2*dy
       x = x + 1 if x < bx else x - 1
      
       pt=Point(int(x),int(y))
       pt.setOutline('blue')
       pt.draw(win)


   win.getMouse()

BresenhamLine() 
      

   
    

    

    

    