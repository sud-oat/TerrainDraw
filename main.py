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
    return terrain[max(0, pos - 10) : pos]


def terrain_draw(terrain, left_x, left_y):
    pyautogui.moveTo(left_x, left_y + (10 - terrain[0].index(1)) * 40)
    for node in terrain:
        height = node.index(1)
        pyautogui.mouseDown()
        pyautogui.moveTo(left_x, left_y + (10 - height) * 40)
        pyautogui.mouseUp()
        left_x += 100


def on_press(key, terrain, current_terrain_position):
    if key in (keyboard.Key.left, keyboard.Key.right):
        if key == keyboard.Key.left:
            current_terrain_position = max(0, current_terrain_position - 1)
        elif key == keyboard.Key.right:
            current_terrain_position = min(len(terrain), current_terrain_position + 1)

        temp = slice_terrain(terrain, current_terrain_position)

        simulate_key_press([keyboard.Key.ctrl, "a"])
        time.sleep(0.01)
        simulate_key_press([keyboard.Key.delete])
        simulate_key_press("p")

        terrain_draw(temp, left_x, left_y)

    return current_terrain_position


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
