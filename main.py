import random
import time
from pynput import keyboard
import pyautogui


def LineGen(line_length):
    line = str(random.randint(2, 5))
    height = int(line)

    for _ in range(line_length - 1):
        arr = [height] * 4
        if height < 9:
            arr.append(height + 1)
        if height > 0:
            arr.append(height - 1)

        height = random.choice(arr)
        line += str(height)
    return line


def ArrayConvert(line):
    line_length = len(line)
    terrain = [[0 for _ in range(10)] for _ in range(line_length)]
    for position in range(line_length):
        terrain[position][int(line[position])] = 1
    return terrain


def slice_terrain(terrain, pos):
    return terrain[max(0, pos - 10) : pos + 1]


def terrain_draw(terrain, left_x, left_y):
    pyautogui.moveTo(left_x, left_y + (10 - terrain[0].index(1)) * 40)
    for node in terrain:
        height = node.index(1)
        pyautogui.mouseDown()
        pyautogui.moveTo(left_x, left_y + (10 - height) * 40)
        pyautogui.mouseUp()
        left_x += 100

def modify_terrain(terrain, current_terrain_position, direction):
    edge_height = terrain[current_terrain_position].index(1)
    if edge_height + direction in range(0, 10):
        terrain[current_terrain_position][edge_height] = 0
        terrain[current_terrain_position][edge_height + direction] = 1
        return True
   
def on_press(key, terrain, current_terrain_position):
    if key in (keyboard.Key.left, keyboard.Key.right, keyboard.Key.up, keyboard.Key.down):
        if key == keyboard.Key.left or key == keyboard.Key.right:
            if current_terrain_position > 10 and current_terrain_position < len(terrain):
                redraw_screen(terrain, current_terrain_position + 1 if keyboard.Key.right else current_terrain_position-1)
        else:
            if modify_terrain(terrain, current_terrain_position, 1 if key == keyboard.Key.up else -1):
                redraw_screen(terrain, current_terrain_position)


    return current_terrain_position


def redraw_screen(terrain, current_terrain_position):
    temp = slice_terrain(terrain, current_terrain_position)

    simulate_key_press([keyboard.Key.ctrl, "a"])
    simulate_key_press([keyboard.Key.delete])
    simulate_key_press("p")

    terrain_draw(temp, left_x, left_y)


def on_release(key):
    if key == keyboard.Key.esc:
        return False


def simulate_key_press(key_combination):
    keyboard_controller = keyboard.Controller()
    for key in key_combination:
        keyboard_controller.press(key)
    for key in key_combination:
        keyboard_controller.release(key)


def main():
    curr = time.time()
    line = LineGen(100)
    terrain = ArrayConvert(line)
    current_terrain_position = 10

    print(
        "Place your cursor on the top left side of the paint application. The program will start in 3 seconds."
    )
    time.sleep(3)

    global left_x, left_y
    left_x, left_y = pyautogui.position()

    pyautogui.PAUSE = 0

    terrain_draw(slice_terrain(terrain, current_terrain_position), left_x, left_y)

    def listener_on_press(key):
        nonlocal current_terrain_position
        current_terrain_position = on_press(key, terrain, current_terrain_position)

    with keyboard.Listener(
        on_press=listener_on_press, on_release=on_release
    ) as listener:
        listener.join()

    print("Elapsed time:", time.time() - curr)


if __name__ == "__main__":
    main()
