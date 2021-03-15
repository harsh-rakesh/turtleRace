from turtle import Turtle, Screen
import random
race_on =False
screen=Screen()
all_turtle=[]
screen.setup(width=500,height=400)
user_bet=screen.textinput("Make your bet","Which turtle will win?")
colors=["red","purple","blue","yellow","orange","green"]
y_position=[20, 50, 80, -40, -10, -70]
for i in range(0,6):
    turtle1 = Turtle(shape='turtle')
    turtle1.color(colors[i])
    turtle1.penup()
    turtle1.goto(x=-240,y=y_position[i])
    all_turtle.append(turtle1)
if user_bet:
    race_on=True
else:
    race_on=False
while race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            race_on=False
            win=turtle.color()
            if win==user_bet:
                print("You've won! The "+ str(win[0])+" colour won.")
            else:
                print("You lost. The "+ str(win[0])+" colour won.")
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)
screen.exitonclick()