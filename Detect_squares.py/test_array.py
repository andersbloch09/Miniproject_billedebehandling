import pyautogui
import time

while 1:
    x, y = pyautogui.position()
    r,g,b = pyautogui.pixel(x, y)
    print(r,g,b)
    time.sleep(0.1)
    
    
    hav = 0,86,179
    grøn = 89,144,35
    gul = 190,168,7
    skov = 37,72,17
    mudder = 137,131,98 and 99,82,46
    