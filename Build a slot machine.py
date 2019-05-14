'''
Date: 08/06/2018
Author: Hanrui Tang
Luck of the Graw

Build a slot machine
- if the player click the button, draw shape
    for each slot:
    - get a random number
    - match the number to a shape
    - draw that shape in the correct slot (each slot has a range)

    check if the player won:
    - if each slot has the same shape
    - show "winner" message
'''

import random
from graphics import *

# define the graphic window
win = GraphWin("Draw the Slot Machine", 500, 500)

# draw 3 slots
r1 = Rectangle(Point(50, 50), Point(150, 150))      # slot1
r1.draw(win)

r2 = Rectangle(Point(200, 50), Point(300, 150))     # slot2
r2.draw(win)

r3 = Rectangle(Point(350, 50), Point(450, 150))     # slot3
r3.draw(win)

# draw the play button
r4 = Rectangle(Point(200, 200), Point(300, 250))
r4.draw(win)

label = Text(Point(250, 225), "Play")
label.draw(win)

# match shapes with numbers
slots = {
    0: { # slot1
        "upper_left": Point(75, 75),
        "lower_right": Point(125, 125),
        "oval_1": Point(75, 100),
        "oval_2": Point(125, 120),
        "center": Point(100, 100),
        "tri_1": Point(100, 75),
        "tri_2": Point(75, 125),
        "tri_3": Point(125, 125)
        },
    1: { # slot2
        "upper_left": Point(225, 75),
        "lower_right": Point(275, 125),
        "oval_1": Point(225, 100),
        "oval_2": Point(275, 120),
        "center": Point(250, 100),
        "tri_1": Point(250, 75),
        "tri_2": Point(225, 125),
        "tri_3": Point(275, 125)
        },

    2: { # slot3
        "upper_left": Point(375, 75),
        "lower_right": Point(425, 125),
        "oval_1": Point(375, 100),
        "oval_2": Point(425, 120),
        "center": Point(400, 100),
        "tri_1": Point(400, 75),
        "tri_2": Point(375, 125),
        "tri_3": Point(425, 125)
        }
}

# define function for square
def square(upper_left, lower_right):
    R1 = Rectangle(upper_left, lower_right)
    R1.setFill("yellow")
    R1.draw(win)

# define function for circle
def circle(center):
    C1 = Circle(center, 40)
    C1.setFill("blue")
    C1.draw(win)

# define function for triangle
def triangle(tri_1, tri_2, tri_3):
    T1 = Polygon(tri_1, tri_2, tri_3)
    T1.setFill("red")
    T1.draw(win)

# Add more shape
# define function for Oval
def oval(oval_1, oval_2):
    O1 = Oval(oval_1, oval_2)
    O1.setFill("green")
    O1.draw(win)

# click the play button and draw the machine
while True:
    p = win.getMouse()
    print("You Clicked", p.getX(), p.getY())
    if 200 < p.getX() < 300 and 200 < p.getY() < 250:
        num_list = []
        for slot in range(3):
            choice = random.randrange(4)
            num_list.append(choice)
            print(num_list)

            # draw the shapes into each slot
            if choice == 0:
                square(slots[slot]["upper_left"], slots[slot]["lower_right"])
            elif choice == 1:
                circle(slots[slot]["center"])
            elif choice == 2:
                oval(slots[slot]["oval_1"], slots[slot]["oval_2"])
            else:
                triangle(slots[slot]["tri_1"], slots[slot]["tri_2"], slots[slot]["tri_3"])

        # show winner message
        if num_list[0] == num_list[1] == num_list[2]:
            message = Text(Point(250, 300), "Winner!")
            message.draw(win)




