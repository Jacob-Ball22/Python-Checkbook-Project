def get_balance_from_file(filename):
    with open(filename, 'r') as file:
        line = file.readline()
        return float(line.split("$")[1].strip())
    
def update_balance_in_file(filename, new_balance):
    with open(filename, 'w') as file:
        file.write(f"${new_balance:.2f}")

def withdraw_money(user_entry, current_balance, now):
    if user_entry > current_balance:
           return print('Thats More Than You Own')
    else:
        new_balance = current_balance - user_entry
        update_balance_in_file('balance.txt', new_balance)
        with open('historical_transactions.txt', 'a') as file:
            file.write(f'\nTransaction: -${user_entry:.2f}\nNew Balance: ${new_balance:.2f}\n' + str(now) +'\n')
        return print(f"Your New Balance Is: ${new_balance:.2f}\n")
    
def deposit_money(user_entry, current_balance, now):
    current_balance = get_balance_from_file('balance.txt')
    new_balance = current_balance + user_entry
    update_balance_in_file('balance.txt', new_balance)
    with open('historical_transactions.txt', 'a') as file:
            file.write(f'\nTransaction: ${user_entry:.2f}\nNew Balance: ${new_balance:.2f}\n' + str(now) +'\n')
    return print(f"Your New Balance Is: ${new_balance:.2f}\n")