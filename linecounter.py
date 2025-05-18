#-----------------------------------------------------------------#
# This is a purely debugging file, it's only purpose is to count
# all of the lines on Bive
#-----------------------------------------------------------------#

import time as t
import pathlib

from config import VERSION

counterOfLines = 0
def countLinesFromFiles(file):

    global counterOfLines

    file = open(pathlib.Path(file), "r")

    # Reading from file
    Content = file.read()
    CoList = Content.split("\n")

    for i in CoList:
        if i:
            counterOfLines += 1


def countLinesAllFiles():
    countLinesFromFiles("blocks.py")
    countLinesFromFiles("config.py")
    countLinesFromFiles("graphics.py")
    countLinesFromFiles("initialize.py")
    countLinesFromFiles("inventory.py")
    countLinesFromFiles("linecounter.py")
    countLinesFromFiles("loadingscreen.py")
    countLinesFromFiles("MAIN.py")
    countLinesFromFiles("player.py")
    countLinesFromFiles("splashtexts.py")
    countLinesFromFiles("terrain.py")
    countLinesFromFiles("titlescreen.py")

countLinesAllFiles()
t.sleep(1)
print("The total number of lines in Bive", VERSION, " is:")
print(counterOfLines)
t.sleep(1)
print("Analized a total of 12 files")

