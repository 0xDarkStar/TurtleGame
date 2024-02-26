import os

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

def findSpace(number = int, ignore = list, returnIndex = bool, mazeMap = list):
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

def makePortalList(number, file, color, mazeMap):
    column, row = findSpace(number, [-1], True, mazeMap)
    port1Pos = mazePos[row][column]
    port2Pos = findSpace(number, [column, row], False, mazeMap)
    file.write(f"{color}Portal = [{str(port1Pos)}, {str(port2Pos)}]\n")

def makeLevel(name, mazeMap):
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
        pos = findSpace(2, [-1], False, mazeMap)
        posC = findSpace(9, [-1], False, mazeMap)
        posB = findSpace(8, [-1], False, mazeMap)
        with open(f"{name}.py", "a") as file:
            file.write(f'    reset = [{str(pos)}, {str(posC)}, {str(posB)}]\n')
        if ", 41," in map:
            with open(f"{name}.py", "a") as file:
                file.write(f'    movement(user, pen, menu, collision, teleport, bot, reset, userCopy)\n')
        else:
            with open(f"{name}.py", "a") as file:
                file.write(f'    movement(user, pen, menu, collision, 0, bot, reset, userCopy)\n')
    elif ", 9," in map:
        pos = findSpace(2, [-1], False, mazeMap)
        posC = findSpace(9, [-1], False, mazeMap)
        with open(f"{name}.py", "a") as file:
            file.write(f'    reset = [{str(pos)}, {str(posC)}]\n')
        if ", 41," in map:
            with open(f"{name}.py", "a") as file:
                file.write(f'    movement(user, pen, menu, collision, teleport, 0, reset, userCopy)\n')
        else:
            with open(f"{name}.py", "a") as file:
                file.write(f'    movement(user, pen, menu, collision, 0, 0, reset, userCopy)\n')
    elif ", 8," in map:
        pos = findSpace(2, [-1], False, mazeMap)
        posB = findSpace(8, [-1], False, mazeMap)
        with open(f"{name}.py", "a") as file:
            file.write(f'    reset = [{str(pos)}, {str(posB)}]\n')
        if ", 41," in map:
            with open(f"{name}.py", "a") as file:
                file.write(f'    movement(user, pen, menu, collision, teleport, bot, reset, 0)\n')
        else:
            with open(f"{name}.py", "a") as file:
                file.write(f'    movement(user, pen, menu, collision, 0, bot, reset, 0)\n')
    else:
        pos = findSpace(2, [-1], False, mazeMap)
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