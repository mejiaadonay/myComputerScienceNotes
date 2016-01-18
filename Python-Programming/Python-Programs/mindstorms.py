import turtle

# mindstorm
# Author: Jose Escobar Mejia
# Date:   1/18/2016

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    total_move = 4
    total = 0

    # This for loop is perform better than the code below.
#    for total in range(total_move):
#        brad.forward(100)
#        brad.right(90)
#    total=total+1

    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)


draw_square()
