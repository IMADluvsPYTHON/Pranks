import time
import random
import pyautogui #install pyautogui by typing pip install pyautogui if you don't have it.

def move_mouse(how_long_in_seconds):
    start_time = time.time()
    time_elapsed = time.time() - start_time
    xsize, ysize = pyautogui.size()

    while time_elapsed < how_long_in_seconds:
        x, y = random.randrange(xsize), random.randrange(ysize)
        pyautogui.moveTo(x, y, duration=0.2)
        time_elapsed = time.time() - start_time


if __name__ == "__main__":
    pyautogui.alert("Click Here")
    #Total time(sec) the mouse will move. Change it if you want.
    move_mouse(120)
   

#If you have problem in stopping the program just restart your computer
