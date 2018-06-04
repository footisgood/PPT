#pyinstaller -F -w -c ppt2jpgwithremarks.py

import time
import pyautogui

n=int(input('Please input the total page of the PPT:'))
time_wait=int(input('Please input the wait time:'))
print ('\n')
print ('Now you have 5 seconds to open the PPT and play...')
time.sleep(5)

for i in range(n): # Turn page
   pyautogui.keyDown('right')
   pyautogui.keyUp('right') # Take and save a screenshot
   pyautogui.screenshot('images/page_%d.jpg' % i)
   time.sleep(time_wait)
