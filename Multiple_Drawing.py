#Multiple_Drawing
from graphics import *
import time
import math
 
def Universalfunc():
  win=GraphWin('Multiple Drawing',1000,1000)
  win.setBackground("white")
  t=Text(Point(50,50),'Multiple Drawing :Enter 1 for dda, 2 for bresnam, 3 for circle, 4 for pattern line, 5 for pattern circle, 6 for thick circle  and 0 to break')
  t.draw(win)

  win.setCoords(-3000.0, -3000.0, 3000.0, 3000.0)
    # Draw vertical lines
  Line(Point(-3000,0), Point(3000,0)).draw(win)
    # Draw horizontal lines
  Line(Point(0,-3000), Point(0,3000)).draw(win)

  def PutPixle(win, x, y):
     pt = Point(x,y)
     pt.draw(win)  

  def midPointCircleDraw2():
        p1=win.getMouse()
        p1.draw(win)
        p2=win.getMouse()
        p2.draw(win)
        ax=p1.x
        ay=p1.y
        bx=p2.x
        by=p2.y

        temp1 = bx-ax
        temp1 = temp1*temp1
        temp2 = by - ay
        temp2 = temp2*temp2 

        r = temp1+temp2
        r = math.sqrt(r)
        x_centre = ax
        y_centre = ay
        
        x = r
        y = 0
            
            
        
        P = 1 - r 
        
        while x > y:
            
            y += 1
                
            
            if P <= 0: 
                P = P + 2 * y + 1
                    
            
            else:         
                x -= 1
                P = P + 2 * y - 2 * x + 1
                
            
            if (x < y):
                break
                
            
            x1 = x + x_centre
            y1 = y + y_centre
            
            x2 = -x + x_centre
            y2 = y + y_centre
            
            x3 = x + x_centre
            y3 = -y + y_centre
            
            x4 = -x + x_centre
            y4 = -y + y_centre
            PutPixle(win, x1,y1)
            PutPixle(win, x2,y2)
            PutPixle(win, x3,y3)
            PutPixle(win, x4,y4)

            
            if x != y:
                x1 = y + x_centre
                y1 = x + y_centre
        
                x2 = -y + x_centre
                y2 = x + y_centre
        
                x3 = y + x_centre
                y3 = -x + y_centre
        
                x4 = -y + x_centre
                y4 =  -x + y_centre
        
                PutPixle(win, x1,y1)
                PutPixle(win, x2,y2)
                PutPixle(win, x3,y3)
                PutPixle(win, x4,y4)
            
        

  def dda2():

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

        for i in range(int(len)):
            ax=ax+xinc
            ay=ay+yinc
            pt=Point(int(ax),int(ay))
            pt.setOutline('blue')
            pt.draw(win)
            print(int(ax),int(ay))

  def bres2():               

        p1=win.getMouse()
        p1.draw(win)
        p2=win.getMouse()
        p2.draw(win)

        x1=p1.x 
        y1=p1.y
        x2=p2.x
        y2=p2.y
        print(x1,y1,x2,y2)

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        m = dy/dx 
        t = 3
        slope = (dy/float(dx))
        print(dx,dy,slope)
        
        x, y = x1, y1 
        ax2 = x1
        ay2 = y1 
        ax1 = x1 
        ay1 = y1 

        if slope > 1:
            dx, dy = dy, dx
            x, y = y, x
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        p = 2 * dy - dx
        
        pt=Point(x,y)
        pt.draw(win)
            
        for k in range(int(dx)):
            if p > 0:
                y = y + 1 if y1 < y2 else y - 1
                p = p + 2*(dy - dx)
            else:
                p = p + 2*dy
            x = x + 1 if x1 < x2 else x - 1

            
            pt=Point(x,y)
            print(x,y)
            pt.draw(win)

        for i in range(int(t)):
             ay1 = y1 + i
             ax1 = x1 - (i/m)
             for j in range(int(dx)):
                if p > 0:
                    ay1 = ay1 + 1 if y1 < y2 else ay1 - 1
                    p = p + 2*(dy - dx)
                else:
                    p = p + 2*dy
                ax1 = ax1 + 1 if x1 < x2 else ax1 - 1

                
                pt=Point(ax1,ay1)
                pt.draw(win)   
  
  def ddawithpattern():

        # Initialising hex string
        temp = "100000C"
        temp  =  temp * 10000
        
        res = "{0:08b}".format(int(temp , 16))

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
        
  def Circlewithpattern():
       
       # Initialising hex string
        temp = "100000C"
        temp  =  temp * 10000
        
        temp = "{0:08b}".format(int(temp , 16))
        p1=win.getMouse()
        p1.draw(win)
        p2=win.getMouse()
        p2.draw(win)
        ax=p1.x
        ay=p1.y
        bx=p2.x
        by=p2.y

        temp1 = bx-ax
        temp1 = temp1*temp1
        temp2 = by - ay
        temp2 = temp2*temp2 

        r = temp1+temp2
        r = math.sqrt(r)
        x_centre = ax
        y_centre = ay
        
        x = r
        y = 0
            
            
        
        P = 1 - r 
        i = 0
        
        while x > y:
            
            y += 1
                
            
            if P <= 0: 
                P = P + 2 * y + 1
                    
            
            else:         
                x -= 1
                P = P + 2 * y - 2 * x + 1
                
            
            if (x < y):
                break
                
            
            x1 = x + x_centre
            y1 = y + y_centre
            
            x2 = -x + x_centre
            y2 = y + y_centre
            
            x3 = x + x_centre
            y3 = -y + y_centre
            
            x4 = -x + x_centre
            y4 = -y + y_centre

            if temp[i] == '1': 
                PutPixle(win, x1,y1)
                PutPixle(win, x2,y2)
                PutPixle(win, x3,y3)
                PutPixle(win, x4,y4)
                i = i+1
            else: 
                i = i+1
                continue

            
            if x != y:
                x1 = y + x_centre
                y1 = x + y_centre
        
                x2 = -y + x_centre
                y2 = x + y_centre
        
                x3 = y + x_centre
                y3 = -x + y_centre
        
                x4 = -y + x_centre
                y4 =  -x + y_centre
         
                PutPixle(win, x1,y1)
                PutPixle(win, x2,y2)
                PutPixle(win, x3,y3)
                PutPixle(win, x4,y4)
  
  def thickCircle():
        p1=win.getMouse()
        p1.draw(win)
        p2=win.getMouse()
        p2.draw(win)
        ax=p1.x
        ay=p1.y
        bx=p2.x
        by=p2.y
        t = 20

        temp1 = bx-ax
        temp1 = temp1*temp1
        temp2 = by - ay
        temp2 = temp2*temp2 

        r = temp1+temp2
        r = math.sqrt(r)

        x_centre = ax
        y_centre = ay
        
        
            
            
        for i in range(int(t)): 
                P = 1 - r + i 
                x = r + i
                y = 0
                
                
                while x > y:
                    
                    y += 1
                        
                    
                    if P <= 0: 
                        P = P + 2 * y + 1
                            
                    
                    else:         
                        x -= 1
                        P = P + 2 * y - 2 * x + 1
                        
                    
                    if (x < y):
                        break
                        
                    
                    x1 = x + x_centre
                    y1 = y + y_centre
                    
                    x2 = -x + x_centre
                    y2 = y + y_centre
                    
                    x3 = x + x_centre
                    y3 = -y + y_centre
                    
                    x4 = -x + x_centre
                    y4 = -y + y_centre
                    PutPixle(win, x1,y1)
                    PutPixle(win, x2,y2)
                    PutPixle(win, x3,y3)
                    PutPixle(win, x4,y4)

                    
                    if x != y:
                        x1 = y + x_centre
                        y1 = x + y_centre
                
                        x2 = -y + x_centre
                        y2 = x + y_centre
                
                        x3 = y + x_centre
                        y3 = -x + y_centre
                
                        x4 = -y + x_centre
                        y4 =  -x + y_centre
                
                        PutPixle(win, x1,y1)
                        PutPixle(win, x2,y2)
                        PutPixle(win, x3,y3)
                        PutPixle(win, x4,y4)

  
  for i in range(100):
     
     textEntry = Entry(Point(233,200),50)
     textEntry.draw(win)

     # click the mouse to signal done entering text
     win.getMouse()

     text = textEntry.getText() 
     shape1 = text

     if shape1 == "3": midPointCircleDraw2()
     elif shape1 == "1": dda2()
     elif shape1 == "2": bres2()
     elif shape1 == "4": ddawithpattern()
     elif shape1 == "5": Circlewithpattern()
     elif shape1 == "6": thickCircle()
     elif shape1 == "0": break 
     else: print("invalid arguement passed")




    

 
  win.getMouse()
  win.close()
                       

   

Universalfunc()