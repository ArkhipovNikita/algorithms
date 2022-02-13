def check(sequence: str) -> bool:
    balance = 0

    for c in sequence:
        if c == '(':
            balance += 1
        else:
            balance -= 1

        if balance < 0:
            return False

    return balance == 0
