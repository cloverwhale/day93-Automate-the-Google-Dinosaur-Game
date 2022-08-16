import time

import pyautogui

BLANK_THRESHOLD = 161
CACTUS_X = (85, 195)
CACTUS_Y = (105, 115)
BIRD_X = (85, 195)
BIRD_Y = (65, 90)
KEYDOWN_TIME = 0.3


# Get 2 points of game over text data
def sees_game_over_text(image):
    return image[255, 50] == 163 and image[315, 50] == 162


def run(env):
    for i in range(CACTUS_X[0], CACTUS_X[1]):
        for j in range(CACTUS_Y[0], CACTUS_Y[1]):
            if env[i, j] == BLANK_THRESHOLD:
                pyautogui.press('up')
                return
    for i in range(BIRD_X[0], BIRD_X[1]):
        for j in range(BIRD_Y[0], BIRD_Y[1]):
            if env[i, j] == BLANK_THRESHOLD:
                pyautogui.keyDown('down')
                time.sleep(KEYDOWN_TIME)
                pyautogui.keyUp('down')
                return
    return
