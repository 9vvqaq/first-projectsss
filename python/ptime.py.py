#pentime11.py
import turtle
import time
def drawGap():
    turtle.penup()
    turtle.fd(5)
def drawline(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawDigit(digit):
    drawline(1)if digit in[2,3,4,5,6,8,9] else drawline(0)
    drawline(1)if digit in[0,1,3,4,5,6,7,8,9] else drawline(0)
    drawline(1)if digit in[0,2,3,5,6,8,9] else drawline(0)
    drawline(1)if digit in[0,2,6,8] else drawline(0)
    turtle.left(90)
    drawline(1)if digit in[0,4,5,6,8,9] else drawline(0)
    drawline(1)if digit in[0,2,3,5,6,7,8,9] else drawline(0)
    drawline(1)if digit in[0,1,2,3,4,7,8,9] else drawline(0)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):
    turtle.pencolor(34,56,108)
    for i in date:
        if i == '-':
            turtle.write("年",font=("Arial",18,"normal"))
            turtle.pencolor(236,208,176)
            turtle.fd(40)
        elif i == '=':
            turtle.write("月",font=("Arial",18,"normal"))
            turtle.pencolor(34,56,108)
            turtle.fd(40)
        elif i == '+':
            turtle.write("日",font=("Arial",18,"normal"))
        else:
            drawDigit(int(i))
            
def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.colormode(255)
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(time.strftime("%Y-%m=%d+", time.gmtime()))
    turtle.hideturtle()
    turtle.done()
main()
