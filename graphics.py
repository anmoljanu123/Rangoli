import turtle as t                                 # turtle is a library to draw shapes and graphics
import time as ti                                  # time is the library in python
from itertools import cycle                        # This method prints all the values that are given as an argument to this me. And again it starts from the beginning when it reaches the end.

colors = cycle(['red','orange','yellow','blue','green','purple'])

def draw_rangoli(color,size,angle):                # declaring function having three parameters
     t.pencolor(next(colors))                      # this argument take color values from the colors list defined above and this cycle go on until it is terminated
     t.circle(size)                                # this will take the size of circle
     t.right(angle)                                # this argument will take the value of angle
     draw_rangoli(color,size,angle)                # this is the recursive function

t.bgcolor('black')                                 # this arguments sets the background colour of rangoli
t.speed(50)                                        # this argument sets the speed of drawing rangoli
t.pensize(4)                                       # this argument sets the width of pen
draw_rangoli("red",100,75)                         # calling function
ti.sleep(3)                                        # it's the time duration of our design to be shown
t.hideturtle()                                     # this argument hides the turtle pointer
