from turtle import Turtle, Screen
import random
"""
we can put function in a function like fun = move_forward
for example, 
def add(n1, n2)
    return n1, n2

def calculator(n1, n2, func):
    return func(n1, n2)
    
result = calculator(2,3,add)
print(result)
"""
is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400) #set the screen size to 500 x 400
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color!: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = [] #multiple turtle instances
y_positions = -100

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions)
    y_positions += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color}turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color}turtle is the winner!")


        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
