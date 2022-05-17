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


#here to start loop


group_name="S-WA-bot"
text_paste(group_name) #search group name

sleep(1)

action3=action(748, 230)
action3.movement()
action3.mouse_click()

action4=action(1066, 499)
action4.movement()
action4.mouse_click()

sleep(1)

new_chat="http://wa.me/+919496225620"
text_paste(new_chat)



sleep(1)
action5=action(1325, 490) #send hyperlink
action5.movement()
action5.mouse_click()


sleep(3)

action6=action(1152, 421) #open link
action6.movement()
action6.mouse_click()
sleep(2)
action7=action(238, 256) #open chat in web
action7.movement()
action7.mouse_click()
sleep(1)
action8=action(988, 488) #open paper clip
action8.movement()
action8.mouse_click()
sleep(1)
action9=action(988, 432) #open gallery
action9.movement()
action9.mouse_click()
sleep(1)
action10=action(1094, 167) #select picture 
action10.movement()
action10.mouse_click()
sleep(1)
action11=action(1120, 446) #open picture
action11.movement()
action11.mouse_click()
sleep(1)
action12=action(1358, 496) #picture/video send 
action12.movement()
action12.mouse_click()
sleep(1)
action13=action(988, 488) #open paper clip
action13.movement()
action13.mouse_click()
sleep(1)
action14=action(988, 432) #open gallery
action14.movement()
action14.mouse_click()
sleep(1)
action15=action(1215, 161) #select video
action15.movement()
action15.mouse_click()
sleep(1)
action11=action(1120, 446) #open button
action11.movement()
action11.mouse_click()
sleep(5)
action16=action(1358, 496) #picture/video send 
action16.movement()
action16.mouse_click()
sleep(1)