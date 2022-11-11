1  # program0612.py
2
3
import turtle

4
5


def gxy():  # 绘制200个点，每点turtle方向右转1度


    6
for i in range(200):
    7
turtle.right(1)  # 调整turtle前进方向右转1度
8
turtle.forward(1)
9
10
turtle.setup(400, 300)
11
turtle.color('red', 'pink')
12
turtle.pensize(2)
13
turtle.speed(30)
14
turtle.goto(0, -100)
15
16
turtle.begin_fill()
17
turtle.left(140)  # 调整turtle前进方向左转140度
18
turtle.forward(112)
19
gxy()
20
turtle.left(120)
21
gxy()
22
turtle.forward(112)
23
turtle.end_fill()
24  # 绘制文字
25
turtle.up()
26
turtle.seth(180)  # 调整turtle方向左向180度
27
turtle.fd(100)
28
turtle.write("I Love Python")
29
turtle.hideturtle()  # 隐藏turtle
