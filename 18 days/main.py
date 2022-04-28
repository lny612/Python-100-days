# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as turtle_module
import random
tim = turtle_module.Turtle()
tim.speed("fastest")
turtle_module.colormode(255)
tim.hideturtle()
tim.penup()
color_list = [(202, 164, 110), (27, 68, 102), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208)]

pos_y = -200
pos_x = -200

for row in range(10):
    tim.setposition(pos_x, pos_y)
    tim.dot(20, random.choice(color_list))
    for _ in range(9):

        if row % 2 == 0:
            tim.forward(50)
        else:
            tim.backward(50)

        tim.dot(20, random.choice(color_list))

    pos_x, pos_y = tim.position()
    pos_y += 50

screen = turtle_module.Screen()
screen.exitonclick()