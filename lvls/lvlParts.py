'''
This file has all the functions required to make a level.

All the functions here (excluding the lvl function and the collision function) is made to be called.
'''

# Required imports:
import turtle
from time import sleep

# Map to draw:
mazePos = [
    [(-275, 275), (-250, 275), (-225, 275), (-200, 275), (-175, 275), (-150, 275), (-125, 275), (-100, 275), (-75, 275), (-50, 275), (-25, 275), (0, 275), (25, 275), (50, 275), (75, 275), (100, 275), (125, 275), (150, 275), (175, 275), (200, 275), (225, 275), (250, 275), (275, 275)],
    [(-275, 250), (-250, 250), (-225, 250), (-200, 250), (-175, 250), (-150, 250), (-125, 250), (-100, 250), (-75, 250), (-50, 250), (-25, 250), (0, 250), (25, 250), (50, 250), (75, 250), (100, 250), (125, 250), (150, 250), (175, 250), (200, 250), (225, 250), (250, 250), (275, 250)],
    [(-275, 225), (-250, 225), (-225, 225), (-200, 225), (-175, 225), (-150, 225), (-125, 225), (-100, 225), (-75, 225), (-50, 225), (-25, 225), (0, 225), (25, 225), (50, 225), (75, 225), (100, 225), (125, 225), (150, 225), (175, 225), (200, 225), (225, 225), (250, 225), (275, 225)],
    [(-275, 200), (-250, 200), (-225, 200), (-200, 200), (-175, 200), (-150, 200), (-125, 200), (-100, 200), (-75, 200), (-50, 200), (-25, 200), (0, 200), (25, 200), (50, 200), (75, 200), (100, 200), (125, 200), (150, 200), (175, 200), (200, 200), (225, 200), (250, 200), (275, 200)],
    [(-275, 175), (-250, 175), (-225, 175), (-200, 175), (-175, 175), (-150, 175), (-125, 175), (-100, 175), (-75, 175), (-50, 175), (-25, 175), (0, 175), (25, 175), (50, 175), (75, 175), (100, 175), (125, 175), (150, 175), (175, 175), (200, 175), (225, 175), (250, 175), (275, 175)],
    [(-275, 150), (-250, 150), (-225, 150), (-200, 150), (-175, 150), (-150, 150), (-125, 150), (-100, 150), (-75, 150), (-50, 150), (-25, 150), (0, 150), (25, 150), (50, 150), (75, 150), (100, 150), (125, 150), (150, 150), (175, 150), (200, 150), (225, 150), (250, 150), (275, 150)],
    [(-275, 125), (-250, 125), (-225, 125), (-200, 125), (-175, 125), (-150, 125), (-125, 125), (-100, 125), (-75, 125), (-50, 125), (-25, 125), (0, 125), (25, 125), (50, 125), (75, 125), (100, 125), (125, 125), (150, 125), (175, 125), (200, 125), (225, 125), (250, 125), (275, 125)],
    [(-275, 100), (-250, 100), (-225, 100), (-200, 100), (-175, 100), (-150, 100), (-125, 100), (-100, 100), (-75, 100), (-50, 100), (-25, 100), (0, 100), (25, 100), (50, 100), (75, 100), (100, 100), (125, 100), (150, 100), (175, 100), (200, 100), (225, 100), (250, 100), (275, 100)],
    [(-275, 75), (-250, 75), (-225, 75), (-200, 75), (-175, 75), (-150, 75), (-125, 75), (-100, 75), (-75, 75), (-50, 75), (-25, 75), (0, 75), (25, 75), (50, 75), (75, 75), (100, 75), (125, 75), (150, 75), (175, 75), (200, 75), (225, 75), (250, 75), (275, 75)],
    [(-275, 50), (-250, 50), (-225, 50), (-200, 50), (-175, 50), (-150, 50), (-125, 50), (-100, 50), (-75, 50), (-50, 50), (-25, 50), (0, 50), (25, 50), (50, 50), (75, 50), (100, 50), (125, 50), (150, 50), (175, 50), (200, 50), (225, 50), (250, 50), (275, 50)],
    [(-275, 25), (-250, 25), (-225, 25), (-200, 25), (-175, 25), (-150, 25), (-125, 25), (-100, 25), (-75, 25), (-50, 25), (-25, 25), (0, 25), (25, 25), (50, 25), (75, 25), (100, 25), (125, 25), (150, 25), (175, 25), (200, 25), (225, 25), (250, 25), (275, 25)],
    [(-275, 0), (-250, 0), (-225, 0), (-200, 0), (-175, 0), (-150, 0), (-125, 0), (-100, 0), (-75, 0), (-50, 0), (-25, 0), (0, 0), (25, 0), (50, 0), (75, 0), (100, 0), (125, 0), (150, 0), (175, 0), (200, 0), (225, 0), (250, 0), (275, 0)],
    [(-275, -25), (-250, -25), (-225, -25), (-200, -25), (-175, -25), (-150, -25), (-125, -25), (-100, -25), (-75, -25), (-50, -25), (-25, -25), (0, -25), (25, -25), (50, -25), (75, -25), (100, -25), (125, -25), (150, -25), (175, -25), (200, -25), (225, -25), (250, -25), (275, -25)],
    [(-275, -50), (-250, -50), (-225, -50), (-200, -50), (-175, -50), (-150, -50), (-125, -50), (-100, -50), (-75, -50), (-50, -50), (-25, -50), (0, -50), (25, -50), (50, -50), (75, -50), (100, -50), (125, -50), (150, -50), (175, -50), (200, -50), (225, -50), (250, -50), (275, -50)],
    [(-275, -75), (-250, -75), (-225, -75), (-200, -75), (-175, -75), (-150, -75), (-125, -75), (-100, -75), (-75, -75), (-50, -75), (-25, -75), (0, -75), (25, -75), (50, -75), (75, -75), (100, -75), (125, -75), (150, -75), (175, -75), (200, -75), (225, -75), (250, -75), (275, -75)],
    [(-275, -100), (-250, -100), (-225, -100), (-200, -100), (-175, -100), (-150, -100), (-125, -100), (-100, -100), (-75, -100), (-50, -100), (-25, -100), (0, -100), (25, -100), (50, -100), (75, -100), (100, -100), (125, -100), (150, -100), (175, -100), (200, -100), (225, -100), (250, -100), (275, -100)],
    [(-275, -125), (-250, -125), (-225, -125), (-200, -125), (-175, -125), (-150, -125), (-125, -125), (-100, -125), (-75, -125), (-50, -125), (-25, -125), (0, -125), (25, -125), (50, -125), (75, -125), (100, -125), (125, -125), (150, -125), (175, -125), (200, -125), (225, -125), (250, -125), (275, -125)],
    [(-275, -150), (-250, -150), (-225, -150), (-200, -150), (-175, -150), (-150, -150), (-125, -150), (-100, -150), (-75, -150), (-50, -150), (-25, -150), (0, -150), (25, -150), (50, -150), (75, -150), (100, -150), (125, -150), (150, -150), (175, -150), (200, -150), (225, -150), (250, -150), (275, -150)],
    [(-275, -175), (-250, -175), (-225, -175), (-200, -175), (-175, -175), (-150, -175), (-125, -175), (-100, -175), (-75, -175), (-50, -175), (-25, -175), (0, -175), (25, -175), (50, -175), (75, -175), (100, -175), (125, -175), (150, -175), (175, -175), (200, -175), (225, -175), (250, -175), (275, -175)],
    [(-275, -200), (-250, -200), (-225, -200), (-200, -200), (-175, -200), (-150, -200), (-125, -200), (-100, -200), (-75, -200), (-50, -200), (-25, -200), (0, -200), (25, -200), (50, -200), (75, -200), (100, -200), (125, -200), (150, -200), (175, -200), (200, -200), (225, -200), (250, -200), (275, -200)],
    [(-275, -225), (-250, -225), (-225, -225), (-200, -225), (-175, -225), (-150, -225), (-125, -225), (-100, -225), (-75, -225), (-50, -225), (-25, -225), (0, -225), (25, -225), (50, -225), (75, -225), (100, -225), (125, -225), (150, -225), (175, -225), (200, -225), (225, -225), (250, -225), (275, -225)],
    [(-275, -250), (-250, -250), (-225, -250), (-200, -250), (-175, -250), (-150, -250), (-125, -250), (-100, -250), (-75, -250), (-50, -250), (-25, -250), (0, -250), (25, -250), (50, -250), (75, -250), (100, -250), (125, -250), (150, -250), (175, -250), (200, -250), (225, -250), (250, -250), (275, -250)],
    [(-275, -275), (-250, -275), (-225, -275), (-200, -275), (-175, -275), (-150, -275), (-125, -275), (-100, -275), (-75, -275), (-50, -275), (-25, -275), (0, -275), (25, -275), (50, -275), (75, -275), (100, -275), (125, -275), (150, -275), (175, -275), (200, -275), (225, -275), (250, -275), (275, -275)],
]


# Make sure the turtles are in the right spot:
def Center(user): # Makes sure user doesn't get coords that are a float which wouldn't allow the walls to work.
    Nycor = round(user.ycor()) # Rounds the turtle's x coordinate
    Nxcor = round(user.xcor()) # Rounds the turtle's y coordinate
    user.goto(int(Nxcor), int(Nycor)) # Moves the turtle to the correct spot

# Drawing walls:
def wall(go1, go2, head, walls, distance): # Little function to make the code for drawing walls a bit smaller.
    walls.penup() # Lifts pen to not draw everywhere
    walls.goto(go1, go2) # Goes to starting position
    Center(walls)
    walls.setheading(head) # Looks in the correct direction
    walls.pendown() # Time to draw
    for a in range(distance): # Going for [distance] spaces
        walls.forward(25) # Move forward 25

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

def trap(x, y, trapT):
    go = (x, y)
    trapT.goto(go)
    trapT.setheading(90)
    trapT.forward(13)
    trapT.color("black")
    trapT.fillcolor("yellow")
    trapT.pendown()
    trapT.begin_fill()
    trapT.setheading(240)
    trapT.forward(25)
    trapT.setheading(0)
    trapT.forward(25)
    trapT.setheading(120)
    trapT.forward(25)
    trapT.end_fill()
    trapT.penup()
    trapT.goto(go)
    trapT.setheading(0)
    trapT.forward(2)
    trapT.setheading(270)
    trapT.forward(3)
    trapT.fillcolor("black")
    trapT.pendown()
    trapT.begin_fill()
    trapT.forward(4)
    trapT.right(90)
    trapT.forward(4)
    trapT.right(90)
    trapT.forward(4)
    trapT.right(90)
    trapT.forward(4)
    trapT.end_fill()
    trapT.penup()
    trapT.left(90)
    trapT.forward(2)
    trapT.pendown()
    trapT.begin_fill()
    trapT.forward(8)
    trapT.left(90)
    trapT.forward(4)
    trapT.left(90)
    trapT.forward(8)
    trapT.left(90)
    trapT.forward(4)
    trapT.end_fill()
    trapT.penup()

def chevron(x, y, angle, direction, chevrons):
    chevrons.setheading(direction)
    chevrons.forward(10.33)
    chevrons.pendown()
    chevrons.setheading(direction - 180)
    x1 = chevrons.xcor()
    y1 = chevrons.ycor()
    chevrons.right(angle)
    chevrons.forward(8)
    chevrons.left(angle)
    chevrons.forward(4)
    chevrons.right(180)
    chevrons.right(angle)
    chevrons.forward(8)

    chevrons.penup()
    chevrons.goto(x1, y1)
    chevrons.pendown()
    chevrons.setheading(direction - 180)
    chevrons.left(angle)
    chevrons.forward(8)
    chevrons.right(angle)
    chevrons.forward(4)
    chevrons.right(180)
    chevrons.left(angle)
    chevrons.forward(8)
    
    chevrons.penup()
    chevrons.goto(x, y)

    chevrons.setheading(direction)
    chevrons.forward(1.66)
    chevrons.pendown()
    chevrons.setheading(direction - 180)
    x1 = chevrons.xcor()
    y1 = chevrons.ycor()
    chevrons.right(angle)
    chevrons.forward(8)
    chevrons.left(angle)
    chevrons.forward(4)
    chevrons.right(180)
    chevrons.right(angle)
    chevrons.forward(8)

    chevrons.penup()
    chevrons.goto(x1, y1)
    chevrons.pendown()
    chevrons.setheading(direction - 180)
    chevrons.left(angle)
    chevrons.forward(8)
    chevrons.right(angle)
    chevrons.forward(4)
    chevrons.right(180)
    chevrons.left(angle)
    chevrons.forward(8)
    
    chevrons.penup()
    chevrons.goto(x, y)

def conveyor(x, y, angle, direction, distance, chevrons):
    chevrons.goto(x, y)
    chevrons.setheading(direction)
    a = 0
    while a < distance:
        x = chevrons.xcor()
        y = chevrons.ycor()
        chevron(x, y, angle, direction, chevrons)
        chevrons.setheading(direction)
        chevrons.forward(50)
        a += 1

def drawMap(mazeMap, walls): # This draws the map using an array!
    # Go in rows from top to bottom
    rowIndex = 0
    columnIndex = 0
    for i in mazeMap: # Cycle through the rows
        columnIndex = 0 # Select first item
        while columnIndex in range(len(i)): # Cycle through the items in the row
            j = i[columnIndex] # Select item
            if j == 1: # It says theres a wall
                start = columnIndex # Save starting point
                count = 0 # To keep track of how far to go
                columnIndex += 1 # To start on the next item
                while columnIndex in range(len(i)): # Go through the items to draw a wall
                    item = i[columnIndex] # Check this item
                    if item == 1: # If its a wall:
                        count += 1 # Add 1 to the length of the draw
                        columnIndex += 1 # Move to next item
                        if columnIndex == 23: # If it has gone out of range of the list
                            wall(mazePos[rowIndex][start][0], mazePos[rowIndex][start][1], 0, walls, count) # Draw it
                            break
                        continue
                    elif item != 1: # If it isn't a wall
                        if count != 0: # If it didn't only meet just one "1"
                            wall(mazePos[rowIndex][start][0], mazePos[rowIndex][start][1], 0, walls, count) # Draw the wall
                        break
            else:
                columnIndex += 1 # Move to next item until we hit another wall or when we move to the next row
        rowIndex += 1 # Move to the next row
    
    columnIndex = 0
    rowIndex = 0
    while columnIndex in range(len(mazeMap[0])): # Cycle through the columns
        rowIndex = 0 # Select first item
        while rowIndex in range(len(mazeMap)): # Cycle through items in the column
            j = mazeMap[rowIndex][columnIndex] # Select item
            if j == 1: # If the item is a wall
                start = rowIndex # Save starting point
                count = 0 # Start counting
                rowIndex += 1 # Move to next item
                while rowIndex in range(len(mazeMap)): # Cycle through the items in the column to draw a wall
                    item = mazeMap[rowIndex][columnIndex] # Select the item
                    if item == 1: # If item is a wall:
                        count += 1 # Add 1 to the length of the wall to be drawn
                        rowIndex += 1 # Move to next item
                        if rowIndex == 23: # If it has gone out of range
                            wall(mazePos[start][columnIndex][0], mazePos[start][columnIndex][1], 270, walls, count) # Draw the wall
                            break
                        continue
                    elif item != 1: # If it isn't a wall
                        if count != 0: # If it didn't only see one "1"
                            wall(mazePos[start][columnIndex][0], mazePos[start][columnIndex][1], 270, walls, count) # Draw the wall
                        break
            else:
                rowIndex += 1 # Move to next item
        columnIndex += 1 # Move to next column


class Collision:
    def __init__(self, mazeMap, user, walls, userCopy = 0, oneWay = 0, conveyors = 0):

        self.mazeMap = mazeMap
        self.walls = walls
        self.user = user
        self.oneWay = oneWay
        self.conveyors = conveyors
        self.userCopy = userCopy

    def userColl(self, pen, door):
        xpos = self.user.xcor()
        ypos = self.user.ycor()
        pos = (xpos,ypos)
        if self.wallColl() == False:
            return door
        return door

    def userCopyColl(self, pen, door):
        xpos = self.user.xcor()
        ypos = self.user.ycor()
        pos = (xpos,ypos)
        xpos1 = self.userCopy.xcor()
        ypos1 = self.userCopy.ycor()
        pos1 = (xpos1,ypos1)
        if self.wallCopyColl() == False:
            if ypos1 <= -275 or ypos1 >= 275 or xpos1 <= -275 or xpos1 >= 275:
                print("Don't try to get your copy to leave my maze.", end = "\r")
                sleep(1)
                print("                                                            ", end = "\r")
                self.userCopy.back(25)
            elif pos == pos1:
                Win = turtle.Turtle()
                Win.hideturtle()
                Win.goto(0,0)
                Win.write("YOU WON", False, align="center", font = ("Arial", 40, "bold") ) # Turtle is spawned to write "YOU WON" in center of screen
                sleep(2)
                door = "next"
                pen.clear()
                self.user.clear()
                self.walls.clear()
                self.userCopy.clear()
                Win.clear()
                self.user.penup()
                self.user.hideturtle()
                self.userCopy.penup()
                self.userCopy.hideturtle()
            return door
        return door
    
    def wallColl(self):
        xpos = self.user.xcor()
        ypos = self.user.ycor()
        pos = (xpos,ypos)
        for i in mazePos:
            if pos in i:
                columnIndex = i.index(pos)
                rowIndex = mazePos.index(i)
                if self.mazeMap[rowIndex][columnIndex] == 1:
                    print("You hit a wall.", end = "\r")
                    sleep(1)
                    print("                                                                           ", end = "\r")
                    self.user.back(25)
                    return True
                else:
                    return False
            else:
                continue

    def wallCopyColl(self):
        xpos1 = self.userCopy.xcor()
        ypos1 = self.userCopy.ycor()
        pos1 = (xpos1,ypos1)
        for i in mazePos:
            if pos1 in i:
                columnIndex = i.index(pos1)
                rowIndex = mazePos.index(i)
                if self.mazeMap[rowIndex][columnIndex] == 1:
                    print("Your copy hit a wall.", end = "\r")
                    sleep(1)
                    print("                                                                           ", end = "\r")
                    self.userCopy.back(25)
                    return True
                else:
                    return False
            else:
                continue

    def oneWayColl(self, door, prevPos, prevPosCopy):
        print("test")

    def check(self, pen, door, prevPos, prevPosCopy):
        door = self.userColl(pen, door)
        if self.userCopy != 0:
            door = self.userCopyColl(pen, door)
        if self.oneWay != 0:
            door = self.oneWayColl(door, prevPos, prevPosCopy)
        return door
