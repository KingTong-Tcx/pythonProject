# 绘制双心
# program0812.py
import turtle


def gxy():  # 绘制200个点，每点turtle方向右转1度
    for i in range(200):
        turtle.right(1)  # 调整turtle前进方向右转1度
        turtle.forward(1)


turtle.up()  # 修改，目的是去掉那条直线
turtle.setup(600, 400)
turtle.color('red')
turtle.pensize(2)
turtle.speed(30)
turtle.goto(0, -100)
turtle.down()  # 修改，配合上面
turtle.begin_fill()
turtle.left(140)  # 调整turtle前进方向左转140度
turtle.forward(112)
gxy()
turtle.left(120)
gxy()
turtle.forward(112)
turtle.fillcolor("red")
turtle.end_fill()
# 绘制另一个心
turtle.up()
turtle.goto(100, -100)
turtle.down()  # 修改，配合上面
turtle.begin_fill()
turtle.setheading(0)
turtle.left(140)  # 调整turtle前进方向左转140度
turtle.forward(112)
gxy()
turtle.left(120)
gxy()
turtle.forward(112)
turtle.fillcolor("red")
turtle.end_fill()
turtle.up()
turtle.seth(180)  # 调整turtle方向左向180度
turtle.fd(100)
turtle.goto(-200, -150)
turtle.write("I Love Python", font=('宋体', 50, 'normal'))
turtle.hideturtle()  # 隐藏turtle

# 绘制文字
turtle.up()
turtle.seth(180)  # 调整turtle方向左向180度
turtle.fd(100)
turtle.goto(-200, -150)
turtle.write("I Love Python", font=('宋体', 50, 'normal'))
turtle.hideturtle()  # 隐藏turtle
turtle.done()  # 结束
