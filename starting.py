
from turtle import Turtle,Screen
screen=Screen()

a=Turtle()
a.speed("fastest")
def f():
    a.forward(30)
def k():
    a.lt(90)
    a.forward(30)
def s():
    n=a.heading()+10
    a.setheading(n)
def c():
    a.clear()
    a.penup()
    a.home()
    a.pendown()
screen.listen()
screen.onkey(key="space",fun=f)
screen.onkey(key="Up",fun=k)
screen.onkey(key="s",fun=s)
screen.onkey(key="c",fun=c)


screen.exitonclick()

