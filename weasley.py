import pyautogui
import time
import datetime
import sys


def main():
    hour = int(sys.argv[1])
    minute = int(sys.argv[2])
    while True:
        now = datetime.datetime.now()
        if now.hour == hour and now.minute == minute:
            pyautogui.keyDown("command")
            pyautogui.press("w")
            pyautogui.keyUp("command")
            time.sleep(0.4)
            pyautogui.press("enter")
            sys.exit()
        time.sleep(1)

if __name__ == "__main__":
    main()
