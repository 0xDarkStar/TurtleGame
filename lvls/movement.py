import turtle
from time import sleep
import sys
from PathFind import pathing
sys.path.append("/home/matt/.local/lib/python3.10/site-packages/")
import keyboard

# Make sure the turtles are in the right spot:
def Center(user): # Makes sure user doesn't get coords that are a float which wouldn't allow the walls to work.
    Nycor = round(user.ycor()) # Rounds the turtle's x coordinate
    Nxcor = round(user.xcor()) # Rounds the turtle's y coordinate
    user.goto(int(Nxcor), int(Nycor)) # Moves the turtle to the correct spot

def grabPos(turtle): # Grabs the position of the specified turtle
    x = turtle.xcor() # The reason I use this is because I want integers, not floats
    y = turtle.ycor()
    pos = (x, y)
    return pos

doorStates = [False, "open", "closed"]

def moveTeleport(user, pen, collision, teleport, reset):
    door = False
    a = 0
    turn = 1
    while a >= 0: # Menu to allow user to move
        Center(user) # Line 71
        prevPos = grabPos(user)
        door = collision(user, pen, door, prevPos) # Line 201 in lvl2.py

        if keyboard.is_pressed("w"): # Move up
            user.setheading(90)
            user.forward(25)
            turn += 1

        elif keyboard.is_pressed("a"): # Move left
            user.setheading(180)
            user.forward(25)
            turn += 1

        elif keyboard.is_pressed("d"): # Move right
            user.setheading(0)
            user.forward(25)
            turn += 1

        elif keyboard.is_pressed("s"): # Move down
            user.setheading(270)
            user.forward(25)
            turn += 1

        elif keyboard.is_pressed("grave"): # Exit the game
            exit()

        elif keyboard.is_pressed("t"): # Teleport
            pos = user.pos()
            teleported = teleport(pos, user)
            if teleported == False:
                sleep(.15)
                turn += 1
            else:
                turn += 1

        # Lines after this are for making levels
        elif keyboard.is_pressed("n"):
            pen.setx(user.xcor())
            pen.sety(user.ycor()) # Going to user coordinates
            pen.write("(" + str(user.xcor()) + ", " + str(user.ycor()) + ")") # Prints the coordinates at the players location

        elif keyboard.is_pressed("g"):
            pen.clear() # Deletes all the printed coordinates

        elif keyboard.is_pressed("c"):
            colors = input("What color do you want? ") # Allows the palyer to change color. Not put in the menu because I don't want players to change to whatever color
            user.pencolor(colors) # I might comment this out when I publish it. If you want to change color, uncomment it.

        elif keyboard.is_pressed("p"):
            if user.isvisible() == False:
                user.showturtle()
                user.pendown()
            elif user.isvisible() == True:
                user.hideturtle()
                user.penup()

        elif keyboard.is_pressed("r"): # This is not for making levels, this is just to reset the player.
            user.penup()
            user.clear()
            user.goto(reset) # Moves player to spawn
            user.pendown()
            turn = 1

        elif keyboard.is_pressed("o"): # Pauses game.
            keyboard.wait("l")
        
        elif keyboard.is_pressed("m"): # Skip level
            user.goto(0, 0) # Goes to goal

        print("Turn: " + str(turn), end = "\r")
        a += 1

        Center(user)
        prevPos = grabPos(user)
        door = collision(user, pen, door, prevPos)
        if door not in doorStates: # They reached the goal
            door = False # Reset door
            sleep(2)
            break

def moveNorm(user, pen, collision, reset):
    door = False
    a = 0
    turn = 1
    while a >= 0: # Menu to allow user to move
        Center(user) # Line 71
        prevPos = grabPos(user)
        door = collision(user, pen, door, prevPos) # Line 185 in lvl1.py
        if keyboard.is_pressed("w"):
            user.setheading(90)
            user.forward(25)
            turn += 1

        elif keyboard.is_pressed("a"):
            user.setheading(180)
            user.forward(25)
            turn += 1

        elif keyboard.is_pressed("d"):
            user.setheading(0)
            user.forward(25)
            turn += 1

        elif keyboard.is_pressed("s"):
            user.setheading(270)
            user.forward(25)
            turn += 1

        elif keyboard.is_pressed("grave"):
            exit()

        # All keys after this are for developing levels
        elif keyboard.is_pressed("n"):
            pen.setx(user.xcor())
            pen.sety(user.ycor())
            pen.write("(" + str(user.xcor()) + ", " + str(user.ycor()) + ")")
            # ^ shows coords of the user

        elif keyboard.is_pressed("g"):
            pen.clear() # removes all written coords from screen

        elif keyboard.is_pressed("c"):
            colors = input("What color do you want?\n ") # changes color of user
            user.pencolor(colors)

        elif keyboard.is_pressed("p"): # helpful to cross gaps when drawing
            if user.isvisible() == False:
                user.showturtle()
                user.pendown()
            elif user.isvisible() == True:
                user.hideturtle()
                user.penup()

        elif keyboard.is_pressed("r"): # except this, this is to reset
            user.penup()
            user.clear()
            user.goto(reset)
            user.pendown()
            turn = 1

        elif keyboard.is_pressed("o"): # pauses game.
            keyboard.wait("l")

        elif keyboard.is_pressed("m"): # skip level
            user.goto(-250, 250)
        
        print("Turn: " + str(turn), end = "\r") # Prints the turn, which is the amount of moves they did + 1
        a += 1

        Center(user)
        prevPos = grabPos(user)
        door = collision(user, pen, door, prevPos)
        if door not in doorStates:
            door = False
            sleep(2)
            break

def moveNormBot(user, pen, collision, bot, reset):
    door = False
    a = 0
    turn = 1
    while a >= 0: # Menu to allow user to move
        Center(user) # Line 71
        prevPos = grabPos(user)
        door = collision(user, pen, door, prevPos) # Line 185 in lvl1.py
        if keyboard.is_pressed("w"):
            user.setheading(90)
            user.forward(25)
            pathing.pathing(bot, user) # bot only moves when player moves
            turn += 1

        elif keyboard.is_pressed("a"):
            user.setheading(180)
            user.forward(25)
            pathing.pathing(bot, user) # bot only moves when player moves
            turn += 1

        elif keyboard.is_pressed("d"):
            user.setheading(0)
            user.forward(25)
            pathing.pathing(bot, user) # bot only moves when player moves
            turn += 1

        elif keyboard.is_pressed("s"):
            user.setheading(270)
            user.forward(25)
            pathing.pathing(bot, user) # bot only moves when player moves
            turn += 1

        elif keyboard.is_pressed("grave"):
            exit()

        # All keys after this are for developing levels
        elif keyboard.is_pressed("n"):
            pen.setx(user.xcor())
            pen.sety(user.ycor())
            pen.write("(" + str(user.xcor()) + ", " + str(user.ycor()) + ")")
            # ^ shows coords of the user

        elif keyboard.is_pressed("g"):
            pen.clear() # removes all written coords from screen

        elif keyboard.is_pressed("c"):
            colors = input("What color do you want?\n ") # changes color of user
            user.pencolor(colors)

        elif keyboard.is_pressed("p"): # helpful to cross gaps when drawing
            if user.isvisible() == False:
                user.showturtle()
                user.pendown()
            elif user.isvisible() == True:
                user.hideturtle()
                user.penup()

        elif keyboard.is_pressed("r"): # except this, this is to reset
            user.penup()
            user.clear()
            user.goto(reset[0])
            bot.goto(reset[1])
            user.pendown()
            turn = 1

        elif keyboard.is_pressed("o"): # pauses game.
            keyboard.wait("l")

        elif keyboard.is_pressed("m"): # skip level
            user.goto(-250, 250)
        
        print("Turn: " + str(turn), end = "\r") # Prints the turn, which is the amount of moves they did + 1
        a += 1

        Center(user)
        prevPos = grabPos(user)
        door = collision(user, pen, door, prevPos)
        if door not in doorStates:
            door = False
            sleep(2)
            break

def moveMirror(user, pen, collision, userCopy, reset):
    door = False
    a = 0
    turn = 1
    while a >= 0: # Menu to allow user to move
        Center(user) # Line 72
        Center(userCopy)
        prevPos = grabPos(user)
        prevPosCopy = grabPos(userCopy)
        door = collision.check(pen, door, prevPos, prevPosCopy) # calls the 

        if keyboard.is_pressed("w"):
            user.setheading(90) # Turn player
            userCopy.setheading(270) # Turn copy
            user.forward(25) # Move player
            userCopy.forward(25) # Move copy
            turn += 1

        elif keyboard.is_pressed("a"):
            user.setheading(180)
            userCopy.setheading(0)
            user.forward(25)
            userCopy.forward(25)
            turn += 1

        elif keyboard.is_pressed("d"):
            user.setheading(0)
            userCopy.setheading(180)
            user.forward(25)
            userCopy.forward(25)
            turn += 1

        elif keyboard.is_pressed("s"):
            user.setheading(270)
            userCopy.setheading(90)
            user.forward(25)
            userCopy.forward(25)
            turn += 1

        elif keyboard.is_pressed("grave"):
            exit()

        # Lines after this are for making levels
        elif keyboard.is_pressed("n"): # This now prints the coordinates of both characters (player and copy)
            pen.setx(user.xcor())
            pen.sety(user.ycor())
            pen.color('red')
            pen.write("(" + str(user.xcor()) + ", " + str(user.ycor()) + ")")
            pen.setx(userCopy.xcor())
            pen.sety(userCopy.ycor())
            pen.color('blue')
            pen.write("(" + str(userCopy.xcor()) + ", " + str(userCopy.ycor()) + ")")

            # ^ shows coords of the user

        elif keyboard.is_pressed("g"):
            pen.clear()

        elif keyboard.is_pressed("c"):
            colors = input("What color do you want? ")
            user.pencolor(colors)

        elif keyboard.is_pressed("p"):
            if user.isvisible() == False:
                user.showturtle()
                user.pendown()
            elif user.isvisible() == True:
                user.hideturtle()
                user.penup()

        elif keyboard.is_pressed("r"): # Except this, this is to reset
            user.penup()
            userCopy.penup() # Resets both characters
            user.clear()
            userCopy.clear()
            user.goto(reset[0])
            userCopy.goto(reset[1])
            user.pendown()
            userCopy.pendown()
            turn = 1
        
        elif keyboard.is_pressed("o"): # Pauses game.
            keyboard.wait("l")

        print("Turn: " + str(turn), end = "\r")
        a += 1

        Center(user) # Line 72
        Center(userCopy)
        prevPos = grabPos(user)
        prevPosCopy = grabPos(userCopy)
        door = collision.check(pen, door, prevPos, prevPosCopy)
        if door not in doorStates:
            door = False
            sleep(2)
            break

def movement(user, pen, menu, collision, teleport, bot, reset, userCopy):
    print(menu)
    global a, turn
    if bot != False:
        moveNormBot(user, pen, collision, bot, reset)
    elif teleport != False:
        moveTeleport(user, pen, collision, teleport, reset)
    elif userCopy != False:
        moveMirror(user, pen, collision, userCopy, reset)
    else:
        moveNorm(user, pen, collision, reset)