import turtle
turtle.bgcolor("black")

heart = turtle.Turtle()
heart.speed(20)
heart.pencolor("blue")
for i in range(500):
    heart.forward(i)
    heart.left(91)