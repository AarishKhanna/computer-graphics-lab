from graphics import *


win = GraphWin("Move the Circle", 1000, 1000)
win.setBackground("white")
def moveTo(newCenter):
    
    circle = Circle(Point(newCenter.getX(), newCenter.getY()),100)
    circle.draw(win)
    return circle



def main():
    
    c = Circle(Point(500, 300), 100)
    c.draw(win)
    i = 0
    while i <=10:
        p = win.getMouse()
        moveTo(p)
        i = i + 1


main()