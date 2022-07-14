import pyautogui

def send_message(username, message):
    pyautogui.press('/')
    pyautogui.typewrite("msg " + username + " LOTTERY: " + message)
    pyautogui.press('enter')

def send_announcement(message):
    pyautogui.press('t')
    pyautogui.typewrite("LOTTERY: " + message)
    pyautogui.press('enter')
