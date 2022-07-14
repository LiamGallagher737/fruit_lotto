from math import floor
import time, os, json
import pyautogui

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def tickets(payment):
    return floor(payment / 1000.0)

if __name__ == "__main__":
    logfile = open(os.getenv("APPDATA")+"/.minecraft/logs/latest.log", "r")
    loglines = follow(logfile)

    for line in loglines:

        # Filer non payment messages
        if "[CHAT]" not in line:
            continue
        if "$" not in line:
            continue
        if " has been received from " not in line:
            continue

        # Get username and payment amount
        words = line.split()
        username = words[-1][:-1]
        payment = float(words[4][1:].replace(',', ''))

        # Print to console
        print("Received payment of $" + str(payment) + " from " + username)

        # Save to log file
        f = open("log.txt", "a")
        f.write(username + ": $" + str(payment) + "\n")
        f.close()

        # Load data from data file
        f = open("data.json", "r")
        data = json.load(f)
        f.close()

        # Add new payment data
        if username in data:
            data[username] = data[username] + payment
        else:
            data[username] = payment

        # Save to data file
        f = open("data.json", "w")
        f.write(json.dumps(data, indent=1))
        f.close()

        # Notify the user that everything was successful
        pyautogui.press('/')
        pyautogui.typewrite("msg " + username + " Successfully added $" + str(payment) + " to your balance. Your total is now $" + str(data[username]) + " for a total of " + str(tickets(data[username])) + " tickets. Good luck!")
        pyautogui.press('enter')
