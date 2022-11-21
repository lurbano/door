
# Note: Julian's file form his portal repository.

import time
import os
import subprocess
import board
import digitalio
import random


os.system('amixer cset numid=1 100%')
os.system("cvlc --play-and-exit /home/pi/door/sounds/portal_start.mp3")

filelist = os.listdir("/home/pi/door/sounds")
# subprocess.Popen('amixer cset numid=1 100%', shell=True)
# subprocess.Popen("cvlc --play-and-exit /home/pi/portal/portal_start.mp3", shell=True)

s1 = digitalio.DigitalInOut(board.D17)
s1.direction = digitalio.Direction.INPUT
s1.pull = digitalio.Pull.DOWN

isopen = s1.value


while True:
        #if (s1.value) == True:
        #       print("closed")
        #else:
        #        print("open")
        if (s1.value != isopen):
                isopen = s1.value
                if isopen == True:
                        print("closed")
                else:
                        print("open")
                        soundFile = f"/home/pi/door/sound/{random.choice(filelist)}"
                        os.system(f"cvlc --play-and-exit {soundFile})

        time.sleep(0.05)