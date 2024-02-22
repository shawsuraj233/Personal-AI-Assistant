import webbrowser
import pyautogui
from time import sleep
def whatsappmessage(name,message):
    webbrowser.open("https://web.whatsapp.com/")
    sleep(15)
    for i in range(7):
        pyautogui.press("tab")
        sleep(0.2)
    sleep(1)
    pyautogui.typewrite(name)
    pyautogui.press("enter")
    sleep(0.1)
    for i in range (2):
        pyautogui.press("tab")
        sleep(0.1)
    pyautogui.press("enter")
    sleep(0.5)
    pyautogui.write(message)
    pyautogui.press("enter")