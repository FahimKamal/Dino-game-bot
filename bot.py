from PIL import ImageGrab, ImageOps
import pyautogui
import time
import numpy as np

# use this game
# http://www.trex-game.skipser.com/
# The screen resolution has to be 1920 X 1080
# to be able to use this bot and game has to be set as in the screenshot
# use command xmag on linux to get the pixel coordinates


class Coordinates():
    replayBtn = (480, 438)
    dinosaur = (259, 441)


def restartGame():
    pyautogui.click(Coordinates.replayBtn)


def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print('Jump')
    pyautogui.keyUp('space')


def imageGrab():
    box = (Coordinates.dinosaur[0] + 40, Coordinates.dinosaur[1],
           Coordinates.dinosaur[0] + 70, Coordinates.dinosaur[1] + 25)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = np.array(grayImage.getcolors())
    print(a.sum())
    return a.sum()


def main():
    restartGame()
    while True:
        if imageGrab() != 997:
            pressSpace()
            # time.sleep()


if __name__ == '__main__':
    main()