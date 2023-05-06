import turtle
from time import sleep

def wall(go1, go2, head, walls, distance): #little function to make the code for drawing walls a bit smaller
    walls.penup()
    walls.goto(go1, go2)
    walls.setheading(head)
    walls.pendown()
    walls.forward(distance)

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

def lvl3(user):
    global trapT, conveyorT, walls
    walls = turtle.Turtle()
    walls.hideturtle()
    walls.speed(0)
    
    goal(-25, 275, walls)

    # Main wall (biggest one)
    wall(-25, 275, 270, walls, 100)
    wall(-25, 175, 180, walls, 50)
    wall(-75, 175, 270, walls, 100)
    
    # Branch off Main wall
    wall(-75, 125, 180, walls, 100)
    wall(-175, 125, 90, walls, 50)
    wall(-175, 175, 0, walls, 50)
    wall(-125, 175, 90, walls, 50)
    wall(-125, 225, 0, walls, 50)
    # End of branch

    # Main wall cont.
    wall(-125, 75, 0, walls, 100)
    wall(-25, 75, 270, walls, 50)
    wall(-75, 25, 0, walls, 100)
    # Main wall breaks into two branches, left and right

    # Main wall branch left
    wall(-75, 25, 270, walls, 100)
    wall(-75, -75, 180, walls, 100)
    wall(-125, -75, 270, walls, 100) # first branch
    wall(-175, -125, 90, walls, 200)
    wall(-175, -125, 180, walls, 50)
    wall(-175, -25, 180, walls, 50)
    wall(-175, 25, 0, walls, 50)
    wall(-125, 25, 270, walls, 50)

    # Main wall branch right
    wall(25, 25, 270, walls, 50)
    wall(25, -25, 0, walls, 200)
    wall(175, 25, 270, walls, 250)
    wall(175, -125, 180, walls, 50)
    wall(125, -125, 90, walls, 50)
    # Main wall done

    # Wall right of goal
    wall(25, 275, 270, walls, 200)
    wall(25, 225, 0, walls, 200)
    wall(25, 125, 180, walls, 50)
    wall(25, 75, 0, walls, 100)
    wall(75, 75, 270, walls, 50)
    wall(125, 25, 90, walls, 100)
    # End of wall right of goal

    # Right of the wall above
    wall(275, 175, 180, walls, 200)
    wall(75, 175, 270, walls, 50)
    wall(175, 175, 270, walls, 100)
    wall(175, 75, 0, walls, 50)
    wall(225, 125, 270, walls, 100)
    # End of this wall

    # Top left wall
    wall(-275, 25, 0, walls, 50)
    wall(-225, 25, 90, walls, 200)
    wall(-225, 225, 0, walls, 50)
    # End of top left wall

    # Bottom wall (The bigger one)
    wall(125, -275, 90, walls, 100)
    wall(125, -175, 180, walls, 200)
    wall(75, -225, 90, walls, 150)
    wall(75, -75, 180, walls, 100)
    wall(-25, -25, 270, walls, 100)
    wall(-75, -125, 0, walls, 100)
    # End of bigger bottom wall

    # The two sticks on the left side
    wall(-275, -75, 0, walls, 50)
    wall(-275, -175, 0, walls, 50)
    # End of the two sticks

    # Bottom wall
    wall(25, -275, 90, walls, 50)
    wall(25, -225, 180, walls, 250)
    wall(-175, -225, 90, walls, 50)
    # End of bottom wall

    # Bottom right corner
    wall(225, -275, 90, walls, 100)
    wall(225, -125, 90, walls, 50)
    wall(225, -75, 0, walls, 50)
    # End of bottom right corner

    # All walls are done!

    conveyorT = turtle.Turtle()
    conveyorT.speed(0)
    conveyorT.penup()
    conveyorT.hideturtle()
    # Conveyor time
    conveyor(50, 200, 45, 0, 4, conveyorT)
    conveyor(250, 200, 45, 90, 1, conveyorT)
    conveyor(250, 250, 45, 180, 4, conveyorT)
    # Top right conveyor trap done

    # Goal conveyor
    conveyor(50, 50, 45, 180, 1, conveyorT)
    conveyor(0, 50, 45, 90, 1, conveyorT)
    conveyor(0, 100, 45, 180, 1, conveyorT)
    conveyor(-50, 100, 45, 90, 1, conveyorT)
    conveyor(-50, 150, 45, 0, 1, conveyorT)
    conveyor(0, 150, 45, 90, 2, conveyorT)
    # Goal conveyor done

    # Death conveyor
    conveyor(-50, -150, 45, 0, 2, conveyorT)
    conveyor(50, -150, 45, 90, 1, conveyorT)
    conveyor(50, -100, 45, 180, 1, conveyorT)
    trapT = turtle.Turtle()
    trapT.speed(0)
    trapT.hideturtle()
    trapT.penup()
    trap(0, -100, trapT)

    user.speed(0)
    user.showturtle()
    x = 0
    y = -250
    user.goto(x, y)
    user.setheading(180)
    user.pendown()
    user.speed(1)

wallDots = [(-250, 25), (-250, -75), (-250, -175), (-225, 225), (-225, 200), (-225, 175), (-225, 150), (-225, 125), (-225, 100), (-225, 75), (-225, 50), (-225, 25), (-225, -25), (-225, -75), (-225, -125), (-225, -175), (-225, -225), (-200, 225), (-200, -25), (-200, -125), (-200, -225), (-175, 225), (-175, 175), (-175, 150), (-175, 125), (-175, 75), (-175, 50), (-175, 25), (-175, 0), (-175, -25), (-175, -50), (-175, -75), (-175, -100), (-175, -125), (-175, -175), (-175, -200), (-175, -225), (-150, 175), (-150, 125), (-150, 25), (-150, -75), (-150, -225), (-125, 225), (-125, 200), (-125, 175), (-125, 125), (-125, 75), (-125, 25), (-125, 0), (-125, -25), (-125, -75), (-125, -100), (-125, -125), (-125, -150), (-125, -175), (-125, -225), (-100, 225), (-100, 125), (-100, 75), (-100, -75), (-100, -225), (-75, 225), (-75, 175), (-75, 150), (-75, 125), (-75, 100), (-75, 75), (-75, 25), (-75, 0), (-75, -25), (-75, -50), (-75, -75), (-75, -125), (-75, -175), (-75, -225), (-50, 175), (-50, 75), (-50, 25), (-50, -125), (-50, -175), (-50, -225), (-25, 250), (-25, 225), (-25, 200), (-25, 175), (-25, 125), (-25, 75), (-25, 50), (-25, 25), (-25, -25), (-25, -50), (-25, -75), (-25, -100), (-25, -125), (-25, -175), (-25, -225), (0, 125), (0, 25), (0, -75), (0, -125), (0, -175), (0, -225), (25, 250), (25, 225), (25, 200), (25, 175), (25, 150), (25, 125), (25, 100), (25, 75), (25, 25), (25, 0), (25, -25), (25, -75), (25, -125), (25, -175), (25, -225), (25, -250), (50, 225), (50, 75), (50, -25), (50, -75), (50, -175), (75, 225), (75, 175), (75, 150), (75, 125), (75, 75), (75, 50), (75, 25), (75, -25), (75, -75), (75, -100), (75, -125), (75, -150), (75, -175), (75, -200), (75, -225), (100, 225), (100, 175), (100, 75), (100, -25), (100, -175), (125, 225), (125, 175), (125, 125), (125, 100), (125, 75), (125, 50), (125, 25), (125, -25), (125, -75), (125, -100), (125, -125), (125, -175), (125, -200), (125, -225), (125, -250), (150, 225), (150, 175), (150, -25), (150, -125), (175, 225), (175, 175), (175, 150), (175, 125), (175, 100), (175, 75), (175, 25), (175, 0), (175, -25), (175, -50), (175, -75), (175, -100), (175, -125), (175, -150), (175, -175), (175, -200), (175, -225), (200, 225), (200, 175), (200, 75), (200, -25), (225, 225), (225, 175), (225, 125), (225, 100), (225, 75), (225, 50), (225, 25), (225, -25), (225, -75), (225, -100), (225, -125), (225, -175), (225, -200), (225, -225), (225, -250), (250, 175), (250, -75)]

conveyor1 = [(250, 200), (250, 250), (50, 250)]
conveyor2 = [(0, 50), (0, 100), (-50, 100), (-50, 150), (0, 150), (0, 250)]
conveyor3 = [(50, -150), (50, -100), (0, -100)]

conveyors = {(50, 200): conveyor1, (75, 250): conveyor1, (50, 50): conveyor2, (-50, -150): conveyor3}

traps = [(0, -100)]

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
    elif pos in conveyors:
        if prevPos == conveyors[pos][-1]:
            turtles.goto(conveyors[pos][-1])
        else:
            for i in conveyors[pos]:
                turtles.goto(i)
    elif xpos <= 24 and xpos >= -24 and ypos <= 275 and ypos >= 225: # Checks if they made it to the goal
        Win = turtle.Turtle()
        Win.hideturtle()
        Win.goto(0,0)
        Win.write("YOU WON", False, align="center", font = ("Arial", 40, "bold") ) # Turtle is spawned to write "YOU WON" in center of screen
        sleep(2)
        door = "lvl4"
        pen.clear()
        turtles.clear()
        walls.clear()
        trapT.clear()
        conveyorT.clear()
        Win.clear()
        turtles.penup()
        turtles.hideturtle()
        return door
    elif pos in traps:
        turtles.penup()
        turtles.clear()
        turtles.goto(0, -250)
        turtles.pendown()
        a = 0
    else:
        return door