import turtle  # this imports a library called "turtle". A library is (typically someone else's) python code, that you can use in your own program.
from random import triangular


def demo():  # demonstration of basic turtle commands
    tom.speed(1)  # fastest: 10, slowest: 1
    for x in range(8):  # do the following for x = 0, 1, 2, 3, 4, 5, 6, 7
        tom.forward(50)  # move 50 pixels
        tom.left(45)  # turn 45 degrees left
        print(f'Tom is now at {tom.position()}, x-value: {tom.position()[0]=:.2f}, y-value: {tom.position()[1]=:.2f}')
    tom.penup()  # do not draw while moving from now on
    tom.forward(100)
    tom.pendown()  # draw while moving from now on
    tom.circle(50)  # draw a circle with radius 50
    tom.pencolor("red")  # draw in red
    tom.right(90)  # turn 90 degrees right
    tom.forward(120)
    tom.right(-90)  # turning -90 degrees right is the same as turning +90 degrees left
    tom.forward(120)
    tom.goto(-100, -200)  # move to coordinates -100, -200  (0, 0 is the middle of the screen)
    tom.home()  # return to the original position in the middle of the window


def cirkel(radius):
    tom.circle(radius)

def move_to(x, y):
    tom.penup()
    tom.goto(x, y)
    tom.pendown()

def square(length):
    for i in range(4):
        tom.forward(length)
        tom.left(90)

def triangle(length):
    tom.right(90)
    tom.forward(length)
    tom.left(120)
    tom.forward(length)
    tom.left(120)
    tom.forward(length)
    tom.left(30)

def color_triangle(length, color):
    tom.pencolor(color)
    triangle(length)
    tom.pencolor("black")

def many_square(numberOf, length, distance):
    for i in range(numberOf):
        square(length)
        tom.penup()
        tom.forward(distance)
        tom.pendown()

def many_circle(numberOf, radius, distance):
    for i in range(numberOf):
        cirkel(radius)
        tom.penup()
        tom.forward(distance)
        tom.pendown()

def draw_square_at(length, x, y):
    tom.penup()
    tom.goto(x, y)
    tom.pendown()
    square(length)

def grid(rows, cols, size):
    tom.penup()
    start_x, start_y = tom.position()  # husker startposition
    y = start_y

    for r in range(rows):
        x = start_x
        for c in range(cols):
            tom.penup()
            tom.goto(x, y)
            tom.pendown()
            square(size)
            x += size  # flyt til næste kolonne
        y -= size

def house(size):
    square(size)
    tom.left(90)
    tom.forward(size)
    tom.color("red")
    triangle(size)
    tom.color("black")
    tom.forward(size)
    tom.left(90)
    tom.forward(size * 0.4)
    tom.left(90)
    tom.forward(size * 0.3)
    tom.right(90)
    tom.forward(size * 0.2)
    tom.right(90)
    tom.forward(size * 0.3)
    tom.left(90)

def spiral_square(size, spiral):
    tom.penup()
    tom.goto(0, 0)
    tom.pendown()
    tom.right(90)
    for i in range(spiral * 4):
        tom.forward(size * i)
        tom.left(90)

    tom.penup()
    tom.goto(0, size)
    tom.pendown()
    tom.left(180)
    for i in range(spiral * 4):
        tom.forward(size * i)
        tom.left(90)

def star(size):
    tom.penup()
    tom.goto(-size * 0.5, 0)
    tom.setheading(90)
    tom.forward(size)
    tom.pendown()
    tom.right(90)
    for i in range(5):
        tom.forward(size)
        tom.right(144)

def danmark():
    tom.speed(10)
    tom.penup()
    tom.goto(-200, -20)
    tom.pendown()
    tom.color("red")
    tom.setheading(-90)
    for i in range(90):
        tom.forward(200 * 0.9)
        tom.left(90)
        tom.forward(1)
        tom.left(90)
        tom.forward(200 * 0.9)
        tom.right(90)
        tom.forward(1)
        tom.right(90)
    tom.penup()
    tom.goto(-200, 10)
    tom.pendown()
    tom.setheading(90)
    for r in range(90):
        tom.forward(200 * 0.9)
        tom.right(90)
        tom.forward(1)
        tom.right(90)
        tom.forward(200 * 0.9)
        tom.left(90)
        tom.forward(1)
        tom.left(90)

    tom.speed(10)
    tom.penup()
    tom.goto(200, -20)
    tom.pendown()
    tom.color("red")
    tom.setheading(-90)
    for i in range(90):
        tom.forward(200 * 0.9)
        tom.right(90)
        tom.forward(1)
        tom.right(90)
        tom.forward(200 * 0.9)
        tom.left(90)
        tom.forward(1)
        tom.left(90)
    tom.penup()
    tom.goto(200, 10)
    tom.pendown()
    tom.setheading(90)
    for r in range(90):
        tom.forward(200 * 0.9)
        tom.left(90)
        tom.forward(1)
        tom.left(90)
        tom.forward(200 * 0.9)
        tom.right(90)
        tom.forward(1)
        tom.right(90)

tom = turtle.Turtle()  # create an object named tom of type Turtle

#cirkel(40)
#move_to(50, 40)
#square(40)
#move_to(100, 90)
#triangle(100)
#move_to(-100, 90)
#color_triangle(100, "blue")
#many_square(6, 40, 60)
#many_circle(2, 20, 60)
#draw_square_at(40, 80, 80)
#move_to(-200, 200)
#grid(5, 5, 40)
#house(100)
#spiral_square(20, 5)
#star(90)
danmark()
#demo()
turtle.done()  # keep the turtle window open after the program is done
