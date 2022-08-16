import pyautogui
import dino
from PIL import ImageGrab

'''
 Offline Version
 Default resolution of MacBook Pro 13'
'''
# Starting position
BBOX_X = 420
BBOX_Y = 179
# Canvas size
WIDTH = 600
HEIGHT = 150

if __name__ == '__main__':

    pyautogui.moveTo(BBOX_X, BBOX_Y)
    pyautogui.click()
    pyautogui.press('up')

    game_over = False
    while not game_over:
        image = ImageGrab.grab(bbox=(BBOX_X, BBOX_Y, BBOX_X + WIDTH, BBOX_Y + HEIGHT)).convert('L')
        env = image.load()
        dino.run(env)
        if dino.sees_game_over_text(env):
            game_over = True
