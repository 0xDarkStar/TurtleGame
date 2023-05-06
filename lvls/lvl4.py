import turtle
from time import sleep
from .lvlParts import *

def lvl4(user):
    global userCopy, text, walls, wallDots
    walls = turtle.Turtle()
    wallDots = []
    border(walls)

    wallDots = wall(-275, 75, 0, walls, 5, wallDots)
    wallDots = wall(25, 75, 0, walls, 5, wallDots)

    wallDots = wall(-275, -75, 0, walls, 5, wallDots)
    wallDots = wall(25, -75, 0, walls, 5, wallDots)

    wallDots = wall(-275, 175, 0, walls, 2, wallDots)
    wallDots = wall(-125, 175, 0, walls, 5, wallDots)
    wallDots = wall(175, 175, 0, walls, 2, wallDots)

    wallDots = wall(-275, -175, 0, walls, 2, wallDots)
    wallDots = wall(-125, -175, 0, walls, 5, wallDots)
    wallDots = wall(175, -175, 0, walls, 2, wallDots)

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

def collision(turtles, pen, door): # Check if user is in a wall or out of bounds
    xpos = turtles.xcor()
    ypos = turtles.ycor()
    pos = (xpos,ypos)
    xposCopy = userCopy.xcor()
    yposCopy = userCopy.ycor()
    posCopy = (xposCopy,yposCopy)
    if ypos <= -275 or ypos >= 275 or xpos <= -275 or xpos >= 275:
        print("Don't try to leave my maze.", end = "\r")
        sleep(1)
        print("                                                            ", end = "\r")
        turtles.back(25)
    elif yposCopy <= -275 or yposCopy >= 275 or xposCopy <= -275 or xposCopy >= 275:
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