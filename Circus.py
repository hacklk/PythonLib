import turtle

def draw_square(one_turtle):
    for i in range (1,5):
        one_turtle.forward(100)
        one_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")
    brand = turtle.Turtle()
    brand.shape("turtle")
    brand.color("yellow")
    brand.speed(8)
    for i in range (1,37):
        draw_square(brand)
        brand.right(10)
    window.exitonclick()

draw_art()


