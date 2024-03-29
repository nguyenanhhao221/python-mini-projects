import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_counts = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}


def get_slot_machine_spin(rows: int, cols: int, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    """Print the slot machine in a readable format"""
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


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


def check_winnings(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet

        return winnings


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

    slot_machine = get_slot_machine_spin(ROWS, COLS, symbol_counts)
    print_slot_machine(slot_machine)


main()
