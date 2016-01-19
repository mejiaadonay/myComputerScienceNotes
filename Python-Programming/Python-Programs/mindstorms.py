import turtle

# mindstorm
# Author: Jose Escobar Mejia
# Date:   1/18/2016

def draw_square(some_turtle):
    for i in range (1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #Create the turtle Brad - draw a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for i  in range(1,36):
        draw_square(brad)
        brad.right(10)

#    draw_circle()
    
    window.exitonclick()
    
#def draw_circle():
#    angie = turtle.Turtle()
#    angie.shape("arrow")
#    angie.color("blue")
#    angie.circle(100)
    
draw_art()
