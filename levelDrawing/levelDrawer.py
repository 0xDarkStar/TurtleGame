import turtle
import keyboard
from time import sleep
import os.path

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

mazeMap = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

colorList = ["blue", "orange", "green", "pink"]

def Center(user): # Makes sure user doesn't get coords that are a float which wouldn't allow the walls to work.
    Nycor = round(user.ycor()) # Rounds the turtle's x coordinate
    Nxcor = round(user.xcor()) # Rounds the turtle's y coordinate
    user.goto(int(Nxcor), int(Nycor)) # Moves the turtle to the correct spot

def grabPos(turtle): # Grabs the position of the specified turtle
    x = turtle.xcor() # The reason I use this is because I want integers, not floats
    y = turtle.ycor()
    pos = (x, y)
    return pos

def grabXY(turtle): # Grabs the position of the specified turtle
    x = turtle.xcor() # The reason I use this is because I want integers, not floats
    y = turtle.ycor()
    return x, y

def portal(color, x, y, portalT):
    portalT.penup()
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
    portalT.pensize(1)
    portalT.penup()
    portalT.goto(x, y)

def oneWay(x, y, walls):
    walls.penup()
    head = None
    pos = grabPos(walls)
    for i in mazePos:
        if pos in i:
            columnIndex = i.index(pos)
            rowIndex = mazePos.index(i)
    if int(columnIndex/2)*2 == columnIndex or int(rowIndex/2)*2 == rowIndex:
        if mazeMap[rowIndex][columnIndex-1] == 1 and mazeMap[rowIndex][columnIndex+1] == 1:
            walls.goto(x-25, y)
            head = 0
        elif mazeMap[rowIndex-1][columnIndex] == 1 and mazeMap[rowIndex+1][columnIndex] == 1:
            walls.goto(x, y+25)
            head = 270
        walls.setheading(head)
        walls.forward(2)
        walls.color("white")
        b = 0
        while b <= 5:
            walls.forward(5)
            walls.penup()
            walls.forward(2)
            walls.pendown()
            b += 1
        walls.penup()
        walls.goto(x,y)

def changeSpace(user, currentState):
    if currentState != 0:
        pos = grabPos(user)
        for i in mazePos:
            if pos in i:
                columnIndex = i.index(pos)
                rowIndex = mazePos.index(i)
                break
        mazeMap[rowIndex][columnIndex] = currentState


def delSpace(user):
    pos = grabPos(user)
    for i in mazePos:
            if pos in i:
                columnIndex = i.index(pos)
                rowIndex = mazePos.index(i)
    mazeMap[rowIndex][columnIndex] = 0
    user.fillcolor("white")
    x = user.xcor()
    y = user.ycor()
    user.goto(x-24, y-24)
    user.begin_fill()
    user.goto(x+24, y-24)
    user.goto(x+24, y+24)
    user.goto(x-24, y+24)
    user.goto(x-24, y-24)
    user.end_fill()
    user.goto(x, y)

def findSpace(number = int, ignore = list, returnIndex = bool):
    columnIndex = 0
    rowIndex = 0
    for i in mazeMap:
        if number in i[ignore[0]+1:-1]:
            columnIndex = i[ignore[0]+1:-1].index(number)
            rowIndex = mazeMap.index(i)
            if columnIndex not in ignore or rowIndex not in ignore:
                if returnIndex == True:
                    return columnIndex, rowIndex
                else:
                    return mazePos[rowIndex][columnIndex]
                break
            else:
                continue
        rowIndex += 1
    
def moveFunc(move, user, currentState, instances, count):
    match move:
        
            case "w":
                user.setheading(90)
                if int(currentState/1000) == 6:
                    currentState = 6090
                    changeSpace(user, currentState)
                user.forward(25)
                Center(user)
                changeSpace(user, currentState)

            case "a":
                user.setheading(180)
                if int(currentState/1000) == 6:
                    currentState = 6180
                    changeSpace(user, currentState)
                user.forward(25)
                Center(user)
                changeSpace(user, currentState)

            case "d":
                user.setheading(0)
                if int(currentState/1000) == 6:
                    currentState = 6000
                    changeSpace(user, currentState)
                user.forward(25)
                Center(user)
                changeSpace(user, currentState)

            case "s":
                user.setheading(270)
                if int(currentState/1000) == 6:
                    currentState = 6270
                    changeSpace(user, currentState)
                user.forward(25)
                Center(user)
                changeSpace(user, currentState)

            case "q":
                delSpace(user)

            case "0":
                currentState = 0
                user.penup()
                user.color("black")

            case "1":
                currentState = 1
                user.color("black")
                user.pendown()
                changeSpace(user, currentState)
            
            case "2":
                currentState = 2
                changeSpace(user, currentState)
                user.color("red")
                user.pendown()
                user.circle(5)
                user.penup()
                currentState = 0
                user.color("black")
                user.speed(1)

            case "3":
                currentState = 3
                changeSpace(user, currentState)
                user.color("light green")
                x = user.xcor()
                y = user.ycor()
                user.goto(x-24, y-24)
                user.begin_fill()
                user.goto(x+24, y-24)
                user.goto(x+24, y+24)
                user.goto(x-24, y+24)
                user.goto(x-24, y-24)
                user.end_fill()
                user.goto(x, y)
                user.penup()
                currentState = 0
                user.color("black")
                user.speed(1)
            
            case "4":
                currentState = 4
                if instances == 1:
                    changeSpace(user, (currentState*10)+count)
                    x = user.xcor()
                    y = user.ycor()
                    portal(colorList[count-1], x, y, user)
                    instances += 1
                elif count == 4:
                    print("You have reached the max number of portals.")
                else:
                    count += 1
                    changeSpace(user, (currentState*10)+count)
                    x = user.xcor()
                    y = user.ycor()
                    portal(colorList[count-1], x, y, user)
                    instances = 1
                currentState = 0
                user.color("black")
                user.speed(1)

            case "5":
                currentState = 5
                changeSpace(user, currentState)
                x = user.xcor()
                y = user.ycor()
                oneWay(x, y, user)
                currentState = 0
                user.color("black")
                user.speed(1)

            case "6":
                currentState = 6
                user.color("gray")
                user.pendown()
                head = int(user.heading())
                currentState = 6000 + head
                changeSpace(user, currentState)

            case "7":
                currentState = 7
                changeSpace(user, currentState)
                user.color("yellow")
                user.pendown()
                user.circle(5)
                user.penup()
                currentState = 0
                user.color("black")
                user.speed(1)

            case "8":
                currentState = 8
                changeSpace(user, currentState)
                user.color("green")
                user.pendown()
                user.circle(5)
                user.penup()
                currentState = 0
                user.color("black")
                user.speed(1)

            case "9":
                currentState = 9
                changeSpace(user, currentState)
                user.color("blue")
                user.pendown()
                user.circle(5)
                user.penup()
                currentState = 0
                user.color("black")
                user.speed(1)
    return currentState

def loadMap(user, count, instances):
    currentState = 0
    mazeMap = []
    # Read the file line by line
    with open('mazeMap.txt', 'r') as file:
        for line in file:
            # Remove leading/trailing whitespace and the ending square bracket
            line = line.strip().rstrip(',')

            # Skip lines that don't contain matrix elements
            if not line.startswith('[') or not line.endswith(']'):
                continue

            # Evaluate the line as Python code and append it to the mpa
            mazeMap.append(eval(line))
    moves = []
    # Read the file line by line
    with open('moves.txt', 'r') as file:
        for line in file:
            # Remove leading/trailing whitespace

            # Skip empty lines or lines that don't contain a list
            if not line or not line.startswith('[') or not line.endswith(']'):
                continue

            # Evaluate the line as Python code and append it to the list
            moves.extend(eval(line))
    print(moves)
    for move in moves:
        moveFunc(move, user, currentState, instances, count)
    return count, instances

def saveMap(moves):
    map = str(mazeMap)
    map = map.replace("[[", "[\n    [")
    map = map.replace("], [", "],\n    [")
    map = map.replace("]]", "]\n]")
    if os.path.isfile('./mazeMap.txt'):
        with open("mazeMap.txt", "w") as file:
            file.write(f"mazeMap = {map}")
    else:
        with open("mazeMap.txt", "x") as file:
            file.write(f"mazeMap = {map}")
    move = str(moves)
    if os.path.isfile('./moves.txt'):
        with open("moves.txt", "w") as file:
            file.write(f"{move}")
    else:
        with open("moves.txt", "x") as file:
            file.write(f"{move}")

def drawGrid(onOff, grid):
    if onOff == "on":
        grid = turtle.Turtle()
        grid.penup()
        grid.hideturtle()
        grid.color("light blue")
        grid.speed(0)
        count = 0
        for j in mazePos[0]:
            if int(count/2)*2 == count:
                grid.goto(j)
                grid.pendown()
                grid.setheading(270)
                grid.forward(550)
                grid.penup()
            count += 1
        count = 0
        for i in mazePos:
            j = i[0]
            if int(count/2)*2 == count:
                grid.goto(j)
                grid.pendown()
                grid.setheading(0)
                grid.forward(550)
                grid.penup()
            count += 1
        return grid
    elif onOff == "off":
        grid.clear()
        return grid

def moveNorm():
    moves = []
    onOff = "on" # Do we want the grid on or off?
    grid = None
    grid = drawGrid(onOff, grid)
    user = turtle.Turtle()
    user.penup()
    user.shape("circle")
    a = 0
    currentState = 0
    instances = 0
    count = 0
    turn = 0
    print(
"""
/-------------------------\\
| w = up                  |
| d = right               |
| a = left                |
| s = down                |
| ~ = set space to 0      |
| 0 = empty               |
| 1 = wall                |
| 2 = user spawn          |
| 3 = goal                |
| 4 = portal (4 pairs max)|
| 5 = one-way door        |
| 6 = conveyor            |
| 7 = trap                |
| 8 = bot spawn           |
| 9 = userCopy spawn      |
| l = print maze          |
| e = exit                |
| g = grid on/off         |
\-------------------------/
""")
    loadMapYN = input("Do you want to load the previously saved map? (y/n) ").lower()
    if loadMapYN == "y":
            count, instances = loadMap(user, count, instances)
    while a >= 0: # Menu to allow user to move
        if int(turn/10)*10 == turn:
                saveMap(moves)
        match keyboard.read_key():
        
            case "w":
                moves.append("w")
                user.setheading(90)
                if int(currentState/1000) == 6:
                    currentState = 6090
                    changeSpace(user, currentState)
                user.forward(25)
                Center(user)
                changeSpace(user, currentState)
                turn += 1

            case "a":
                moves.append("a")
                user.setheading(180)
                if int(currentState/1000) == 6:
                    currentState = 6180
                    changeSpace(user, currentState)
                user.forward(25)
                Center(user)
                changeSpace(user, currentState)
                turn += 1

            case "d":
                moves.append("d")
                user.setheading(0)
                if int(currentState/1000) == 6:
                    currentState = 6000
                    changeSpace(user, currentState)
                user.forward(25)
                Center(user)
                changeSpace(user, currentState)
                turn += 1

            case "s":
                moves.append("s")
                user.setheading(270)
                if int(currentState/1000) == 6:
                    currentState = 6270
                    changeSpace(user, currentState)
                user.forward(25)
                Center(user)
                changeSpace(user, currentState)
                turn += 1

            case "q":
                moves.append("q")
                delSpace(user)
                turn += 1

            case "0":
                moves.append("0")
                currentState = 0
                user.penup()
                user.color("black")
                turn += 1

            case "1":
                moves.append("1")
                currentState = 1
                user.color("black")
                user.pendown()
                changeSpace(user, currentState)
                turn += 1
            
            case "2":
                moves.append("2")
                currentState = 2
                changeSpace(user, currentState)
                user.color("red")
                user.pendown()
                user.circle(5)
                user.penup()
                currentState = 0
                user.color("black")
                user.speed(1)
                turn += 1

            case "3":
                moves.append("3")
                currentState = 3
                changeSpace(user, currentState)
                user.color("light green")
                x = user.xcor()
                y = user.ycor()
                user.goto(x-24, y-24)
                user.begin_fill()
                user.goto(x+24, y-24)
                user.goto(x+24, y+24)
                user.goto(x-24, y+24)
                user.goto(x-24, y-24)
                user.end_fill()
                user.goto(x, y)
                user.penup()
                currentState = 0
                user.color("black")
                user.speed(1)
                turn += 1
            
            case "4":
                moves.append("4")
                currentState = 4
                if instances == 1:
                    changeSpace(user, (currentState*10)+count)
                    x = user.xcor()
                    y = user.ycor()
                    portal(colorList[count-1], x, y, user)
                    instances += 1
                elif count == 4:
                    print("You have reached the max number of portals.")
                else:
                    count += 1
                    changeSpace(user, (currentState*10)+count)
                    x = user.xcor()
                    y = user.ycor()
                    portal(colorList[count-1], x, y, user)
                    instances = 1
                currentState = 0
                user.color("black")
                user.speed(1)
                turn += 1
                

            case "5":
                moves.append("5")
                currentState = 5
                changeSpace(user, currentState)
                x = user.xcor()
                y = user.ycor()
                oneWay(x, y, user)
                currentState = 0
                user.color("black")
                user.speed(1)
                turn += 1

            case "6":
                moves.append("6")
                currentState = 6
                user.color("gray")
                user.pendown()
                head = int(user.heading())
                currentState = 6000 + head
                changeSpace(user, currentState)
                turn += 1


            case "7":
                moves.append("7")
                currentState = 7
                changeSpace(user, currentState)
                user.color("yellow")
                user.pendown()
                user.circle(5)
                user.penup()
                currentState = 0
                user.color("black")
                user.speed(1)
                turn += 1

            case "8":
                moves.append("8")
                currentState = 8
                changeSpace(user, currentState)
                user.color("green")
                user.pendown()
                user.circle(5)
                user.penup()
                currentState = 0
                user.color("black")
                user.speed(1)
                turn += 1

            case "9":
                moves.append("9")
                currentState = 9
                changeSpace(user, currentState)
                user.color("blue")
                user.pendown()
                user.circle(5)
                user.penup()
                currentState = 0
                user.color("black")
                user.speed(1)
                turn += 1
            
            case "l":
                print(mazeMap)
                sleep(2)

            case "p":
                saveMap(moves)
                print("Your maze has been saved to: mazeMap.txt")

            case "e":
                while a == 0:
                    answer = input("Do you want to save? (y/n) ").lower()
                    if answer == "y":
                        saveMap(moves)
                        print("Your maze has been saved to: mazeMap.txt")
                        name = input("What do you want to name your file? Do not add the file format.\nIf you name it another file, it will overwrite it. ")
                        if name == f"{name}Drawer":
                            name = f"{name}"
                        print(f"The level using your maze has been made in: {name}.py")
                        return name
                    elif answer == "n":
                        exit()
                    else:
                        continue

            case "g":
                if onOff == "on":
                    onOff = "off"
                    grid = drawGrid(onOff, grid)
                    sleep(.5)
                else:
                    onOff = "on"
                    grid = drawGrid(onOff, grid)
        

def makePortalList(number, file, color):
    column, row = findSpace(number, [-1], True)
    port1Pos = mazePos[row][column]
    port2Pos = findSpace(number, [column, row], False)
    file.write(f"{color}Portal = [{str(port1Pos)}, {str(port2Pos)}]\n")
                 
def makeLevel(name):
    map = str(mazeMap)
    map = map.replace("[[", "[\n    [")
    map = map.replace("], [", "],\n    [")
    map = map.replace("]]", "]\n]")
    if os.path.isfile(f'./{name}.py'):
        with open(f"{name}.py", "w") as file:
            file.write(
f"""# You can do whatever you want with this file now.
import turtle
from time import sleep
from .lvlParts import drawMap, Collision
from .movement import movement

def lvl(user, pen):
    walls = turtle.Turtle()
    walls.speed(0)
    walls.hideturtle()

    '''
    Map guide:
    0 = empty
    1 = wall
    2 = user spawn
    3 = goal
    4 = portals
    5 = one-way doors
    6 = conveyors
    7 = traps
    8 = enemy spawn
    9 = userCopy spawn
    '''

    mazeMap = {map}
    userCopy, bot = drawMap(mazeMap, walls, user)

    collision = Collision(mazeMap, user, walls, userCopy, bot)\n
""")
    else:
        with open(f"{name}.py", "x") as file:
            file.write(
f""" # Copy this to your level file
import turtle
from time import sleep
from .lvlParts import drawMap, Collision
from .movement import movement

def lvl(user, pen):
    walls = turtle.Turtle()
    walls.speed(0)
    walls.hideturtle()

    '''
    Map guide:
    0 = empty
    1 = wall
    2 = user spawn
    3 = goal
    4 = portals
    5 = one-way doors
    6 = conveyors
    7 = traps
    8 = enemy spawn
    9 = userCopy spawn
    '''

    mazeMap = {map}
    userCopy, bot = drawMap(mazeMap, walls, user)

    collision = Collision(mazeMap, user, walls, userCopy, bot)

""")
    if ", 41," in map:
        with open(f"{name}.py", "a") as file:
            file.write('    menu = "/-------------\\\\n| w = up      |\\n| d = right   |\\n| a = left    |\\n| s = down    |\\n| ~ = quit    |\\n| r = reset   |\\n| t = teleport |\\n\-------------/\\n"\n')
    else:
        with open(f"{name}.py", "a") as file:
            file.write('    menu = "/-------------\\\\n| w = up      |\\n| d = right   |\\n| a = left    |\\n| s = down    |\\n| ~ = quit    |\\n| r = reset   |\\n|              |\\n\-------------/\\n"\n')

    if ", 9," in map and ", 8," in map:
        pos = findSpace(2, [-1], False)
        posC = findSpace(9, [-1], False)
        posB = findSpace(8, [-1], False)
        with open(f"{name}.py", "a") as file:
            file.write(f'    reset = [{str(pos)}, {str(posC)}, {str(posB)}]\n')
        if ", 41," in map:
            with open(f"{name}.py", "a") as file:
                file.write(f'    movement(user, pen, menu, collision, teleport, bot, reset, userCopy)\n')
        else:
            with open(f"{name}.py", "a") as file:
                file.write(f'    movement(user, pen, menu, collision, 0, bot, reset, userCopy)\n')
    elif ", 9," in map:
        pos = findSpace(2, [-1], False)
        posC = findSpace(9, [-1], False)
        with open(f"{name}.py", "a") as file:
            file.write(f'    reset = [{str(pos)}, {str(posC)}]\n')
        if ", 41," in map:
            with open(f"{name}.py", "a") as file:
                file.write(f'    movement(user, pen, menu, collision, teleport, 0, reset, userCopy)\n')
        else:
            with open(f"{name}.py", "a") as file:
                file.write(f'    movement(user, pen, menu, collision, 0, 0, reset, userCopy)\n')
    elif ", 8," in map:
        pos = findSpace(2, [-1], False)
        posB = findSpace(8, [-1], False)
        with open(f"{name}.py", "a") as file:
            file.write(f'    reset = [{str(pos)}, {str(posB)}]\n')
        if ", 41," in map:
            with open(f"{name}.py", "a") as file:
                file.write(f'    movement(user, pen, menu, collision, teleport, bot, reset, 0)\n')
        else:
            with open(f"{name}.py", "a") as file:
                file.write(f'    movement(user, pen, menu, collision, 0, bot, reset, 0)\n')
    else:
        pos = findSpace(2, [-1], False)
        with open(f"{name}.py", "a") as file:
            file.write(f'    reset = [{str(pos)}]\n')
        if ", 41," in map:
            with open(f"{name}.py", "a") as file:
                file.write(f'    movement(user, pen, menu, collision, teleport, 0, reset, 0)\n\n')
        else:
            with open(f"{name}.py", "a") as file:
                file.write(f'    movement(user, pen, menu, collision, 0, 0, reset, 0)\n')
    if ", 41," in map:
        with open(f"{name}.py", "a") as file:
            makePortalList(41, file, "blue")
            if ", 44," in map:
                makePortalList(42, file, "orange")
                makePortalList(43, file, "green")
                makePortalList(44, file, "pink")
                file.write("portals = [bluePortal, orangePortal, greenPortal, pinkPortal]\n\n")
            elif ", 43," in map:
                makePortalList(42, file, "orange")
                makePortalList(43, file, "green")
                file.write("portals = [bluePortal, orangePortal, greenPortal]\n\n")
            elif ", 42," in map:
                makePortalList(42, file, "orange")
                file.write("portals = [bluePortal, orangePortal]\n\n")
            else:
                file.write("portals = [bluePortal]")
            file.write(f"""
def teleport(input, user): # Find the portal that the player is at
    indeX = 0
    while indeX < 4: # Cycle through the portal list
        if input in portals[indeX]:
            break # Player is on a portal, return the index (Line 59 is called after this function when this is the result)
        else:
            indeX += 1
    if indeX != 4: # It reached the end of the list
        playerPort = portals[indeX].index(input)
        portal = portals[indeX]
        if playerPort == 0:
            endPort = portal[1]
            user.penup()
            user.goto(endPort)
            user.pendown()
        else:
            endPort = portal[0]
            user.penup()
            user.goto(endPort)
            user.pendown()
        return True
    else:
        return False
""")
name = moveNorm()
makeLevel(name)
