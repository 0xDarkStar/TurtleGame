'''
By: 0xDarkStar

A small maze game in which the user goes to the end goal in order to win (duh)
'''

'''
This file calls all other files and is the main control script.
Any movement goes through this script (excluding the enemy, that goes through pathing)
Another exception to the movement claim is when the player bumps into a wall, in which they are pushed back. That can be found in the level scripts
'''
import sys
sys.path.append("/home/matt/.local/lib/python3.10/site-packages/")

import updateList
updateList.main()

import platform
import keyboard
import turtle
from os import system
from PathFind import pathing
from time import sleep
from lvls import *

screen = turtle.Screen()
screen.setup(width = 550, height = 550)

OS = platform.system()

# Lists
blueport = [(250, 50), (-100, -250)]
pinkport = [(-250, 50), (-150, 50)]
greenport = [(200, 200), (150, 50)]
purpport = [(0, 50), (150, -250)]
portals = [blueport, pinkport, greenport, purpport]

#Functions
def grabPos(turtle): # Grabs the position of the specified turtle
    x = turtle.xcor() # The reason I use this is because I want integers, not floats
    y = turtle.ycor()
    pos = (x, y)
    return pos


def findportnum(input, listL): # Find the portal that the player is at
    a = 0
    while a < 4: # Cycle through the portal list
        if input in listL[a]:
            return a # Player is on a portal, return the index (Line 59 is called after this function when this is the result)
        else:
            a += 1
    if a == 4: # It reached the end of the list
        a = "duck" # Random string, idk why
        return a # It returns the string


def findport2(input, listL, b): # To find the portal where the player will teleport to
    a = listL[b].index(input) # assigns "a" to the position of the other portal
    return a # returns the position

def sysClear(): # Checks which OS the computer is using in order to clear the terminal
    if OS == "Linux" or OS == "Darwin": # Linux or MacOS
        system("clear") # Their way of clearing the terminal
    elif OS == "Windows": # Windows
        system("cls") # Windows' way of clearing the terminal
    else: # Unknown operating system
        print("I can't find your OS which means I can't clear the terminal. :(", end= "\r")

def Center(user): # Makes sure user doesn't get coords that are a float which wouldn't allow the walls to work.
    Nycor = round(user.ycor()) # Rounds the turtle's x coordinate
    Nxcor = round(user.xcor()) # Rounds the turtle's y coordinate
    user.goto(int(Nxcor), int(Nycor)) # Moves the turtle to the correct spot

def menu(lvl): # Gives users a menu showing them how to move
    if lvl == "lvl1": # Menus level 1 through to level 5 (excluding level 2) are the same
        print("/-------------\ \n| w = up      |\n| d = right   |\n| a = left    |\n| s = down    |\n| ~ = quit    |\n| r = reset   |\n|             |\n\-------------/\n", end= "\r")
    elif lvl == "lvl2": # This level has teleporting!      (wow...)
        print("/-------------\ \n| w = up      |\n| d = right   |\n| a = left    |\n| s = down    |\n| ~ = quit    |\n| r = reset   |\n| t = teleport|\n\-------------/\n", end= "\r")
    elif lvl == "lvl3":
        print("/-------------\ \n| w = up      |\n| d = right   |\n| a = left    |\n| s = down    |\n| ~ = quit    |\n| r = reset   |\n|             |\n\-------------/\n", end= "\r")
    elif lvl == "lvl4":
        print("/-------------\ \n| w = up      |\n| d = right   |\n| a = left    |\n| s = down    |\n| ~ = quit    |\n| r = reset   |\n|             |\n\-------------/\n", end= "\r")

#start
def start():
    sysClear() # Line 63
    door = False
    user = turtle.Turtle() # Spawn user
    pen = turtle.Turtle() # Spawns pen, used to write down the coordinates of the user.
    pen.color("red") # It [pen] is useful when a wall isn't working
    pen.hideturtle()
    pen.penup()
    pen.speed(0)
    user.pencolor("red")
    user.pensize(4)
    user.speed(0)
    user.penup()
    user.hideturtle()
    x, y = lvl1.lvl1(user) # Line 26 in lvl1.py
    lvl = "lvl1" # Used to print the correct menu
    a = 0
    menu(lvl) # line 76
    turn = 1
    while a >= 0: # Menu to allow user to move
        Center(user) # Line 71
        door = lvl1.collision(user, pen, door) # Line 185 in lvl1.py
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
            user.goto(x, y)
            user.pendown()
            turn = 1

        elif keyboard.is_pressed("o"): # pauses game.
            keyboard.wait("l")

        elif keyboard.is_pressed("m"): # skip level
            user.goto(-250, 250)
        
        print("Turn: " + str(turn), end = "\r") # Prints the turn, which is the amount of moves they did + 1
        a += 1

        door = lvl1.collision(user, pen, door)
        if door == "lvl2":
            lvl = "lvl2"
            door = False
            sleep(2)
            break
    
    sysClear() # Line 63
    menu(lvl) # Line 76
    lvl2.lvl2(user) # Line 69 in lvl2.py
    a = 0
    turn = 1
    while a >= 0: # Menu to allow user to move
        Center(user) # Line 71
        door = lvl2.collision(user, pen, door) # Line 201 in lvl2.py

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
            b = findportnum(pos, portals) # Line 47
            if b != "duck": # It was in the list of portals
                c = findport2(pos, portals, b) # Line 59
                name = portals[b] # Store the portal coord list as name
                if c == 0: # Player is at the first portal
                    port = name[1] # Store the second portal as port
                    user.penup()
                    user.goto(port) # Teleport to second portal
                    user.pendown()
                elif c == 1: # Player is at the second portal
                    port = name[0] # Store the first portal as port
                    user.penup()
                    user.goto(port) # Teleport to first portal
                    user.pendown()
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
            user.goto(-250, 250) # Moves player to spawn
            user.pendown()
            turn = 1

        elif keyboard.is_pressed("o"): # Pauses game.
            keyboard.wait("l")
        
        elif keyboard.is_pressed("m"): # Skip level
            user.goto(0, 0) # Goes to goal

        print("Turn: " + str(turn), end = "\r")
        a += 1

        door = lvl2.collision(user, pen, door)
        if door == "lvl3": # They reached the goal
            lvl = "lvl3" # Change this to print the right menu
            door = False # Reset door
            sleep(2)
            break
    sysClear() # Line 63
    menu(lvl) # Line 76
    lvl3.lvl3(user) # Line 159 in lvl3.py
    a = 0
    prevPos = 0 # make this variable to use later
    turn = 1
    while a >= 0: # Menu to allow user to move
        Center(user) # Line 72
        door = lvl3.collision(user, pen, door, prevPos) # Line 301 in lvl3.py

        if keyboard.is_pressed("w"): # Move up
            user.setheading(90)
            prevPos = grabPos(user)
            user.forward(25)
            turn += 1

        elif keyboard.is_pressed("a"): # Move left
            user.setheading(180)
            prevPos = grabPos(user)
            user.forward(25)
            turn += 1

        elif keyboard.is_pressed("d"): # Move right
            user.setheading(0)
            prevPos = grabPos(user)
            user.forward(25)
            turn += 1

        elif keyboard.is_pressed("s"): # Move down
            user.setheading(270)
            prevPos = grabPos(user)
            user.forward(25)
            turn += 1

        elif keyboard.is_pressed("grave"): # Exit the game
            exit()

        # Lines after this are for making levels
        elif keyboard.is_pressed("n"):
            pen.setx(user.xcor())
            pen.sety(user.ycor())
            pen.write("(" + str(user.xcor()) + ", " + str(user.ycor()) + ")")

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
            user.clear()
            user.goto(0, -250)
            user.pendown()
            a = 0
        
        elif keyboard.is_pressed("o"): # Pauses game.
            keyboard.wait("l")

        elif keyboard.is_pressed("m"): # Skip level
            user.goto(0, 250)

        print("Turn: " + str(turn), end = "\r")
        a += 1

        door = lvl3.collision(user, pen, door, prevPos)
        if door == "lvl4":
            lvl = "lvl4"
            door = False
            sleep(2)
            break
    sysClear() # Line 63
    menu(lvl) # Line 76
    userCopy = lvl4.lvl4(user) # Mirror level! Line 30 in lvl4.py
    a = 0
    prevPos = 0
    turn = 1
    while a >= 0: # Menu to allow user to move
        Center(user) # Line 72
        Center(userCopy)
        door = lvl4.collision(user, pen, door) # Line 85 in lvl4.py

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
            user.goto(0, -250)
            userCopy.goto(0, 250)
            user.pendown()
            userCopy.pendown()
            turn = 1
        
        elif keyboard.is_pressed("o"): # Pauses game.
            keyboard.wait("l")

        print("Turn: " + str(turn), end = "\r")
        a += 1

        Center(user) # Line 72
        Center(userCopy)

        door = lvl4.collision(user, pen, door)
        if door == "lvl5":
            lvl = "lvl5"
            door = False
            sleep(2)
            break
    sysClear()
    menu(lvl) # Line 76
    userCopy = lvl5.lvl5(user)
    a = 0
    prevPos = 0
    turn = 1
    while a >= 0: # Menu to allow user to move
        Center(user) # Line 72
        Center(userCopy)
        door = lvl5.collision(user, pen, door)

        if keyboard.is_pressed("w"):
            user.setheading(90)
            userCopy.setheading(270)
            prevPos = grabPos(user)
            user.forward(25)
            userCopy.forward(25)
            turn += 1

        elif keyboard.is_pressed("a"):
            user.setheading(180)
            userCopy.setheading(0)
            prevPos = grabPos(user)
            user.forward(25)
            userCopy.forward(25)
            turn += 1

        elif keyboard.is_pressed("d"):
            user.setheading(0)
            userCopy.setheading(180)
            prevPos = grabPos(user)
            user.forward(25)
            userCopy.forward(25)
            turn += 1

        elif keyboard.is_pressed("s"):
            user.setheading(270)
            userCopy.setheading(90)
            prevPos = grabPos(user)
            user.forward(25)
            userCopy.forward(25)
            turn += 1

        elif keyboard.is_pressed("grave"):
            exit()

        # Lines after this are for making levels
        elif keyboard.is_pressed("n"):
            pen.setx(user.xcor())
            pen.sety(user.ycor())
            pen.color('red')
            pen.write("(" + str(user.xcor()) + ", " + str(user.ycor()) + ")")
            pen.setx(userCopy.xcor())
            pen.sety(userCopy.ycor())
            pen.color('blue')
            pen.write("(" + str(userCopy.xcor()) + ", " + str(userCopy.ycor()) + ")")

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
            user.goto(0, -250)
            userCopy.goto(-150, 250)
            user.pendown()
            userCopy.pendown()
            turn = 1
        
        elif keyboard.is_pressed("o"): # Pauses game.
            keyboard.wait("l")

        print("Turn: " + str(turn), end = "\r")
        a += 1

        Center(user) # Line 72
        Center(userCopy)

        door = lvl5.collision(user, pen, door)
        if door == "lvl6":
            lvl = "lvl6"
            door = False
            sleep(2)
            break


start()

# Bot code:
'''
    bot = turtle.Turtle()
    bot.penup()
    bot.hideturtle()
    bot.speed(0)
    bot.shape("circle")
''' # This makes the bot so it can be used
'''
            pathing.pathing(bot, user) # bot only moves when player moves
''' # This moves the bot everytime the player moves.
# We have it do that by just putting this line of code into each movement key section
