from time import sleep
from random import random
import random, app

data = app.get_data()

tickets = []

for user in data:
    for _ in range(data[user]):
        tickets.append(user)

app.log("Total tickets: ", str(len(tickets)))

winner = random.choice(tickets)

app.log(winner, "won the lotto")
