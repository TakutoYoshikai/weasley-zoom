import pyautogui
import time
import datetime
import sys
import subprocess
from subprocess import PIPE

def main():
    hour = int(sys.argv[1])
    minute = int(sys.argv[2])
    while True:
        now = datetime.datetime.now()
        if now.hour == hour and now.minute == minute:
            subprocess.run("killall zoom.us", shell=True, stdout=PIPE, stderr=PIPE, text=True)
            sys.exit()
        time.sleep(1)

if __name__ == "__main__":
    main()
