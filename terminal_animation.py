
""" terminal_animation (v1.0)

A text-based animation which runs on the command line.
The frames of the animation are loaded from the 'anim_frames' module.
A frame is simply a string of characters and the animation consists of a list of frames.

Author: mdq3
2012/05/16

"""
import sys
from sys import platform
import time
import os
import devsoft

duration = 0.15    # The duration of time in seconds between each frame.
cycles = 100       # The number of cycles the animation plays through.
command = ""

if platform == "linux" or platform == "linux2":
    command = "clear"
elif platform == "win32":
    command = "cls"

def animate_dollar():
    """Iterate through the frames, printing then clearing each one to create an animation."""
    count = 0
    while count < cycles:
        for frame in devsoft.dollar:
            print(frame)  # Print the frame in color blue.
            time.sleep(duration)
            print(os.system(command))
        count = count + 1

def animate_isometric():
    """Iterate through the frames, printing then clearing each one to create an animation."""
    count = 0
    while count < cycles:
        for frame in devsoft.isometric:
            print(frame)  # Print the frame in color blue.
            time.sleep(duration)
            print(os.system(command))
        count = count + 1

if __name__ == "__main__":
    if (len(sys.argv) > 1) and (sys.argv[1] == "isom"):
        animate_isometric()
    if (len(sys.argv) > 1) and (sys.argv[1] == "dollar"):
        animate_dollar()
    if len(sys.argv) == 1:
        animate_dollar()
    