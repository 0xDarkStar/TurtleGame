import turtle
from time import sleep

def wall(go1, go2, head, walls, distance): #little function to make the code for drawing walls a bit smaller
    walls.penup()
    walls.goto(go1, go2)
    walls.setheading(head)
    walls.pendown()
    walls.forward(distance)

def goal(x, y, walls):
    walls.color("light green")
    wall(x, y, 0, walls, 550) # Goal
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

def lvl4(user):
    global userCopy, text, walls
    walls = turtle.Turtle()
    goal(-275, 0, walls)

    wall(-275, 75, 0, walls, 250)
    wall(25, 75, 0, walls, 250)

    wall(-275, -75, 0, walls, 250)
    wall(25, -75, 0, walls, 250)

    wall(-275, 175, 0, walls, 100)
    wall(-125, 175, 0, walls, 250)
    wall(175, 175, 0, walls, 100)

    wall(-275, -175, 0, walls, 100)
    wall(-125, -175, 0, walls, 250)
    wall(175, -175, 0, walls, 100)

    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.speed(0)
    text.goto(0, -250)
    text.write("This is you", False, "Center", font = ("Arial", 12, "bold"))
    text.goto(0, 250)
    text.write("This is your copy", False, "Center", font = ("Arial", 12, "bold"))
    text.goto(0, 25)
    text.write("Your copy does the opposite of what you do", False, "Center", font = ("Arial", 12, "bold"))
    text.goto(0, -25)
    text.write("The goal in these levels is to land on your copy", False, "Center", font = ("Arial", 12, "bold"))

    userCopy = turtle.Turtle()
    userCopy.penup()
    userCopy.speed(0)
    userCopy.clear()
    userCopy.goto(0, 250)
    userCopy.speed(1)
    userCopy.color("blue")
    userCopy.pensize(4)
    userCopy.pendown()
    userCopy.setheading(270)

    user.speed(0)
    user.penup()
    user.showturtle()
    user.goto(0, -250)
    user.speed(1)
    user.pendown()
    user.setheading(90)

    return userCopy

wallDots = [(-250, 175), (-250, 75), (-250, -75), (-250, -175), (-225, 175), (-225, 75), (-225, -75), (-225, -175), (-200, 175), (-200, 75), (-200, -75), (-200, -175), (-175, 175), (-175, 75), (-175, -75), (-175, -175), (-150, 75), (-150, -75), (-125, 175), (-125, 75), (-125, -75), (-125, -175), (-100, 175), (-100, 75), (-100, -75), (-100, -175), (-75, 175), (-75, 75), (-75, -75), (-75, -175), (-50, 175), (-50, 75), (-50, -75), (-50, -175), (-25, 175), (-25, 75), (-25, -75), (-25, -175), (0, 175), (0, -175), (25, 175), (25, 75), (25, -75), (25, -175), (50, 175), (50, 75), (50, -75), (50, -175), (75, 175), (75, 75), (75, -75), (75, -175), (100, 175), (100, 75), (100, -75), (100, -175), (125, 175), (125, 75), (125, -75), (125, -175), (150, 75), (150, -75), (175, 175), (175, 75), (175, -75), (175, -175), (200, 175), (200, 75), (200, -75), (200, -175), (225, 175), (225, 75), (225, -75), (225, -175), (250, 175), (250, 75), (250, -75), (250, -175)]

def collision(turtles, pen, door): # Check if user is in a wall or out of bounds
    xpos = turtles.xcor()
    ypos = turtles.ycor()
    pos = (xpos,ypos)
    xposCopy = userCopy.xcor()
    yposCopy = userCopy.ycor()
    posCopy = (xposCopy,yposCopy)
    if ypos <= -275 or ypos >= 275:
        print("Don't try to leave my maze.", end = "\r")
        sleep(1)
        print("                                                            ", end = "\r")
        turtles.back(25)
    elif xpos <= -275 or xpos >= 275:
        print("Don't try to leave my maze.", end = "\r")
        sleep(1)
        print("                                                            ", end = "\r")
        turtles.back(25)
    if yposCopy <= -275 or yposCopy >= 275:
        print("Don't try to get your copy to leave my maze.", end = "\r")
        sleep(1)
        print("                                                            ", end = "\r")
        userCopy.back(25)
    elif xposCopy <= -275 or xposCopy >= 275:
        print("Don't try to get your copy to leave my maze.", end = "\r")
        sleep(1)
        print("                                                            ", end = "\r")
        userCopy.back(25)
    elif pos in wallDots and posCopy in wallDots:
        print("Both of you hit a wall.", end = "\r")
        sleep(1)
        print("                                                            ", end = "\r")
        turtles.back(25)
        userCopy.back(25)
    elif pos in wallDots:
        print("You hit a wall.", end = "\r")
        sleep(1)
        print("                                                            ", end = "\r")
        turtles.back(25)
    elif posCopy in wallDots:
        print("Your copy hit a wall.", end = "\r")
        sleep(1)
        print("                                                            ", end = "\r")
        userCopy.back(25)
    elif pos == posCopy: # Checks if they made it to the goal
        Win = turtle.Turtle()
        Win.hideturtle()
        Win.goto(0,0)
        Win.write("YOU WON", False, align="center", font = ("Arial", 40, "bold") ) # Turtle is spawned to write "YOU WON" in center of screen
        sleep(2)
        door = "lvl5"
        pen.clear()
        turtles.clear()
        walls.clear()
        text.clear()
        userCopy.clear()
        Win.clear()
        turtles.penup()
        turtles.hideturtle()
        userCopy.penup()
        userCopy.hideturtle()
        return door
    else:
        return door