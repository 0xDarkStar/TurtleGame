'''
This file has all the functions required to make a level.

All the functions here (excluding the lvl function and the collision function) is made to be called.

The lvl function is made by you. In the lvl function you draw the goal (if there is one), map, and other elements (traps, conveyors, portals, etc.).

The collision function is made by taking parts that you need and adding it to the collision function in your level file.

It is incomplete!
'''

# Required imports:
import turtle
from time import sleep
# from .lvlParts import *     Don't make it a comment when actually importing...

# Drawing walls:
def wall(go1, go2, head, walls, distance, wallDots): # Little function to make the code for drawing walls a bit smaller.
    walls.penup() # Lifts pen to not draw everywhere
    walls.goto(go1, go2) # Goes to starting position
    walls.setheading(head) # Looks in the correct direction
    walls.pendown() # Time to draw
    for a in range(distance): # Going for [distance] spaces
        for i in range(2):
            x = walls.xcor()
            y = walls.ycor()
            pos = (x, y) # Grabbed the position of the turtle
            wallDots += [pos] # Add it to the wallDots. Doesn't need to be manually added (lucky you)
            walls.forward(25) # Move forward 25, repeat once more
        x = walls.xcor()
        y = walls.ycor()
        pos = (x, y) # Grabbed the position of the turtle
        wallDots += [pos] # Add it to the wallDots. Doesn't ened to be manually added
    return wallDots

# Draw Goal and border
# 1. Normal
def goal(x, y, walls):
    walls.color("white")
    walls.fillcolor("light green")
    walls.begin_fill()
    trash = []
    trash = wall(x, y, 0, walls, 1, trash) # Goal
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
# 2. Mirror mode (goal is just landing on the characters, this only draws the border)
def border(walls):
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

# Draw one-way doors
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

# Draw portals (You need to make the portal list yourself, should be easy though)
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

# Main level function (calls all other functions to draw the map and set starting points)
# This is a template, do not use call this function from here
# Add the function to your own lvl.py script so it can draw everything
def lvl1(user):
    global walls, wallDots # include all the other turtles such as portalT, conveyorT, trapT. Only include them if you use them
    # If mirror, add userCopy to global
    walls = turtle.Turtle()
    walls.hideturtle()
    walls.speed(0)
    wallDots = []

    # Make the goal.
    # If mirror, do "border(walls)".
    # If normal call "goal(x, y, walls)".

    # Draw the map here.
    
    # Draw portals, conveyors, whatever you want to add to the map.

    # Set spawns
    '''
    If mirror add:
    userCopy = turtle.Turtle()
    userCopy.penup()
    userCopy.speed(0)
    userCopy.clear()
    xCopy = 0
    yCopy = 250
    userCopy.goto(xCopy, yCopy)
    userCopy.speed(1)
    userCopy.color("blue")
    userCopy.pensize(4)
    userCopy.pendown()
    userCopy.setheading(270)
    '''
    user.speed(0)
    user.showturtle()
    x = 0
    y = -250
    user.goto(x, y) # Spawn
    user.setheading(180) # Isn't required
    user.pendown()
    user.speed(1)

    return x, y
    # If mirror, add userCopy to return

# Lists
# If you want conveyors
conveyor1 = ["starting coord", "coord at bend", "another coord at another bend", "final coord (off the conveyor)"]

conveyors = {(0, 0): conveyor1, (25, 150): conveyor1}
#                    start                  end

# Collision function
# This is what checks if the player ran into a wall, tried to escape, or ran into something ont he map (trap, conveyor, etc.)
# This is meant to let you copy paste parts that you need.
# If you have several elifs that are about the same thing (check if character hit something, suer or userCopy, doesn't matter),
# then I recommend putting them next to each other to make it easier to find and change.
def collision(user, pen, door):
    xpos = user.xcor()
    ypos = user.ycor()
    pos = (xpos,ypos)
    ''' If mirror, add this:
    xposCopy = userCopy.xcor()
    yposCopy = userCopy.ycor()
    posCopy = (xposCopy,yposCopy)
    '''
    # This checks if the player is trying to escape the maze by going past the border.
    if ypos <= -275 or ypos >= 275 or xpos <= -275 or xpos >= 275:
        print("Don't try to leave my maze.", end = "\r")
        sleep(1)
        print("                                                            ", end = "\r")
        user.back(25)
    ''' If mirror, add this:
    elif yposCopy <= -275 or yposCopy >= 275 or xposCopy <= -275 or xposCopy >= 275:
        print("Don't try to get your copy to leave my maze.", end = "\r")
        sleep(1)
        print("                                                            ", end = "\r")
        userCopy.back(25)

    elif pos in wallDots and posCopy in wallDots: # Checks if both characters hit a wall
        print("Both of you hit a wall.", end = "\r")
        sleep(1)
        print("                                                            ", end = "\r")
        user.back(25)
        userCopy.back(25)
    '''
    # Having too many comments between elifs makes it mad, so don't do that
    # This might be commented out, but it is required for normal gameplay
    '''elif pos in wallDots: # Checks if player hit a wall
        print("You hit a wall.", end = "\r")
        sleep(1)
        print("                                                            ", end = "\r")
        user.back(25)
    '''
    # The above comment is required for normal gameplay, unless you want players phasing through walls

    ''' Add if you have conveyors
    elif pos in conveyors:
        if prevPos == conveyors[pos][-1]:
            turtles.goto(conveyors[pos][-1])
        else:
            for i in conveyors[pos]:
                turtles.goto(i)
    '''
    ''' If mirror, add this:
    elif posCopy in wallDots: # Checks if userCopy hit a wall
        print("Your copy hit a wall.", end = "\r")
        sleep(1)
        print("                                                            ", end = "\r")
        userCopy.back(25)
    elif pos == posCopy: # Checks if the two characters landed on each other
        Win = turtle.Turtle()
        Win.hideturtle()
        Win.goto(0,0)
        Win.write("YOU WON", False, align="center", font = ("Arial", 40, "bold") ) # Turtle is spawned to write "YOU WON" in center of screen
        sleep(2)
        door = "lvl5"
        # Clear all drawings (map, characters, conveyors, portals, etc.)
        pen.clear()
        user.clear()
        walls.clear()
        text.clear() # Add this line if you have text on the map.
        userCopy.clear()
        Win.clear()
        turtles.penup()
        turtles.hideturtle()
        userCopy.penup()
        userCopy.hideturtle()
        return door
    else:
        return door
    '''