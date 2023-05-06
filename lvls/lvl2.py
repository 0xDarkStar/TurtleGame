import turtle
from time import sleep

def wall(go1, go2, head, walls): #little function to make the code for drawing walls a bit smaller
    walls.penup()
    walls.goto(go1, go2)
    walls.setheading(head)
    walls.pendown()
    walls.forward(50)

def goal(x, y, walls):
    walls.color("white")
    walls.fillcolor("light green")
    walls.begin_fill()
    wall(x, y, 0, walls) # Goal
    walls.right(90)
    walls.forward(50)
    walls.right(90)
    walls.forward(50)
    walls.right(90)
    walls.forward(50)
    walls.end_fill()
    walls.color("black")

    # border
    walls.penup()
    walls.goto(275, 275)
    walls.setheading(270)
    walls.hideturtle()
    walls.pendown()# Border
    walls.forward(550)
    walls.right(90)
    walls.forward(550)
    walls.right(90)
    walls.forward(550)
    walls.right(90)
    walls.forward(550) # Border done

def oneWay(x, y, head, walls, color):
    walls.penup()
    walls.goto(x, y)
    walls.setheading(head)
    walls.forward(2)
    walls.color(color)
    b = 0
    while b <= 5:
        walls.forward(5)
        walls.penup()
        walls.forward(2)
        walls.pendown()
        b += 1

def portal(color, x, y, portalT):
    portalT.penup()
    portalT.hideturtle()
    portalT.speed(0)
    portalT.goto(x, y + 7.071)
    portalT.color(color)
    portalT.pensize(2)
    portalT.setheading(-45)
    a = 0
    portalT.begin_fill()
    while a < 4:
        portalT.forward(10)
        portalT.right(90)
        a += 1
    portalT.end_fill()

def lvl2(user):
    global portalT, walls
    walls = turtle.Turtle()
    walls.speed(0)

    goal(-25, 25, walls)

    wall(-225, 275, 270, walls)
    walls.forward(50)
    
    wall(-275, 125, 0, walls)
    walls.forward(50)
    walls.left(90)
    walls.forward(100)

    wall(-125, 275, 270, walls)
    walls.forward(100)
    walls.left(90)
    walls.forward(50)
    walls.left(90)
    walls.forward(50)
    walls.left(180)
    walls.forward(200)
    walls.left(90)
    walls.forward(100)
    walls.left(90)
    walls.forward(50)
    walls.left(90)
    walls.forward(50)
    walls.right(90)
    walls.forward(50)
    walls.right(90)
    walls.forward(100)
    walls.right(90)
    walls.forward(300)
    walls.right(90)
    walls.forward(100)

    wall(-125, 225, 0, walls)
    walls.forward(50)
    walls.right(90)
    walls.forward(50)
    walls.left(90)
    walls.forward(150)
    walls.right(90)
    walls.forward(150)
    walls.left(90)
    walls.forward(50)
    walls.left(90)
    walls.forward(200)
    walls.right(90)
    walls.forward(50)
    walls.right(90)
    walls.forward(200)
    walls.left(90)
    walls.forward(50)

    wall(175, 225, 180, walls)
    walls.forward(100)

    wall(125, 125, 180, walls)
    walls.forward(100)

    wall(225, -225, 90, walls)
    walls.forward(150)
    walls.left(90)
    walls.forward(100)
    walls.left(90)
    walls.forward(250)

    wall(175, -275, 90, walls)
    walls.forward(150)

    wall(25, -25, 270, walls)
    walls.forward(100)
    walls.left(90)
    walls.forward(50)
    walls.right(180)
    walls.forward(250)
    walls.right(180)
    walls.forward(50)
    walls.left(90)
    walls.forward(250)
    walls.left(90)
    walls.forward(50)
    walls.left(90)
    walls.forward(150)
    walls.right(90)
    walls.forward(100)

    wall(-275, 75, 0, walls)
    walls.right(90)
    walls.forward(100)

    wall(-75, -175, 270, walls)
    walls.forward(50)
    walls.back(50)
    walls.right(90)
    walls.forward(150)
    walls.right(90)
    walls.forward(100)
    walls.right(90)
    walls.forward(50)

    wall(25, -125, 180, walls)
    walls.forward(50)
    walls.right(90)
    walls.forward(50)
    walls.right(90)
    walls.forward(100)
    oneWay(-25, -75, 0, walls, "white")

    portalT = turtle.Turtle()
    portal("pink", -250, 50, portalT)
    portal("pink", -150, 50, portalT)
    portal("blue", 250, 50, portalT)
    portal("blue", -100, -250, portalT)
    portal("green", 200, 200, portalT)
    portal("green", 150, 50, portalT)
    portal("purple", 0, 50, portalT)
    portal("purple", 150, -250, portalT)

    user.speed(0)
    user.showturtle()
    user.goto(-250, 250) # true start
    #user.goto(-250, -200) # just to test
    user.setheading(270)
    user.pendown()
    user.speed(1)

wallDots = [(175, -75), (175, -100), (175, -125), (175, -150), (175, -175), (175, -200), (175, -225), (175, -250), (225, -225), (225, -200), (225, -175), (225, -150), (225, -125), (225, -100), (225, -75), (225, -50), (225, -25), (200, -25), (175, -25), (150, -25), (125, -25),(125, -250), (125, -225), (125, -200), (125, -175), (125, -150), (125, -125), (125, -100), (125, -75), (125, -50), (125, -25), (225, 25), (225, 50), (225, 75), (225, 100), (225, 125), (225, 150), (225, 175), (225, 200), (225, 225), (250, 25), (200, 225), (175, 225), (150, 225), (125, 225), (100, 225), (75, 225), (25, 225), (175, 200), (175, 175), (175, 150), (175, 125), (175, 100), (175, 75), (175, 50), (175, 25), (150, 25), (125, 25), (125, 50), (125, 75), (125, 100), (125, 125), (125, 150), (125, 175), (100, 125), (75, 125), (50, 125), (25, 125), (0, 125), (-25, 125), (100, 175), (75, 175), (25, 175), (0, 175), (-25, 175), (-25, 200), (-25, 225), (-50, 225), (-75, 225), (-100, 225), (-125, 225), (-125, 250), (-125, 200), (-125, 175), (-125, 150), (-125, 125), (-100, 125), (-75, 125), (-75, 150), (-75, 175), (-75, 100), (-75, 75), (-75, 50), (-75, 25), (-75, 0), (-75, -25), (-50, -25), (-25, -25), (0, -25), (25, -25), (25, 0), (25, 25), (25, -50), (25, -75), (25, -100), (25, -125), (25, -150), (25, -175), (50, -175), (75, -175), (75, -150), (75, -125), (75, -100), (75, -75), (75, -50), (75, -25), (75, 0), (75, 25), (75, 50), (75, 75), (50, 75), (25, 75), (0, 75), (-25, 75), (-25, 50), (-25, 25), (0, 25), (50, 175), (50, 225), (75, -200), (75, -225), (50, -225), (25, -225), (0, -225), (-25, -225), (0, -175), (-25, -175), (-50, -175), (-75, -175), (-100, -175), (-125, -175), (-150, -175), (-175, -175), (-125, -150), (-125, -125), (-125, -100), (-125, -75), (-125, -50), (-125, -25), (-125, 0), (-125, 25), (-125, 50), (-125, 75), (-150, 75), (-175, 75), (-175, 50), (-175, 25), (-175, 0), (-175, -25), (-175, -50), (-175, -75), (-200, -75), (-225, -75), (-250, -75), (-250, 75), (-225, 75), (-225, 50), (-225, 25), (-225, 0), (-225, -25), (0, -125), (-25, -125), (-50, -125), (-75, -125), (-75, -100), (-75, -75), (-50, -75), (-25, -75), (-175, -125), (-200, -125), (-225, -125), (-225, -150), (-225, -175), (-225, -200), (-225, -225), (-200, -225), (-175, -225), (-150, -225), (-125, -225), (-100, -225), (-75, -225), (-75, -200), (-75, -250), (-225, 250), (-225, 225), (-225, 200), (-225, 175), (-175, 225), (-175, 200), (-175, 175), (-175, 150), (-175, 125), (-200, 125), (-225, 125), (-250, 125)]

def collision(turtles, pen, door): # Check if user is in a wall or out of bounds
    xpos = turtles.xcor()
    ypos = turtles.ycor()
    pos = (xpos,ypos)
    if ypos <= -275 or ypos >= 275:
        print("Don't try to leave my maze.", end = "\r")
        sleep(1)
        print("                                          ", end = "\r")
        turtles.back(25)
    elif xpos <= -275 or xpos >= 275:
        print("Don't try to leave my maze.", end = "\r")
        sleep(1)
        print("                                          ", end = "\r")
        turtles.back(25)
    elif pos in wallDots:
        print("You hit a wall.", end = "\r")
        sleep(1)
        print("                                          ", end = "\r")
        turtles.back(25)
    elif xpos <= 24 and xpos >= -24 and ypos <= 24 and ypos >= -24: # Checks if they made it to the goal
        Win = turtle.Turtle()
        Win.hideturtle()
        Win.goto(0,0)
        Win.write("YOU WON", False, align="center", font = ("Arial", 40, "bold") ) # Turtle is spawned to write "YOU WON" in center of screen
        sleep(2)
        door = "lvl3"
        pen.clear()
        turtles.clear()
        walls.clear()
        portalT.clear()
        Win.clear()
        turtles.penup()
        turtles.hideturtle()
        return door
    elif pos == (0, -50):
        if door != "open":
            oneWay(-25, -75, 0, walls, "light green")
            door = "open"
        return door      
    elif pos == (0, -100):
        if door != "closed":
            oneWay(-25, -75, 0, walls, "red")
            door = "closed"
        return door
    elif pos == (0, -75):
        if turtles.heading() == 270:
            turtles.forward(25)
        elif turtles.heading() == 90:
            turtles.back(25)
        else:
            print("I don't know how you went into the door through a wall or sideways.\nThere should be no way.", end = "\r")
            sleep(1)
            print("                                          ", end = "\r")

    else:
        return door