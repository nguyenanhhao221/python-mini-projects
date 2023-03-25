MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")
    return amount


def get_number_of_lines():
    while True:
        lines = input("How many lines would you like to bet? (1-3) ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= 3:
                break
            else:
                print("Amount must be between 1 and 3")
        else:
            print("Please enter a number")
    return lines


def get_bet():
    while True:
        amount = input("How much would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(
                    f"""Amount must be larger than{MIN_BET}
                      and less than {MAX_BET}"""
                )
        else:
            print("Please enter a number")
    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bets = bet * lines
        if total_bets > balance:
            print(
                f"""Your balance is not enough to make the bet.
                  Your current balance is {balance}"""
            )
        else:
            break
    print(
        f"""You are betting ${bet} on {lines} lines.
                    Total bet is ${total_bets}"""
    )


main()
