import turtle

screen = turtle.Screen()
screen.title("SpongeBob SquarePants")
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.pensize(3)


def go(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def fill_rect(x, y, width, height, color):
    go(x, y)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()


def fill_circle(x, y, radius, color):
    go(x, y)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def draw_sponge_holes():
    holes = [
        (-120, 80, 12), (-40, 110, 10), (40, 85, 14),
        (-90, 20, 10), (10, 20, 12), (90, 40, 10),
        (-60, -30, 9), (50, -20, 11)
    ]
    for x, y, r in holes:
        fill_circle(x, y, r, "#d1b12c")


def draw_eyes():
    fill_circle(-35, 85, 32, "white")
    fill_circle(35, 85, 32, "white")

    fill_circle(-22, 88, 12, "#5dade2")
    fill_circle(48, 88, 12, "#5dade2")

    fill_circle(-18, 92, 5, "black")
    fill_circle(52, 92, 5, "black")

    fill_circle(-16, 97, 2, "white")
    fill_circle(54, 97, 2, "white")

    # Eyelashes
    for x in (-45, -35, -25):
        go(x, 120)
        t.setheading(90)
        t.forward(18)

    for x in (25, 35, 45):
        go(x, 120)
        t.setheading(90)
        t.forward(18)


def draw_nose():
    go(8, 70)
    t.setheading(-20)
    t.circle(35, 120)


def draw_mouth():
    go(-55, 35)
    t.setheading(-10)
    t.circle(60, 120)

    # Teeth
    fill_rect(-18, 25, 15, 20, "white")
    fill_rect(2, 25, 15, 20, "white")

    # Tongue
    go(-15, 18)
    t.setheading(0)
    t.fillcolor("#f1948a")
    t.begin_fill()
    t.circle(15, 180)
    t.goto(-15, 18)
    t.end_fill()

    # Cheeks
    fill_circle(-70, 45, 6, "#f5b7b1")
    fill_circle(80, 45, 6, "#f5b7b1")


def draw_shirt_and_tie():
    fill_rect(-140, -90, 280, 45, "white")
    fill_rect(-140, -45, 280, 20, "#8b5a2b")

    # Tie
    go(0, -45)
    t.fillcolor("red")
    t.begin_fill()
    t.setheading(-60)
    for _ in range(3):
        t.forward(22)
        t.left(120)
    t.end_fill()

    fill_rect(-10, -25, 20, 30, "red")


def draw_legs():
    # Legs
    for x in (-45, 35):
        go(x, -110)
        t.setheading(-90)
        t.forward(60)

    # Socks
    for x in (-45, 35):
        go(x, -145)
        t.setheading(0)
        t.forward(20)
        go(x, -152)
        t.forward(20)

    # Shoes
    for x in (-55, 25):
        go(x, -170)
        t.fillcolor("black")
        t.begin_fill()
        t.setheading(0)
        for _ in range(2):
            t.forward(40)
            t.circle(10, 90)
            t.forward(10)
            t.circle(10, 90)
        t.end_fill()


def draw_arms():
    # Left arm
    go(-140, -10)
    t.setheading(180)
    t.forward(70)

    go(-210, -10)
    t.setheading(-40)
    t.forward(20)

    # Right arm
    go(140, -10)
    t.setheading(0)
    t.forward(70)

    go(210, -10)
    t.setheading(-140)
    t.forward(20)

    # Hands
    fill_circle(-225, -27, 8, "yellow")
    fill_circle(225, -27, 8, "yellow")


def draw_body():
    fill_rect(-140, 140, 280, 230, "#f4d03f")


# Main drawing
t.hideturtle()
draw_body()
draw_sponge_holes()
draw_eyes()
draw_nose()
draw_mouth()
draw_shirt_and_tie()
draw_legs()
draw_arms()

turtle.done()
