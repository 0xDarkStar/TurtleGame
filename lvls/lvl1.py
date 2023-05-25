import turtle
from time import sleep
from .movement import movement

def wall(go1, go2, head, walls): #little function to make the code for drawing walls a bit smaller
    walls.penup()
    walls.goto(go1, go2)
    walls.setheading(head)
    walls.pendown()
    walls.forward(50)

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

#Level 1
def lvl1(user, pen): #Drawing all the walls
    global walls, wallDots
    wallDots = [(225,225),(250,225), (225, 175), (225, 200), (250, 125), (225, 125), (225, -25), (225, 0), (225, 25), (225, 50), (225, 75), (225, -75), (200, -75), (175, -75), (150, -75), (125, -75), (100, -75), (75, -75), (50, -75), (25, -75), (25, -225), (25, -200), (25, -175), (25, -150), (25, -125), (25, -100), (25, -50), (25, -25), (25, 0), (25, 25), (25, 50), (25, 75), (25, 100), (25, 125), (25, 150), (25, 175), (25, 200), (25, 225), (25, 250), (75, 225), (75, 250), (125, 225), (125, 250), (150, 225), (175, 225), (175, 125), (175, 150), (175, 175), (175, 200), (150, 125), (125, 125), (100, 125), (75, 125), (75, 150), (75, 175), (100, 175), (125, 175), (50, 25), (75, 25), (75, -25), (100, -25), (125, -25), (75, 75), (100, 75), (125, 75), (125, 50), (125, 25), (125, 0), (125, -50), (200, 75), (175, 75), (175, 50), (175, 25), (175, 0), (175, -25), (175, -50), (250, -125), (225, -125), (200, -125), (175, -125), (150, -125), (125, -125), (75, -125), (75, -150), (75, -175), (100, -175), (125, -175), (150, -175), (175, -175), (200, -175), (225, -175), (225, -200), (225, -225), (200, -225), (175, -225), (150, -225), (125, -225), (100, -225), (75, -225), (50, -225), (-250, -175), (-225, -175), (-225, -200), (-225, -225), (-175, -225), (-150, -225), (-125, -225), (-100, -225), (-75, -225), (-50, -225), (-25, -225), (-25, -200), (-25, -175), (-25, -150), (-25, -125), (-25, -100), (-25, -75), (-25, -50), (-25, -25), (-225, 225), (-200, 225), (-175, 225), (-150, 225), (-125, 225), (-100, 225), (-75, 225), (-150, -125), (-125, -125), (-125, -75), (-125, -100), (-125, -25), (-125, 0), (-125, 25), (-175, 25), (-175, 50), (-175, 75), (-100, 25), (-75, 25), (-50, 25), (-25, 25), (-75, 0), (-75, -25), (-75, -50), (-75, -75), (-75, -125), (-75, -150), (-75, -175), (-100, -175), (-125, -175), (-150, -175), (-175, -175), (-175, -150), (-175, -125), (150, -125), (-25, 50), (-25, 75), (-25, 100), (-25, 125), (-25, 150), (-25, 175), (-25, 200), (-25, 225), (0, 225), (-175, -25), (-175, -50), (-175, -75), (-175, -100), (-200, -125), (-225, -125), (-225, -100), (-225, -75), (-225, -50), (-225, -25), (-225, 0), (-225, 25), (-225, 50), (-225, 75), (-225, 125), (-225, 150), (-225, 175), (-225, 200), (-250, 225), (-175, 100), (-175, 125), (-200, 175), (-175, 175), (-125, 175), (-125, 150), (-125, 125), (-125, 100), (-125, 75), (-150, 75), (-75, 75), (-75, 100), (-75, 125), (-75, 150), (-75, 175), (-75, 200), (-75, 225), (-175, 0)]
    walls = turtle.Turtle()
    walls.speed(0)

    walls.color("white")
    walls.fillcolor("light green")
    walls.begin_fill()
    wall(-225, 275, 270, walls) # Goal
    walls.right(90)
    walls.forward(50)
    walls.right(90)
    walls.forward(50)
    walls.right(90)
    walls.forward(50)
    walls.end_fill()
    walls.color("black")

    walls.penup()
    walls.goto(275, 275)
    walls.right(90)
    walls.hideturtle()
    walls.pendown()# Border
    walls.forward(550)
    walls.right(90)
    walls.forward(550)
    walls.right(90)
    walls.forward(550)
    walls.right(90)
    walls.forward(550) # Border done

    wall(225, 225, 0, walls) #line (225 - 275, 225)

    wall(225, 225, 270, walls) # line (225, 225 - 175)

    wall(225, 125, 0, walls) # line (225 - 275, 175)

    wall(225, 75, 270, walls)
    walls.forward(50) # line(225, 75 - -25)

    wall(225, -75, 180, walls)
    walls.forward(150) # line (225 - 25, -75)

    wall(25, -225, 90, walls)
    walls.forward(450) # line (25, 275 - -225 )

    wall(75, 275, 270, walls) # line (75, 225 - 275)

    wall(125, 275, 270, walls) # line (125, 275 - 225)
    walls.left(90)
    walls.forward(50) # line (125 - 175, 225)
    walls.right(90)
    walls.forward(100) # line (175, 225 - 125)
    walls.right(90)
    walls.forward(100) # line (175 - 75, 125)
    walls.right(90)
    walls.forward(50) # line (75, 125 - 175)
    walls.right(90)
    walls.forward(50) # line (75 - 125, 175)
    
    wall(225, 75, 180, walls) # line (225 - 175, 75)
    walls.left(90)
    walls.forward(150) # line (175, 75 - -75)

    wall(125, -75, 90, walls)
    walls.forward(100) # line (125, -75 - 75)
    walls.left(90)
    walls.forward(50) # line (125 - 75, 75)
    
    wall(75, 25, 180, walls) # line (75 - 25, 25)

    wall(75, -25, 0, walls) # line (75 - 125, -25)

    wall(275, -125, 180, walls)
    walls.forward(100) # line (275 - 125, -125)

    wall(75, -125, 270, walls) # line (75, -125 - -175)
    walls.left(90)
    walls.forward(150) # line (75 - 225, -175)
    walls.right(90)
    walls.forward(50) # line (225, -175 - -225)
    walls.right(90)
    walls.forward(200) # line (25 - 225, -225)

    wall(-25, -225, 180, walls)
    walls.forward(100) # line (-175 - -25, -225)

    wall(-25, -225, 90, walls)
    walls.forward(150) # line (-25, -225 - -25)
    
    wall(-225, -225, 90, walls) # line (-225, -225 - -175)
    walls.left(90)
    walls.forward(50) # line (-275 - -225, -175)

    wall(-275, 225, 0, walls) #line (-225 - -75, 225)
    walls.forward(150)

    wall(-175, 125, 270, walls)
    walls.forward(50)
    walls.left(90)
    walls.forward(150)
    walls.left(90)
    walls.forward(200)
    walls.right(90)
    walls.forward(50)

    wall(-125, 25, 270, walls)
    walls.penup()
    walls.forward(50)
    walls.pendown()
    walls.forward(50)
    walls.right(90)
    walls.forward(50)
    walls.right(90)
    walls.forward(150)
    
    wall(-175, -125, 270, walls)
    walls.left(90)
    walls.forward(100)
    walls.left(90)
    walls.forward(50)

    wall(-75, -75, 90, walls)
    walls.forward(50)
    
    wall(-175, -125, 180, walls)
    walls.right(90)
    walls.forward(200)

    wall(-225, 225, 270, walls)
    walls.forward(50)
    walls.back(50)
    walls.left(90)
    walls.forward(50)

    wall(-125, 175, 270, walls)
    walls.forward(50)
    walls.right(90)
    walls.forward(50)

    wall(-75, 225, 270, walls) # I stopped commenting the walls because there are too many
    walls.forward(100)

    oneWay(-175, 25, 0, walls, "white")

    user.showturtle()
    global reset, menu
    reset = (250, 250)
    menu = "/-------------\ \n| w = up      |\n| d = right   |\n| a = left    |\n| s = down    |\n| ~ = quit    |\n| r = reset   |\n|             |\n\-------------/\n"
    user.goto(reset) # true start
    #user.goto(-250, -200) # just to test
    user.setheading(180)
    user.pendown()
    user.speed(1)
    '''
    bot.goto(100, 150)
    bot.showturtle()
    bot.speed(1)
    '''
    movement(user, pen, menu, collision, 0, 0, reset, 0)

def collision(turtles, pen, door, prevPos): # Check if user is in a wall or out of bounds
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
    elif pos == (-150, 0):
        if door != "open":
            oneWay(-175, 25, 0, walls, "light green")
            door = "open"
    elif pos == (-150, 50):
        if door != "closed":
            oneWay(-175, 25, 0, walls, "red")
            door = "closed"
    elif pos == (-150, 25):
        if turtles.heading() == 90:
            turtles.forward(25)
        elif turtles.heading() == 270:
            turtles.back(25)
        else:
            print("I don't know how you went into the door through a wall or sideways.\nThere should be no way.", end = "\r")
            sleep(1)
            print("                                          ", end = "\r")
    elif xpos <= -226 and xpos >= -274 and ypos <= 274 and ypos >= 226: # Checks if they made it to the goal
        Win = turtle.Turtle()
        Win.hideturtle()
        Win.goto(0,0)
        Win.write("YOU WON", False, align="center", font = ("Arial", 40, "bold") ) # Turtle is spawned to write "YOU WON" in center of screen
        sleep(2)
        door = "lvl2"
        pen.clear()
        turtles.clear()
        walls.clear()
        Win.clear()
        turtles.penup()
        turtles.hideturtle()
    return door
