import time, os, json, winsound

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
        print(line)

        if "[CHAT]" not in line:
            continue

        if "[Shop]" not in line:
            continue

        if " bought [Mud Lotto Ticket] for $1,000." not in line:
            continue

        words = line.split()

        user = words[5]

        log(user, "bought a ticket")

        data = get_data()

        if user in data:
            data[user] = data[user] + 1
        else:
            data[user] = 1

        f = open("data.json", "w")
        f.write(json.dumps(data, indent=1))
        f.close()

        winsound.Beep(1000, 200)
