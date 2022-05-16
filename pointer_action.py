import pyautogui as pi
from time import sleep

sleep(5)

#To find pointer target

def pointer_position():
    pointer_live_position=pi.position()
    print(pointer_live_position)

pointer_position()
