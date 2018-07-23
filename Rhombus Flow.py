import turtle

def draw_rhombus(turtle, size, small_angle):
    for i in range (2):
        turtle.forward(size)
        turtle.right(small_angle)
        turtle.forward(size)
        turtle.right((360-2*small_angle)//2)


def draw_flower(turtle, size, angle):
    for i in range (360//angle):
        draw_rhombus(turtle, size, angle)
        turtle.right(10)
    turtle.right(90)
    turtle.forward(size*3)


window = turtle.Screen()
window.bgcolor("blue")

brand = turtle.Turtle()
brand.shape("turtle")
brand.color("yellow")
brand.speed(99)

draw_flower(brand, 100, 5)

window.exitonclick()

