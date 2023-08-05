from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


def draw_points(x, y):
    glPointSize(2) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glColor3f(1, 0, 1) #color
    glVertex2f(x,y)
    

    #jekhane show korbe pixel, Cordinates
    glEnd()


def sym(x, y, c_x, c_y):
    draw_points(c_x + x, c_y + y)
    draw_points(c_x - x, c_y + y)
    draw_points(c_x + x, c_y - y)
    draw_points(c_x - x, c_y - y)
    draw_points(c_x + y, c_y + x)
    draw_points(c_x - y, c_y + x)
    draw_points(c_x + y, c_y - x)
    draw_points(c_x - y, c_y - x)

# def sm_sym(x, y, c_x, c_y,r):
#     c_x+=15+150
#     c_y+=15+150
#     draw_spoints(c_x,c_y,x,y)
#     c_x= r
#     c_y= r 
#     c_x+=85+150
#     c_y+=85+150  

#     draw_spoints(c_x,c_y,x,y)   
#     c_x= r
#     c_y= r+150
#     c_x+= 50+150
#     draw_spoints(c_x,c_y,x,y)
#     c_x= r+150
#     c_y= r
#     c_y+= 50+150
#     draw_spoints(c_x,c_y,x,y)
#     c_x= r
#     c_y= r
#     c_x+= 100+150
#     c_y+= 50+150
#     draw_spoints(c_x,c_y,x,y)
#     c_x= r
#     c_y= r
#     c_x+= 50+150
#     c_y+= 100+150
#     draw_spoints(c_x,c_y,x,y) 
#     c_x= r
#     c_y= r
#     c_x+= 85+150
#     c_y+= 15+150
#     draw_spoints(c_x,c_y,x,y)
#     c_x= r
#     c_y= r
#     c_x+= 15+150
#     c_y+= 85+150
#     draw_spoints(c_x,c_y,x,y)


def MidpointCircle(r, c_x, c_y):
    d= 1-r
    x= 0
    y= r
    while x<=y:
        sym(x,y,c_x,c_y)
        if(d<0):
            #choose E
            d= d+ 2*x +3
            x+=1

        else:
            #choose SE
            d= d+ 2*x - 2*y +5
            x+=1
            y-=1

