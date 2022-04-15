from turtle import Turtle,Screen
import random
screen=Screen()

race_on=False
screen.setup(width=500,height=300)
user_bet=screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter a code: ")
color=['red','blue','yellow','green','black']
y=-30
types_of_turtle=[]
for i in color:
    a=Turtle(shape="turtle")
    a.color(i)
    a.penup()
    a.goto(x=-250,y=y)
    y+=50
    types_of_turtle.append(a)

if user_bet:
    race_on=True
while race_on:
    for i in types_of_turtle:

        if i.xcor()>730:
            winning_color=i.pencolor()
            race_on=False
            if winning_color==user_bet:
                print(f"You've won! The {winning_color} Turtle is the Winner")
            else:
                print(f"You've lost! The winner is {winning_color} Turtle")

        dist=random.randint(0,10)
        i.fd(dist)

screen.exitonclick()