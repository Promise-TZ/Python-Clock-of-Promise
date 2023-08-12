import turtle
import time

def draw_clock(h, m, s):
    # 绘制表盘
    turtle.pensize(4)
    turtle.pencolor("black")
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.circle(200)

    # 绘制刻度
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(90)
    for i in range(12):
        turtle.penup()
        turtle.forward(170)
        turtle.pendown()
        turtle.forward(20)
        turtle.penup()
        turtle.goto(0, 0)
        turtle.right(30)

    # 绘制时针
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(90)
    angle = (h % 12) * 30 + m / 2
    turtle.right(angle)
    turtle.pendown()
    turtle.pensize(6)
    turtle.pencolor("red")
    turtle.forward(100)

    # 绘制分针
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(90)
    angle = m * 6
    turtle.right(angle)
    turtle.pendown()
    turtle.pensize(4)
    turtle.pencolor("blue")
    turtle.forward(150)

    # 绘制秒针
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(90)
    angle = s * 6
    turtle.right(angle)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor("green")
    turtle.forward(180)

while True:
	h = int(time.strftime("%I"))
	m = int(time.strftime("%M"))
	s = int(time.strftime("%S"))
	draw_clock(h, m, s)
	time.sleep(1)
	turtle.clear()

