import turtle
from time import sleep # You can do "import time" but that means you have to type "time.sleep()" everytime you use sleep
from lvlParts import *

def draw(user): # Function that draws the map
    global walls, wallDots # Makes everything (excluding user) in the function global
    walls = turtle.Turtle() # This turtle will be drawing the walls
    walls.speed(0) # Setting the turtle speed to 0 means that the level is drawn as fast as possible
    wallDots = [] # List to store all the dots to check if a player hit a wall

    goal(225, 25, walls)

    # Main wall tree
    wallDots = wall(125, 25, 0, walls, 3, wallDots)
    wallDots = wall(125, -75, 90, walls, 2, wallDots) # Branch heading South
    wallDots = wall(75, -75, 0, walls, 2, wallDots)
    wallDots = wall(75, -125, 90, walls, 1, wallDots)
    wallDots = wall(-25, -125, 0, walls, 5, wallDots)
    wallDots = wall(225, -225, 90, walls, 4, wallDots) # Branch on East side heading North
    wallDots = wall(175, -25, 0, walls, 1, wallDots)

    wallDots = wall(25, -175, 90, walls, 3, wallDots) # Branch in center of map heading North
    wallDots = wall(-25, -25, 0, walls, 2, wallDots)
    wallDots = wall(-25, -25, 90, walls, 1, wallDots)
    wallDots = wall(75, -25, 90, walls, 1, wallDots)

    # Return to Main wall, going down branch heading North
    wallDots = wall(175, 25, 90, walls, 1, wallDots)
    wallDots = wall(175, 75, 0, walls, 1, wallDots)
    wallDots = wall(225, 75, 90, walls, 3, wallDots)
    wallDots = wall(125, 175, 0, walls, 2, wallDots)
    wallDots = wall(125, 175, 90, walls, 1, wallDots)
    wallDots = wall(25, 225, 0, walls, 2, wallDots)
    wallDots = wall(25, 175, 90, walls, 1, wallDots)
    wallDots = wall(-25, 175, 0, walls, 1, wallDots)
    wallDots = wall(-25, 125, 90, walls, 1, wallDots)
    wallDots = wall(-75, 125, 0, walls, 1, wallDots)
    # End of Main wall

    # Start of biggest wall tree
    wallDots = wall(175, -275, 90, walls, 2, wallDots)
    wallDots = wall(75, -175, 0, walls, 2, wallDots)
    wallDots = wall(75, -225, 90, walls, 1, wallDots)
    wallDots = wall(-25, -225, 0, walls, 3, wallDots)
    wallDots = wall(-25, -225, 90, walls, 1, wallDots)
    wallDots = wall(-75, -175, 0, walls, 1, wallDots)
    wallDots = wall(-75, -175, 90, walls, 5, wallDots)
    wallDots = wall(-125, -25, 0, walls, 1, wallDots)
    wallDots = wall(-75, -75, 0, walls, 1, wallDots)

    # Split
    wallDots = wall(-125, 75, 0, walls, 5, wallDots)
    # Eastern side
    wallDots = wall(25, 25, 90, walls, 1, wallDots)
    wallDots = wall(125, 75, 90, walls, 1, wallDots)
    wallDots = wall(25, 125, 0, walls, 3, wallDots)
    wallDots = wall(75, 125, 90, walls, 1, wallDots)
    # End of Eastern side
    # Western side
    # Split
    wallDots = wall(-125, 25, 90, walls, 3, wallDots)
    # Northern side
    wallDots = wall(-175, 175, 0, walls, 2, wallDots)
    wallDots = wall(-75, 175, 90, walls, 1, wallDots)
    wallDots = wall(-225, 225, 0, walls, 4, wallDots)
    wallDots = wall(-225, 125, 90, walls, 2, wallDots)
    wallDots = wall(-225, 125, 0, walls, 1, wallDots)
    # End of Northern side
    # Southern side
    wallDots = wall(-225, 25, 0, walls, 2, wallDots)
    wallDots = wall(-225, -125, 90, walls, 3, wallDots)
    wallDots = wall(-225, -125, 0, walls, 2, wallDots)
    wallDots = wall(-125, -125, 90, walls, 1, wallDots)
    wallDots = wall(-175, -75, 0, walls, 1, wallDots)
    wallDots = wall(-175, -225, 90, walls, 2, wallDots)
    wallDots = wall(-175, -75, 90, walls, 1, wallDots)
    # End of biggest wall

    # Start of small border walls
    wallDots = wall(-275, 75, 0, walls, 2, wallDots)
    wallDots = wall(175, 225, 90, walls, 1, wallDots)
    wallDots = wall(-275, -175, 0, walls, 1, wallDots)
    wallDots = wall(-225, -225, 90, walls, 1, wallDots)
    wallDots = wall(-125, -275, 90, walls, 2, wallDots)
    wallDots = wall(-125, -225, 0, walls, 1, wallDots)

    oneWay(75, -125, 90, walls, "white")