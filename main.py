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

curr = time.time()
print(LineGen(1000))
print(time.time() - curr)