import random
import time

def LineGen(line_length):
    line = str(random.randint(2, 5))
    height = int(line)
    
    for i in range(line_length):
        arr = [height] * 4
        if height < 9:
            arr.append(height + 1)
        if height > 0: 
            arr.append(height - 1)
        
        height = random.choice(arr)
        line += str(height)
    return line

def ArrayConvert(line):
    #uses vertical 2d array represebtation
    line_length = len(line)
    terrain = [[0 for _ in range(10)] for _ in range(line_length)]
    for position in range(line_length):
        terrain[position][int(line[position])] = 1
    

curr = time.time()
line = LineGen(10000)
ArrayConvert(line)

print(time.time() - curr)