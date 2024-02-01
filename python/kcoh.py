#koch.py
import turtle as tt
def koch (size,n):
    if n == 0:
        tt.fd(size)
    else:
        for angle in [0,60,-120,60]:
            tt.left(angle)
            koch(size/3,n-1)
def main():
    tt.setup(600,600)
    tt.penup()
    tt.goto(-200,100)
    tt.pendown()
    tt.pensize(2)
    level = int(input("请输入几阶："))
    koch(400,level)
    tt.right(120)
    koch(400,level)
    tt.right(120)
    koch(400,level)
    tt.hideturtle()
main()
