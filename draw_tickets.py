from math import floor
from time import sleep
from random import random
import json, random
import minecraft

def tickets(payment):
    return floor(payment / 1000.0)

f = open("data.json", "r")
data = json.load(f)
f.close()

sleep(10)

# Announce closure of ticket sales
minecraft.send_announcement("Lotto ticket purchases are now closed, everyone who purchased a ticket will receive a message confirming their tickets")

tickets_total = []
prize_pool = 0.0

# Message each customer and count tickets
for username in data:
    sleep(2)
    minecraft.send_message(username, "You have got " + str(tickets(data[username])) + " tickets from $" + str(data[username]) + ". Good luck!")
    prize_pool += data[username]
    for _ in range(tickets(data[username])):
        tickets_total.append(username)

# Announce prize pool
minecraft.send_announcement("Total pize pool of the lottery is $" + str(prize_pool) + "! Good luck!")

sleep(7)
minecraft.send_announcement("3")
sleep(1)
minecraft.send_announcement("2")
sleep(1)
minecraft.send_announcement("1")
sleep(1)

# Pick random winner
winner = random.choice(tickets_total)

# Announce winner
minecraft.send_announcement("The winner is " + winner + "! Congratulations!")

# Message winner
minecraft.send_message(username, "Congratulations! You won the grand prize of $" + str(prize_pool))
