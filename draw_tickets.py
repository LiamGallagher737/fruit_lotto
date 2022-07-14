from math import floor
from random import random
from time import sleep
import pyautogui
import json, random

def tickets(payment):
    return floor(payment / 1000.0)

f = open("data.json", "r")
data = json.load(f)
f.close()

sleep(10)

pyautogui.press('t')
pyautogui.typewrite("Lotto ticket purchases are now closed, everyone who purchased a ticket will receive a message confirming their tickets")
pyautogui.press('enter')

tickets_total = []
prize_pool = 0.0

for username in data:
    sleep(2)
    pyautogui.press('/')
    pyautogui.typewrite("msg " + username + " You have got " + str(tickets(data[username])) + " tickets from $" + str(data[username]) + ". Good luck!")
    pyautogui.press('enter')
    prize_pool += data[username]
    for _ in range(tickets(data[username])):
        tickets_total.append(username)

pyautogui.press('t')
pyautogui.typewrite("Total pize pool of the lottery is $" + str(prize_pool) + "! Good luck!")
pyautogui.press('enter')

sleep(10)

winner = random.choice(tickets_total)

pyautogui.press('t')
pyautogui.typewrite("Congratulations " + winner + " for winning the lottery!")
pyautogui.press('enter')

pyautogui.press('/')
pyautogui.typewrite("msg " + username + " YOU WON! You will receive your money shortly!")
pyautogui.press('enter')
