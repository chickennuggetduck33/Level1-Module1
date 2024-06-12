"""
Turtle Race
"""
import turtle
import random
from PIL import Image

# ================= Instructions at the bottom of this file ===================


def screen_clicked(x, y):
    print('You pressed: x=' + str(x) + ', y=' + str(y))


def draw_background():
    filename = 'race_track.gif'

    try:
        image = Image.open(filename)
    except(FileNotFoundError, IOError):
        print("ERROR: Unable to find file " + filename)
        return

    window = turtle.Screen()
    window.setup(image.width + 100, image.height + 100, startx=0, starty=0)
    window.bgpic(filename)
    window.onclick(screen_clicked)

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    draw_background()
    waffle = 185
    turtlelist = []
    for i in range(8):

    # TODO 1) Create an empty list of turtles

    # TODO 2) Create a new turtle and set its shape to 'turtle
        beans = turtle.Turtle()
        beans.shape("turtle")
    # TODO 3) Set the turtle's speed to 3
        beans.speed(3)
    # TODO 4) Set the turtle's pen up
        beans.penup()
    # TODO 5) Use the turtle's goto() method to set its position on the left
    #  side of the screen
        beans.goto(-400, waffle)
    # TODO 6) use a loop to repeat the previous instructions and create
    #  8 turtles lined up on the left side of the screen
    #  *HINT* click on the window to print the corresponding x, y location
        waffle = waffle - 53
        turtlelist.append(beans)
    # TODO 7) Move each turtle forward a random distance between 1 and 20
    chip = True
    winner = None
    while chip:
        for x in turtlelist:
            potato = random.randint(1, 20)
            x.forward(potato)
            if x.xcor()>340:
                winner = turtlelist.index(x) + 1
                chip = False
                break
    print(f"the winner is turtle {winner}")
    # TODO 8) Create a loop to keep moving each turtle until a turtle
    #  crosses the finish line
    #  *HINT* click on the window to print the corresponding x, y location

    # TODO 9) When a turtle crosses the finish line, stop the race and
    #  indicate which turtle won the race.

    # EXTRA: Create different colors for each turtle and code a special
    # dance for the winning turtle!

    turtle.done()
