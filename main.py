import random
import time

def LineGen(line_length):
    line = str(random.randint(2, 5))
    height = int(line)
    
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
def slicer(arr, xpos, slice_size):
    return arr[:]


curr = time.time()
line = LineGen(1000)
terrain = LineConversion(line)
print(time.time() - curr)
slicer(terrain, 10)
