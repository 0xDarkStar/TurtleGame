import sys
sys.path.append("/home/matt/.local/lib/python3.10/site-packages/") # Required to find the keyboard module

import turtle
from time import sleep
import keyboard
import guideWalls as level # Replace this with whatever level you want to run

screen = turtle.Screen()
screen.setup(width = 550, height = 550)

def Center(user): # Makes sure user doesn't get coords that are a float which wouldn't allow the walls to work.
    Nycor = round(user.ycor()) # Rounds the turtle's x coordinate
    Nxcor = round(user.xcor()) # Rounds the turtle's y coordinate
    user.goto(int(Nxcor), int(Nycor)) # Moves the turtle to the correct spot

def start():
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
    level.draw(user)
    a = 0
    turn = 1
    while a >= 0: # Menu to allow user to move
        Center(user) # Line 71
#        door = level.collision(user, pen, door) # Line 201 in lvl2.py

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

#        elif keyboard.is_pressed("t"): # Teleport
#            pos = user.pos()
#            teleported = level.teleport(pos, user) # Remove comments if necessary
#            if teleported == False:
#                sleep(.15)
#                turn += 1
#            else:
#                turn += 1

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

#        door = level.collision(user, pen, door)
        if door == "done": # They reached the goal
            lvl = "done" # Change this to print the right menu
            door = False # Reset door
            sleep(2)
            break

start()