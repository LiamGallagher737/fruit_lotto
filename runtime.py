import time, os, json
import minecraft, rules

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def log(username, message):
    print(username + " " + message)
    f = open("log.txt", "a")
    f.write(username + " " + message + "\n")
    f.close()

def get_data():
    f = open("data.json", "r")
    data = json.load(f)
    f.close()
    return data

if __name__ == "__main__":
    logfile = open(os.getenv("APPDATA")+"/.minecraft/logs/latest.log", "r")
    loglines = follow(logfile)

    # Make sure file is created and has valid json
    f = open("data.json", "a")
    if os.path.getsize("data.json") < 2:
        f.write("{}")
    f.close()

    for line in loglines:

        # Commands
        if rules.is_command(line):
            words = line.split()
            username = words[4][1:]

            # Balance command
            if "bal" in line:
                log(username, "used the bal command")
                data = get_data()
                if username in data:
                    minecraft.send_message(
                        username,
                        "Your balance is $" +
                        str(data[username])
                    )
                else:
                    minecraft.send_message(
                        username,
                        "Your account is empty :("
                    )
                continue

            # GitHub repo command
            if "code" in line:
                log(username, "used the git/code command")
                minecraft.send_message(
                    username,
                    "You can view the code at the GitHub repository LiamGallagher737/fruit_lotto"
                )
                continue

            if "active" in line:
                log(username, "used the active/on command")
                minecraft.send_message(
                    username,
                    "The lotto bot is active"
                )
                continue

        # Payments
        if rules.is_payment(line):

            words = line.split()
            username = words[-1][:-1]
            payment = float(words[4][1:].replace(',', ''))
            log(username, "paid $" + str(payment))

            data = get_data()

            if username in data:
                data[username] = data[username] + payment
            else:
                data[username] = payment

            f = open("data.json", "w")
            f.write(json.dumps(data, indent=1))
            f.close()

            if data[username] >= 25000.0:
                minecraft.send_message(
                    username,
                    "Your new balance of $" +
                    str(data[username]) +
                    " is over the 25 ticket limit ($25000), if you wish the get a partial refund of $" +
                    str(data[username] - 25000.0) +
                    " message the organizers "
                )
                continue

            minecraft.send_message(
                username,
                "Successfully added $" + str(payment) +
                " to your balance. Your total is now $" +
                str(data[username]) +
                " for a total of " +
                str(rules.tickets(data[username])) +
                " tickets. Good luck!"
            )
