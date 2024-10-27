import random
import time
from pynput import keyboard

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
    # Uses vertical 2D array representation
    line_length = len(line)
    terrain = [[0 for _ in range(10)] for _ in range(line_length)]
    for position in range(line_length):
        terrain[position][int(line[position])] = 1
    return terrain  # Return the terrain array

def slice_terrain(terrain, pos):
    return terrain[max(0, pos-10):pos]

def terrain_draw(terrain):
    # Draw the terrain slice
    for row in terrain:
        print("".join(str(x) for x in row))
    print("--------------")

def on_press(key, terrain, terrain_pos):
    if key == keyboard.Key.left:
        terrain_pos = max(0, terrain_pos - 1)
    elif key == keyboard.Key.right:
        terrain_pos = min(len(terrain), terrain_pos + 1)
    
    terrain_draw(slice_terrain(terrain, terrain_pos))

    return terrain_pos 

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def main():
    curr = time.time()
    line = LineGen(10000)
    terrain = ArrayConvert(line)
    terrain_pos = 10  # Starting position

    terrain_draw(slice_terrain(terrain, terrain_pos))  # Draw initial terrain slice

    def listener_on_press(key):
        nonlocal terrain_pos
        terrain_pos = on_press(key, terrain, terrain_pos)

    with keyboard.Listener(on_press=listener_on_press, on_release=on_release) as listener:
        listener.join()
    
    print("Elapsed time:", time.time() - curr)

if __name__ == "__main__":
    main()
