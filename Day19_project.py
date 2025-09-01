from turtle import Turtle,Screen
import random
b=Screen()
end=False
b.setup(600,400)
color=["red","blue","green","yellow","cyan","magenta"]
position=[50,100,150,0,-50,-100]
turtles=[]
c= b.textinput("winner","Chose Color which Turtle will win?")
for tur in range(0,6):
    a = Turtle(shape="turtle")
    a.penup()
    a.color(color[tur])
    a.goto(-280, position[tur])
    turtles.append(a)
while end==False:
    for tur in turtles:
        if tur.xcor()<280:
            mov=random.randint(0,10)
            tur.forward(mov)
        else:
            end=True
            print(f"{tur.fillcolor()} turtle won the Race")
            if tur.fillcolor()==c:
                print("Congratulations! You Win!")
            else:
                print("You Lose!")

b.exitonclick()