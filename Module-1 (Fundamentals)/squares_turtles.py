from turtle import *

wn = Screen()
wn.setup(500,500)
turtle = Turtle()
turtle.speed("fastest")
i=0
step = 100
def draw_square(length,angle):
    global i,step
    for b in range (0,4):
        turtle.forward(length+i)
        turtle.right(angle+b)
    while(i<step):
        i+=1
        draw_square(100,90)
draw_square(100,90)
                                            