import pyautogui
import time
import random


class MouseController:
    def __init__(self):
        pass

    def click_to(self, x=None, y=None, button='left'):
        if x is not None and y is not None:
            pyautogui.click(x, y, button=button)
        else:
            pyautogui.click(button=button)

    def move_to(self, x, y, duration=0.0):
        pyautogui.moveTo(x, y, duration=duration)

    def motion_loop(self, time_sec_total):
        time_sec = 0
        time_left = time_sec_total
        for time_sec in range(time_sec_total):
            random_x = random.randint(1,3840)
            random_y = random.randint(1,2400)
            waiting_duration = random.randint(1,10)
            self.move_to(random_x, random_y)
            print("Your mouse location, X:" + str(random_x) + "; " + "Y:" + str(random_y) + "; " )
            print("Waiting for " + str(waiting_duration) + " sec")
            time.sleep(waiting_duration)
            self.click_to(1, 1)
            print("Your mouse location, X:" + "1" + "; " + "Y:" + "1" + "; " )
            time_sec = time_sec + waiting_duration
            time_left = time_left - time_sec

            if time_left > 0:
                print("You are at: " + str(time_sec) + "secs")
                print("There are " + str(time_left) + "secs left\n")
                continue
            else:
                print("Process is over.")
                break

# Usage
if __name__ == "__main__":
    mouse = MouseController()
    time_sec_total = 30
    mouse.motion_loop(time_sec_total)


