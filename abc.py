#Bresenham's Line Drawing
from graphics import *

def BresenhamLine():
   win=GraphWin('Brasenham Line',500,500)
   t=Text(Point(50,50),'Brasenham')
   t.draw(win)

  
   p1=win.getMouse()
   p1.draw(win)
   p2=win.getMouse()
   p2.draw(win)

   x1=p1.x 
   y1=p1.y
   x2=p2.x
   y2=p2.y
   print(y1,y2)

   dx = abs(x2 - x1)
   dy = abs(y2 - y1)
   slope = dy/float(dx)
  
   x, y = x1, y1  


   if slope > 1:
       dx, dy = dy, dx
       x, y = y, x
       x1, y1 = y1, x1
       x2, y2 = y2, x2

   p = 2 * dy - dx
  
   pt=Point(x,y)
   pt.draw(win)

   for k in range(2, int(dx)):
       if p > 0:
           y = y + 1 if y < y2 else y - 1
           p = p + 2*(dy - dx)
       else:
           p = p + 2*dy
       x = x + 1 if x < x2 else x - 1
       pt=Point(x,y)
       pt.draw(win)


   win.getMouse()

BresenhamLine()
