1  # program0611.py
2
'''绘制图案为紫色正方形螺旋'''
3
import turtle

4
turtle.setup(400, 360)
5
turtle.pensize(2)  # 设置画笔宽度为1像素
6
turtle.pencolor("purple")  # 设置画笔颜色为紫色
7
turtle.shape("turtle")  # 设置画笔形状为“海龟”
8
turtle.speed(10)  # 设置绘图速度为10
9
a = 5  # 起始移动长度a为5单位
10
for i in range(40):  # 循环40次
    11
a = a + 6  # 移动长度a每次增加6单位
12
turtle.left(90)  # 画笔每次移动旋转90度
13
turtle.fd(a)  # 画笔向前移动a单位
14
turtle.hideturtle()  # 隐藏画笔
15
turtle.done()  # 结束绘制
