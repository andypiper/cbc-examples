# A polling Cheerlights client for CodeBug Connect

import time
import urequests
import cbc
from micropython import const

CL_URL = "https://api.thingspeak.com/channels/1417/field/2/last.txt"
screen = cbc.Drawable(5,5)
# want to make "screen" an interesting shape somehow

def cheer():
    response = urequests.get(CL_URL)
    if response.status_code == 200:
        cl_color = response.text
        print(cl_color)
        screen.clear(cbc.Color(cl_color) - cbc.Color("#777777"))
        cbc.display.draw(0,0,screen)
    else:
        print("Cheerlights API failed")
        return
        
def clr_screen():
    screen.clear(cbc.Color('black'))
    cbc.display.draw(0,0,screen)
        
while True:
    cheer()
    time.sleep(const(60))
    