import pyautogui as pag
import PIL
import time
import keyboard

def findAndClick(path):
    # Will find the image, then click it. 
    # Returns false and terminates if nothing is found
    coords = pag.locateCenterOnScreen(path, confidence = 0.8)

    if coords == None:
        return False
    else:
        x, y = coords
        pag.click(x, y)
        return True

def storyMode():
    inMission = True

    print('Press W or Ctrl+C for break the script')

    while (keyboard.is_pressed('w') == False): 

        if inMission: # Find the buttons when we're in a mission (inMission = True)
            if findAndClick("assets\\auto-off.png"):
                time.sleep(45)
                continue

            elif findAndClick('assets\\skip-conv.jpg'):
                time.sleep(2)
                continue 

            elif findAndClick('assets\\friend-request.jpg'):
                continue

            elif findAndClick("assets\\next-quest.png") == True:
                inMission = False
                time.sleep(5)
                continue

        else: # What to do when we're not in a mission
            if findAndClick('assets\\prep-quest.jpg'):
                continue

            elif findAndClick('assets\\start-quest.jpg'):
                time.sleep(5)
                continue

            elif findAndClick('assets\\skip-conv.jpg'):
                continue

storyMode()