import random
import time
from pynput import keyboard
import pyautogui


def LineGen(line_length):  
    height = random.randint(2, 5)
    line = str(height)
    
    for i in range(line_length):
        arr = [height] * 4
        if height < 9:
            arr.append(height + 1)
        if height > 1: 
            arr.append(height - 1)
        
        height = random.choice(arr)
        line += str(height)
    return line


def LineConversion(line):
    line_length = len(line)
    arr = [[0 for i in range(10)] for j in range(line_length)]

    for i in range(line_length):
        arr[i][int(line[i])] = 1
    return arr


def Slicer(arr, xpos, slice_size):
    return arr[xpos:xpos+slice_size]


def Draw(terrain, xpos, leftx, lefty):
    terrain_slice = Slicer(terrain, xpos, 10)
    for node in terrain_slice:
        height = node.index(1)
        print(height)


curr = time.time() #starts a timer
line = LineGen(1000) #Calls LineGen()
terrain = LineConversion(line)
time.sleep(3.7669420)
leftx, lefty = pyautogui.position()
print(time.time() - curr)
print(Draw(terrain, 10, startx, starty))

