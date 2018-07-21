import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("blue")

    one_turtle = turtle.Turtle()
    one_turtle.shape("turtle")
    one_turtle.color("yellow")
    one_turtle.speed(2)

    for i in range (1,5):
        one_turtle.forward(100)
        one_turtle.right(90)

    window.exitonclick()

draw_square()

