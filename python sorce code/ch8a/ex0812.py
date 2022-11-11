# program0612.py
import turtle
def gxy():                #绘制200个点，每点turtle方向右转1度
    for i in range (200):
        turtle.right(1)   #调整turtle前进方向右转1度
        turtle.forward(1)
turtle.setup(400,300)
turtle.color('red','black')
turtle.pensize(2)
turtle.speed(30)
turtle.goto(0,-100)
turtle.begin_fill()
turtle.left(140)     #调整turtle前进方向左转140度
turtle.forward(112)
gxy()
turtle.left(120)
gxy()
turtle.forward(112)
turtle.end_fill()
#绘制文字
turtle.up()
turtle.seth(180)       #调整turtle方向左向180度
turtle.fd(100)
turtle.write("I Love Python")
turtle.hideturtle()    #隐藏turtle
