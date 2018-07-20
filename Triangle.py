import turtle

def draw_triangle():
    window = turtle.Screen()
    window.bgcolor("blue")

    holo = turtle.Turtle()
    holo.shape("circle")
    holo.color("green")
    holo.speed(2)
    loopcount = 0
    loopmax = 3

    while loopcount < loopmax:
        holo.forward(100)
        holo.left(120)
        loopcount = loopcount + 1
    window.exitonclick()

draw_triangle()


