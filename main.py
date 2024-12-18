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
    terrain_slice = Slicer(terrain, xpos, SliceSizeInput)
    for node in terrain_slice:
        height = node.index(1)
        print(height)

#USER CONFIG
LineLength = 1000
SliceSizeInput = 100
slicestart = 10
#USER CONFIG


curr = time.time() #starts a timer
line = LineGen(LineLength) #Calls LineGen()
terrain = LineConversion(line)
print("Move yo dam cursor to where u want dat code to top left")
#time.sleep(3.7669420)
startx, starty = pyautogui.position()
print(time.time() - curr)
Draw(terrain, slicestart, startx, starty)

