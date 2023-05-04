from PathFind import graph, a_star
from time import sleep
import math

def truncate(n):
    return int(n / 50) * 50


def run():
    # Create graph
    raph = graph.Graph()
    # Add vertices            y,x
    #y 1
    raph.add_node(graph.Node('AA', (1,1)))
    raph.add_node(graph.Node("AB", (1,2)))
    raph.add_node(graph.Node("AC", (1,3)))
    raph.add_node(graph.Node("AD", (1,4)))
    raph.add_node(graph.Node("AE", (1,5)))
    raph.add_node(graph.Node("AF", (1,6)))
    raph.add_node(graph.Node("AG", (1,7)))
    raph.add_node(graph.Node("AH", (1,8)))
    raph.add_node(graph.Node("AI", (1,9)))
    raph.add_node(graph.Node("AJ", (1,10)))
    raph.add_node(graph.Node("AK", (1,11)))
    #y 2
    raph.add_node(graph.Node("BA", (2,1)))
    raph.add_node(graph.Node("BB", (2,2)))
    raph.add_node(graph.Node("BC", (2,3)))
    raph.add_node(graph.Node("BD", (2,4)))
    raph.add_node(graph.Node("BE", (2,5)))
    raph.add_node(graph.Node("BF", (2,6)))
    raph.add_node(graph.Node("BG", (2,7)))
    raph.add_node(graph.Node("BH", (2,8)))
    raph.add_node(graph.Node("BI", (2,9)))
    raph.add_node(graph.Node("BJ", (2,10)))
    raph.add_node(graph.Node("BK", (2,11)))
    #y 3
    raph.add_node(graph.Node("CA", (3,1)))
    raph.add_node(graph.Node("CB", (3,2)))
    raph.add_node(graph.Node("CC", (3,3)))
    raph.add_node(graph.Node("CD", (3,4)))
    raph.add_node(graph.Node("CE", (3,5)))
    raph.add_node(graph.Node("CF", (3,6)))
    raph.add_node(graph.Node("CG", (3,7)))
    raph.add_node(graph.Node("CH", (3,8)))
    raph.add_node(graph.Node("CI", (3,9)))
    raph.add_node(graph.Node("CJ", (3,10)))
    raph.add_node(graph.Node("CK", (3,11)))
    #y 4
    raph.add_node(graph.Node("DA", (4,1)))
    raph.add_node(graph.Node("DB", (4,2)))
    raph.add_node(graph.Node("DC", (4,3)))
    raph.add_node(graph.Node("DD", (4,4)))
    raph.add_node(graph.Node("DE", (4,5)))
    raph.add_node(graph.Node("DF", (4,6)))
    raph.add_node(graph.Node("DG", (4,7)))
    raph.add_node(graph.Node("DH", (4,8)))
    raph.add_node(graph.Node("DI", (4,9)))
    raph.add_node(graph.Node("DJ", (4,10)))
    raph.add_node(graph.Node("DK", (4,11)))
    #y 5
    raph.add_node(graph.Node("EA", (5,1)))
    raph.add_node(graph.Node("EB", (5,2)))
    raph.add_node(graph.Node("EC", (5,3)))
    raph.add_node(graph.Node("ED", (5,4)))
    raph.add_node(graph.Node("EE", (5,5)))
    raph.add_node(graph.Node("EF", (5,6)))
    raph.add_node(graph.Node("EG", (5,7)))
    raph.add_node(graph.Node("EH", (5,8)))
    raph.add_node(graph.Node("EI", (5,9)))
    raph.add_node(graph.Node("EJ", (5,10)))
    raph.add_node(graph.Node("EK", (5,11)))
    #y 6
    raph.add_node(graph.Node("FA", (6,1)))
    raph.add_node(graph.Node("FB", (6,2)))
    raph.add_node(graph.Node("FC", (6,3)))
    raph.add_node(graph.Node("FD", (6,4)))
    raph.add_node(graph.Node("FE", (6,5)))
    raph.add_node(graph.Node("FF", (6,6)))
    raph.add_node(graph.Node("FG", (6,7)))
    raph.add_node(graph.Node("FH", (6,8)))
    raph.add_node(graph.Node("FI", (6,9)))
    raph.add_node(graph.Node("FJ", (6,10)))
    raph.add_node(graph.Node("FK", (6,11)))
    #y 7
    raph.add_node(graph.Node("GA", (7,1)))
    raph.add_node(graph.Node("GB", (7,2)))
    raph.add_node(graph.Node("GC", (7,3)))
    raph.add_node(graph.Node("GD", (7,4)))
    raph.add_node(graph.Node("GE", (7,5)))
    raph.add_node(graph.Node("GF", (7,6)))
    raph.add_node(graph.Node("GG", (7,7)))
    raph.add_node(graph.Node("GH", (7,8)))
    raph.add_node(graph.Node("GI", (7,9)))
    raph.add_node(graph.Node("GJ", (7,10)))
    raph.add_node(graph.Node("GK", (7,11)))
    #y 8
    raph.add_node(graph.Node("HA", (8,1)))
    raph.add_node(graph.Node("HB", (8,2)))
    raph.add_node(graph.Node("HC", (8,3)))
    raph.add_node(graph.Node("HD", (8,4)))
    raph.add_node(graph.Node("HE", (8,5)))
    raph.add_node(graph.Node("HF", (8,6)))
    raph.add_node(graph.Node("HG", (8,7)))
    raph.add_node(graph.Node("HH", (8,8)))
    raph.add_node(graph.Node("HI", (8,9)))
    raph.add_node(graph.Node("HJ", (8,10)))
    raph.add_node(graph.Node("HK", (8,11)))
    #y 9
    raph.add_node(graph.Node("IA", (9,1)))
    raph.add_node(graph.Node("IB", (9,2)))
    raph.add_node(graph.Node("IC", (9,3)))
    raph.add_node(graph.Node("ID", (9,4)))
    raph.add_node(graph.Node("IE", (9,5)))
    raph.add_node(graph.Node("IF", (9,6)))
    raph.add_node(graph.Node("IG", (9,7)))
    raph.add_node(graph.Node("IH", (9,8)))
    raph.add_node(graph.Node("II", (9,9)))
    raph.add_node(graph.Node("IJ", (9,10)))
    raph.add_node(graph.Node("IK", (9,11)))
    #y 10
    raph.add_node(graph.Node("JA", (10,1)))
    raph.add_node(graph.Node("JB", (10,2)))
    raph.add_node(graph.Node("JC", (10,3)))
    raph.add_node(graph.Node("JD", (10,4)))
    raph.add_node(graph.Node("JE", (10,5)))
    raph.add_node(graph.Node("JF", (10,6)))
    raph.add_node(graph.Node("JG", (10,7)))
    raph.add_node(graph.Node("JH", (10,8)))
    raph.add_node(graph.Node("JI", (10,9)))
    raph.add_node(graph.Node("JJ", (10,10)))
    raph.add_node(graph.Node("JK", (10,11)))
    #y 11
    raph.add_node(graph.Node("KA", (11,1)))
    raph.add_node(graph.Node("KB", (11,2)))
    raph.add_node(graph.Node("KC", (11,3)))
    raph.add_node(graph.Node("KD", (11,4)))
    raph.add_node(graph.Node("KE", (11,5)))
    raph.add_node(graph.Node("KF", (11,6)))
    raph.add_node(graph.Node("KG", (11,7)))
    raph.add_node(graph.Node("KH", (11,8)))
    raph.add_node(graph.Node("KI", (11,9)))
    raph.add_node(graph.Node("KJ", (11,10)))
    raph.add_node(graph.Node("KK", (11,11)))
    # Add edges
    raph.add_edge("AA", "AB", 1)
    raph.add_edge("AB", "AC", 1)
    raph.add_edge("AC", "AD", 1)
    raph.add_edge("AD", "AE", 1)
    raph.add_edge("AE", "AF", 1)
    raph.add_edge("AE", "BE", 1)
    raph.add_edge("BE", "CE", 1)
    raph.add_edge("CE", "DE", 1)
    raph.add_edge("DE", "EE", 1)
    raph.add_edge("EE", "ED", 1)
    raph.add_edge("ED", "EC", 1)
    raph.add_edge("ED", "DD", 1)
    raph.add_edge("DD", "CD", 1)
    raph.add_edge("CD", "BD", 1)
    raph.add_edge("BD", "BC", 1)
    raph.add_edge("BC", "BB", 1)
    raph.add_edge("BC", "CC", 1)
    raph.add_edge("CC", "DC", 1)
    raph.add_edge("CC", "CB", 1)
    raph.add_edge("CB", "DB", 1)
    raph.add_edge("DB", "EB", 1)
    raph.add_edge("EB", "FB", 1)
    raph.add_edge("FB", "GB", 1)
    raph.add_edge("GB", "HB", 1)
    raph.add_edge("DB", "DA", 1)
    raph.add_edge("DA", "CA", 1)
    raph.add_edge("CA", "BA", 1)
    raph.add_edge("DA", "EA", 1)
    raph.add_edge("EA", "FA", 1)
    raph.add_edge("FA", "GA", 1)
    raph.add_edge("GA", "HA", 1)
    raph.add_edge("HA", "IA", 1)
    raph.add_edge("IA", "IB", 1)
    raph.add_edge("IB", "JB", 1)
    raph.add_edge("JB", "KB", 1)
    raph.add_edge("JB", "JC", 1)
    raph.add_edge("JC", "JD", 1)
    raph.add_edge("JD", "JE", 1)
    raph.add_edge("JE", "IE", 1)
    raph.add_edge("IE", "HE", 1)
    raph.add_edge("HE", "HD", 1)
    raph.add_edge("HD", "ID", 1)
    raph.add_edge("ID", "IC", 1)
    raph.add_edge("HD", "GD", 1)
    raph.add_edge("GD", "FD", 1)
    raph.add_edge("GD", "GC", 1)
    raph.add_edge("GC", "HC", 1)
    raph.add_edge("GC", "FC", 1)
    raph.add_edge("FC", "EC", 1)
    raph.add_edge("HE", "GE", 1)
    raph.add_edge("GE", "FE", 1)
    raph.add_edge("FE", "FF", 1)
    raph.add_edge("FF", "EF", 1)
    raph.add_edge("EF", "DF", 1)
    raph.add_edge("DF", "CF", 1)
    raph.add_edge("CF", "BF", 1)
    raph.add_edge("FF", "GF", 1)
    raph.add_edge("GF", "HF", 1)
    raph.add_edge("HF", "IF", 1)
    raph.add_edge("IF", "JF", 1)
    raph.add_edge("JF", "KF", 1)
    raph.add_edge("KF", "KE", 0)
    raph.add_edge("KE", "KD", 1)
    raph.add_edge("KD", "KC", 1)
    raph.add_edge("KC", "KB", 1)
    raph.add_edge("KB", "KA", 1)
    raph.add_edge("KA", "JA", 1)
    raph.add_edge("KF", "KG", 1)
    raph.add_edge("KG", "KH", 1)
    raph.add_edge("KH", "KI", 1)
    raph.add_edge("KI", "KJ", 1)
    raph.add_edge("KJ", "KK", 1)
    raph.add_edge("KK", "JK", 1)
    raph.add_edge("JK", "IK", 1)
    raph.add_edge("IK", "IJ", 1)
    raph.add_edge("IJ", "II", 1)
    raph.add_edge("II", "IH", 1)
    raph.add_edge("IH", "HH", 1)
    raph.add_edge("HH", "HG", 1)
    raph.add_edge("HG", "IG", 1)
    raph.add_edge("IG", "JG", 1)
    raph.add_edge("JG", "JH", 1)
    raph.add_edge("JH", "JI", 1)
    raph.add_edge("JI", "JJ", 1)
    raph.add_edge("HH", "HI", 1)
    raph.add_edge("HI", "HJ", 1)
    raph.add_edge("HJ", "HK", 1)
    raph.add_edge("HK", "GK", 1)
    raph.add_edge("GK", "GJ", 1)
    raph.add_edge("GJ", "FJ", 1)
    raph.add_edge("FJ", "EJ", 1)
    raph.add_edge("GK", "FK", 1)
    raph.add_edge("FK", "EK", 1)
    raph.add_edge("EK", "DK", 1)
    raph.add_edge("DK", "DJ", 1)
    raph.add_edge("DJ", "DI", 1)
    raph.add_edge("DI", "DH", 1)
    raph.add_edge("DH", "DG", 1)
    raph.add_edge("DG", "CG", 1)
    raph.add_edge("CG", "BG", 1)
    raph.add_edge("BG", "AG", 1)
    raph.add_edge("BG", "BH", 1)
    raph.add_edge("BH", "AH", 1)
    raph.add_edge("BH", "BI", 1)
    raph.add_edge("BI", "CI", 1)
    raph.add_edge("CI", "CH", 1)
    raph.add_edge("DG", "EG", 1)
    raph.add_edge("EG", "EH", 1)
    raph.add_edge("EH", "FH", 1)
    raph.add_edge("FH", "FG", 1)
    raph.add_edge("FG", "GG", 1)
    raph.add_edge("GG", "GH", 1)
    raph.add_edge("DI", "EI", 1)
    raph.add_edge("EI", "FI", 1)
    raph.add_edge("FI", "GI", 1)
    raph.add_edge("DJ", "CJ", 1)
    raph.add_edge("CJ", "CK", 1)
    raph.add_edge("CK", "BK", 1)
    raph.add_edge("CJ", "BJ", 1)
    raph.add_edge("BJ", "AJ", 1)
    raph.add_edge("AJ", "AI", 1)
    raph.add_edge("AJ", "AK", 1)

    

    return raph

def pathing(bot, user):
    coordinates = {"AK": (250, 250), "AJ": (200, 250), "AI": (150, 250), "AH": (100, 250), "AG": (50, 250), "AF": (0, 250), "AE": (-50, 250), "AD": (-100, 250), "AC": (-150, 250), "AB": (-200, 250), "AA": (-250, 250), 
                "BK": (250, 200), "BJ": (200, 200), "BI": (150, 200), "BH": (100, 200), "BG": (50, 200), "BF": (0, 200), "BE": (-50, 200), "BD": (-100, 200), "BC": (-150, 200), "BB": (-200, 200), "BA": (-250, 200), 
                "CK": (250, 150), "CJ": (200, 150), "CI": (150, 150), "CH": (100, 150), "CG": (50, 150), "CF": (0, 150), "CE": (-50, 150), "CD": (-100, 150), "CC": (-150, 150), "CB": (-200, 150), "CA": (-250, 150), 
                "DK": (250, 100), "DJ": (200, 100), "DI": (150, 100), "DH": (100, 100), "DG": (50, 100), "DF": (0, 100), "DE": (-50, 100), "DD": (-100, 100), "DC": (-150, 100), "DB": (-200, 100), "DA": (-250, 100), 
                "EK": (250, 50), "EJ": (200, 50), "EI": (150, 50), "EH": (100, 50), "EG": (50, 50), "EF": (0, 50), "EE": (-50, 50), "ED": (-100, 50), "EC": (-150, 50), "EB": (-200, 50), "EA": (-250, 50), 
                "FK": (250, 0), "FJ": (200, 0), "FI": (150, 0), "FH": (100, 0), "FG": (50, 0), "FF": (0, 0), "FE": (-50, 0), "FD": (-100, 0), "FC": (-150, 0), "FB": (-200, 0), "FA": (-250, 0), 
                "GK": (250, -50), "GJ": (200, -50), "GI": (150, -50), "GH": (100, -50), "GG": (50, -50), "GF": (0, -50), "GE": (-50, -50), "GD": (-100, -50), "GC": (-150, -50), "GB": (-200, -50), "GA": (-250, -50), 
                "HK": (250, -100), "HJ": (200, -100), "HI": (150, -100), "HH": (100, -100), "HG": (50, -100), "HF": (0, -100), "HE": (-50, -100), "HD": (-100, -100), "HC": (-150, -100), "HB": (-200, -100), "HA": (-250, -100), 
                "IK": (250, -150), "IJ": (200, -150), "II": (150, -150), "IH": (100, -150), "IG": (50, -150), "IF": (0, -150), "IE": (-50, -150), "ID": (-100, -150), "IC": (-150, -150), "IB": (-200, -150), "IA": (-250, -150), 
                "JK": (250, -200), "JJ": (200, -200), "JI": (150, -200), "JH": (100, -200), "JG": (50, -200), "JF": (-0, -200), "JE": (-50, -200), "JD": (-100, -200), "JC": (-150, -200), "JB": (-200, -200), "JA": (-250, -200), 
                "KK": (250, -250), "KJ": (200, -250), "KI": (150, -250), "KH": (100, -250), "KG": (50, -250), "KF": (0, -250), "KE": (-50, -250), "KD": (-100, -250), "KC": (-150, -250), "KB": (-200, -250), "KA": (-250, -250)}
    # Execute the algorithm
    x = bot.xcor()
    y = bot.ycor()
    graph = run()
    for node, coord in coordinates.items():
        if coord == (x, y):
            node = node
            break
    x = user.xcor()
    y = user.ycor()
    x = truncate(x)
    y = truncate(y)
    for node2, coord in coordinates.items():
        if coord == (x, y):
            node2 = node2
            break
    if node == node2:
        print("                 ", end = "\r")
        print("\x1B[1mYOU DIED\x1B[0m")
        sleep(1)
        exit()
    alg = a_star.AStar(graph, node, node2)
    path, path_length = alg.search()
    #print(" -> ".join(path))
    if path[1] in coordinates:
        node = path[1]
        x, y = coordinates[node]
        bot.goto(x, y)
        if bot.pos() == user.pos():
            print("                 ", end = "\r")
            print("\x1B[1mYOU DIED\x1B[0m")
            sleep(1)
            exit()
        try:
            node = path[2]
            x, y = coordinates[node]
            bot.goto(x, y)
            if bot.pos() == user.pos():
                print("                 ", end = "\r")
                print("YOU DIED")
                sleep(1)
                exit()
        except IndexError:
            print("", end= "\r")
        
    return path


    


# S -> D -> H -> J -> K -> T
# Length of the path: 17