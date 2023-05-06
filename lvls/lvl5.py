import turtle
from time import sleep

wallDots = []

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

def lvl5(user):
    global trapT, conveyors, walls, userCopy
    walls = turtle.Turtle()
    walls.speed(0)
    walls.hideturtle()

    goal(-275, 0, walls)

    userCopy = turtle.Turtle()
    userCopy.penup()
    userCopy.speed(0)
    userCopy.clear()
    userCopy.goto(-150, 250)
    userCopy.speed(1)
    userCopy.color("blue")
    userCopy.pensize(4)
    userCopy.pendown()
    userCopy.showturtle()
    userCopy.setheading(270)

    user.speed(0)
    user.penup()
    user.showturtle()
    user.goto(0, -250)
    user.speed(1)
    user.pendown()
    user.setheading(90)

    return userCopy

def clearMap():
    trapT.clear()
    conveyors.clear()

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
        door = "lvl6"
        pen.clear()
        turtles.clear()
        walls.clear()
        userCopy.clear()
        clearMap()
        Win.clear()
        turtles.penup()
        turtles.hideturtle()
        return door
    else:
        return door  