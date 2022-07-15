from time import sleep
from random import random
import json, random
import minecraft, rules

f = open("data.json", "r")
data = json.load(f)
f.close()

sleep(10)

# Announce closure of ticket sales
minecraft.send_announcement("Lotto ticket purchases are now closed, wiinner will be drawn shortly")

tickets_total = []
prize_pool = 0.0

# Message each customer and count tickets
for username in data:
    prize_pool += data[username]
    for _ in range(rules.tickets(data[username])):
        tickets_total.append(username)

# Announce prize pool
minecraft.send_announcement("Total pize pool of the lottery is $" + str(prize_pool) + "! Good luck!")

sleep(2)
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
minecraft.send_message(winner, "Congratulations! You won the grand prize of $" + str(prize_pool) + "! You will reveive this shortly.")

