import pyautogui as pi
from time import sleep
from pointer_action import *

#Whatsapp auto boardcast bot designed by S Sidharth

class action():
    def __init__(self):
        sleep(.005)
    def movement(self ,x ,y):
        pi.moveTo(x=x, y=y ,duration=.01)
    def mouse_click(self, x ,y):
        pi.click(x=x, y=y)


action1=action()
action1.movement(905, 747)
action1.mouse_click(905, 747)