def is_command(line):
    if "[CHAT]" not in line:
        return False
    if " -> me] " not in line:
        return False
    return True

def is_payment(line):
    if "[CHAT]" not in line:
        return False
    if "$" not in line:
        return False
    if " has been received from " not in line:
        return False
    return True
