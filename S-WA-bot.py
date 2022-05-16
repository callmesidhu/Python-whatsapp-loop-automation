from codecs import BOM_UTF16
from re import A
import pyautogui as pi
from time import sleep
from pointer_action import *

#Whatsapp auto boardcast bot designed by S Sidharth

class action():
    def __init__(self,x ,y):
        self.x=x
        self.y=y
        sleep(.005)
    def movement(self):
        pi.moveTo(x=self.x, y=self.y ,duration=.001)
    def mouse_click(self):
        pi.click(x=self.x, y=self.y)


def text_paste(paste):
    pi.typewrite(paste)


action1=action(905, 747)
action1.movement()
action1.mouse_click()

action2=action(708, 107)
action2.movement()
action2.mouse_click()

group_name="S-WA-bot"
text_paste(group_name)

sleep(1)

action3=action(748, 230)
action3.movement()
action3.mouse_click()

action4=action(1066, 499)
action4.movement()
action4.mouse_click()

sleep(1)

new_chat="http://wa.me/+91"
text_paste(new_chat)





action5=action(1325, 490)
action5.movement()
action5.mouse_click()
