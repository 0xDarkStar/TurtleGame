'''
By: 0xDarkStar

A small maze game in which the user goes to the end goal in order to win (duh)
'''

'''
This file calls all other files and is the main control script.
Any movement goes through this script (excluding the enemy, that goes through pathing)
Another exception to the movement claim is when the player bumps into a wall, in which they are pushed back. That can be found in the level scripts
'''

import updateList
updateList.main()

import platform
import turtle
from os import system
from PathFind import pathing
from time import sleep
from lvls import *

screen = turtle.Screen()
screen.setup(width = 550, height = 550)

OS = platform.system()

#Functions

def sysClear(): # Checks which OS the computer is using in order to clear the terminal
    if OS == "Linux" or OS == "Darwin": # Linux or MacOS
        system("clear") # Their way of clearing the terminal
    elif OS == "Windows": # Windows
        system("cls") # Windows' way of clearing the terminal
    else: # Unknown operating system
        print("I can't find your OS which means I can't clear the terminal. :(", end= "\r")


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
    lvl1.lvl1(user, pen) # Line 26 in lvl1.py
    sysClear() # Line 63
    lvl2.lvl2(user, pen) # Line 69 in lvl2.py
    sysClear() # Line 63
    lvl3.lvl3(user, pen) # Line 159 in lvl3.py
    sysClear() # Line 63
    lvl4.lvl4(user, pen) # Mirror level! Line 30 in lvl4.py
    sysClear()
    lvl5.lvl5(user, pen)
    sysClear()


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
