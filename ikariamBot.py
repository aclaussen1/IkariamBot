
""" Ikariam bot
Alex Claussen

A bot for the game ikariam"""

import pyautogui, time, os, logging, sys, random, copy, threading

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')

# various coordinates of objects in the game
GAME_REGION = () # (left, top, width, height) values coordinates of the entire game window
PIRATEFORTRESS_COORDS = None
PHONE_COORDS = None
TOPPING_COORDS = None
ORDER_BUTTON_COORDS = None
RICE1_COORDS = None
RICE2_COORDS = None
NORMAL_DELIVERY_BUTTON_COORDS = None
PIRATE_COORDS = None

def main():
   
    logging.debug('Program Started. Press Ctrl-C to abort at any time.')
    logging.debug('To interrupt mouse movement, move mouse to upper left corner.')
    getGameRegion()
    print("hi")
    setupCoordinates()
    pirateFortressFarming()
    

def imPath(filename):
    """A shortcut for joining the 'images/'' file path, since it is used so often. Returns the filename with 'images/' prepended."""
    return os.path.join('imagesIkariam', filename)

def getGameRegion():
    """Obtains the region that the Sushi Go Round game is on the screen and assigns it to GAME_REGION. The game must be at the start screen (where the PLAY button is visible)."""
    global GAME_REGION

    # identify the top-left corner
    logging.debug('Finding game region...')
    region = pyautogui.locateOnScreen(imPath('topRightCorner.png'))
    if region is None:
        raise Exception('Could not find game on screen. Is the game visible?')

    # calculate the region of the entire game
    topRightX = region[0] + region[2] # left + width
    topRightY = region[1] # top
    GAME_REGION = (topRightX - 640, topRightY, 640, 480) # the game screen is always 640 x 480
    logging.debug('Game region found: %s this is wrong though left over from other bot' % (GAME_REGION,))
    
def setupCoordinates():
    """Sets several of the coordinate-related global variables, after acquiring the value for GAME_REGION."""
    global PIRATE_COORDS
    
    PIRATE_COORDS = pyautogui.locateCenterOnScreen(imPath('pirateFortress.png'))
    pyautogui.click(PIRATE_COORDS, duration=0.55)
    logging.debug('PIRATE_COORDS found: %s this is wrong though left over from other bot' % (PIRATE_COORDS,))
    f()

def f():
    while True:
            time.sleep(5)
            pyautogui.click(pyautogui.locateCenterOnScreen(imPath('captureButton.png')), duration=0)
            time.sleep(60+60+40)

def pirateFortressFarming():
    
    pyautogui.click(PIRATE_COORDS, duration=0.25)

if __name__ == '__main__':
    main()
