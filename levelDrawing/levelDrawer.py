import turtle
import keyboard
from time import sleep

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
    if mazeMap[rowIndex][columnIndex-1] == 1 and mazeMap[rowIndex][columnIndex+1] == 1:
        walls.goto(x-25, y)
        head = 0
    elif mazeMap[rowIndex-1][columnIndex] == 1 and mazeMap[rowIndex+1][columnIndex] == 1:
        walls.goto(x, y+25)
        head = 270
    if head != None:
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

def saveMap():
    map = str(mazeMap)
    map = map.replace("[[", "[\n    [")
    map = map.replace("], [", "],\n    [")
    map = map.replace("]]", "]\n]")
    with open("mazeMap.txt", "w") as file:
        file.write(f"mazeMap = {map}")

def drawGrid():
    grid = turtle.Turtle()
    grid.penup()
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

def moveNorm():
    drawGrid()
    user = turtle.Turtle()
    user.penup()
    user.shape("circle")
    a = 0
    currentState = 0
    instances = 0
    while a >= 0: # Menu to allow user to move
        if keyboard.is_pressed("w"):
            user.setheading(90)
            user.forward(25)
            Center(user)
            changeSpace(user, currentState)

        elif keyboard.is_pressed("a"):
            user.setheading(180)
            user.forward(25)
            Center(user)
            changeSpace(user, currentState)

        elif keyboard.is_pressed("d"):
            user.setheading(0)
            user.forward(25)
            Center(user)
            changeSpace(user, currentState)

        elif keyboard.is_pressed("s"):
            user.setheading(270)
            user.forward(25)
            Center(user)
            changeSpace(user, currentState)

        elif keyboard.is_pressed("grave"):
            delSpace(user)

        elif keyboard.is_pressed("0"):
            currentState = 0
            user.penup()

        elif keyboard.is_pressed("1"):
            currentState = 1
            user.color("black")
            user.pendown()
        
        elif keyboard.is_pressed("2"):
            currentState = 2
            changeSpace(user, currentState)
            user.color("red")
            user.pendown()
            user.circle(5)
            user.penup()
            currentState = 0
            user.color("black")
            user.speed(1)

        elif keyboard.is_pressed("3"):
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
        
        elif keyboard.is_pressed("4"):
            currentState = 4
            changeSpace(user, currentState)
            if instances == 1:
                x = user.xcor()
                y = user.ycor()
                portal(color, x, y, user)
                instances += 1
                currentState = 0
                user.color("black")
                user.speed(1)
            else:
                x = user.xcor()
                y = user.ycor()
                color = input("What color should the portal be? ")
                portal(color, x, y, user)
                instances = 1
                currentState = 0
                user.color("black")
                user.speed(1)
            

        elif keyboard.is_pressed("5"):
            currentState = 5
            changeSpace(user, currentState)
            x = user.xcor()
            y = user.ycor()
            oneWay(x, y, user)
            currentState = 0
            user.color("black")
            user.speed(1)

        elif keyboard.is_pressed("6"):
            currentState = 6
            user.color("gray")
            user.pendown()


        elif keyboard.is_pressed("7"):
            currentState = 7
            changeSpace(user, currentState)
            user.color("yellow")
            user.pendown()
            user.circle(5)
            user.penup()
            currentState = 0
            user.color("black")
            user.speed(1)

        elif keyboard.is_pressed("8"):
            currentState = 8
            changeSpace(user, currentState)
            user.color("green")
            user.pendown()
            user.circle(5)
            user.penup()
            currentState = 0
            user.color("black")
            user.speed(1)

        elif keyboard.is_pressed("9"):
            currentState = 9
            changeSpace(user, currentState)
            user.color("blue")
            user.pendown()
            user.circle(5)
            user.penup()
            currentState = 0
            user.color("black")
            user.speed(1)
        
        elif keyboard.is_pressed("l"):
            print(mazeMap)
            sleep(2)
        
        elif keyboard.is_pressed("p"):
            saveMap()
            exit()

moveNorm()