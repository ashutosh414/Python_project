'''
It is a spin casino project. Where we input total amount. After how much you want to bet and how many lines you want to bet on.
'''




import random

ROWS=3
COLS=3

MAX_LINES = 3
MAX_BET=100
MIN_BET=1

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8

}

symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2

}

def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line+1)
        return winnings, winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns=[]
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value= random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        
        print()



def deposit():
    while True:
        amount= input('Enter the Deposite amount. $')
        if amount.isdigit() and int(amount)>0:
            break
        else:
            print("please enter a valid number and number shoud be greater then 0")
    return int(amount)

def get_number_of_lines():
    while True:
        Lines= input('Enter the lines to bet on (1- ' + str(MAX_LINES)+ ')? ')
        if Lines.isdigit() and 1<= int(Lines) <= MAX_LINES:
            break
        else:
            print("please enter a valid number of lines and number shoud be greater then 0")
    return int(Lines)

def get_bet():
    while True:
        amount= input('What would you want to bet? $ ')
        if amount.isdigit() and MIN_BET<= int(amount) <= MAX_BET:
            break
        else:
            print(f"enter amountmust be ${MIN_BET} - ${MAX_BET}.")
    return int(amount)

def game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet=bet*lines

        if total_bet > balance:
            print(f"You donot have enought to bet that amunt, your current balance is: ${balance}")
        else:
            break
    print(f"you are betting ${bet} on {lines} lines. Total bet amount is equal to ${total_bet}.")

    slots= get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines= check_winnings(slots,lines,bet,symbol_value)
    print(f"you won ${winnings} ")
    print(f'you won on',*winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        spin1=  input('press enter to spin or q to Quit')
        if spin1 =="q":
            break
        balance +=game(balance)

    print(f'you left with ${balance}')
main()
