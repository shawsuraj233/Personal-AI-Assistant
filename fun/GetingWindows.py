import subprocess
from time import sleep


def get_current_window_title():
    try:
        result = subprocess.run(['xdotool', 'getwindowfocus', 'getwindowname'], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return "Error: xdotool command failed - Safity First"
    except FileNotFoundError:
        return "Error: xdotool not found - Please make sure it's installed - Safity First"
if __name__ == "__main__":
    while True:
        CURRENT_APP = " "
        try:
            CURRENT_APP = get_current_window_title()
            print(type(CURRENT_APP))
        except :
            CURRENT_APP = " "
        #CURRENT_APP NAME
        print(CURRENT_APP)
        CURRENT_APP_NAME=CURRENT_APP.split(" - ")[-1]
        print(CURRENT_APP_NAME)
        print("-----------")
        sleep(1)
