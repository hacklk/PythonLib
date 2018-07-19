import turtle


def draw_circle():
    window = turtle.Screen()
    window.bgcolor("blue")
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("red")
    angie.speed(2)
    angie.circle(100)

    window.exitonclick()

draw_circle()
