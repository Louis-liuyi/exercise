import turtle
import math

def trianglehuge(some_turtle,x):
def trianglebig(some_turtle,x):
    triangle(some_turtle,x)
    some_turtle.goto(x,0)
    triangle(some_turtle,x)
    some_turtle.goto(0.5*x,math.sqrt(x**2-(0.5*x)**2))
    triangle(some_turtle,x)
    some_turtle.goto(0,0)
    
    
def triangle(some_turtle,x):
    for i in range(1,4):
        some_turtle.forward(x)
        some_turtle.left(120)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")

    liu = turtle.Turtle()
    liu.shape("arrow")
    liu.color("blue","green")
    liu.speed(10)
    liu.begin_fill()
    trianglehuge(liu,20)
    liu.end_fill()
    liu.goto(40,(math.sqrt(80*80-40*40)))
    window.exitonclick()
    

draw_art()
