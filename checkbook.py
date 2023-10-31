#imports for reading the directory and text file
import os
import subprocess
import datetime

def get_balance_from_file(filename):
    with open(filename, 'r') as file:
        line = file.readline()
        return float(line.split("$")[1].strip())
    
def update_balance_in_file(filename, new_balance):
    with open(filename, 'w') as file:
        file.write(f"${new_balance:.2f}")

        
#starts checkbook if .txt file is present
if os.path.exists('balance.txt'):
    print('~~~ Welcome to your terminal checkbook! ~~~')
#creates .txt file then starts if not already present
else:
    print('.txt file does not exist, creating file.')
    with open('balance.txt', 'w') as bal:
        bal.write('0.00')
    print('~~~ Welcome to your terminal checkbook! ~~~')
    
    
#sets current balance to be retrived by the if statements 
current_balance = get_balance_from_file('balance.txt')
now = datetime.datetime.now()

#the main menu that will be repeated until exit is chosen
loop = True
while loop == True:
    
    print('What would you like to do?\n')
    print('1) view current balance')
    print('2) record a debit (withdraw)')
    print('3) record a credit (deposit)')
    print('4) exit' )
    print('Your Choice?\n')
    choice = input()


    if choice == '1':
        print('Your Current Balance Is $' + str(current_balance)+'\n')
    
    elif choice == '2':
        print('How Much Would You Like To Withdraw?')
        withdraw = float(input())
        if withdraw > current_balance:
            print('Thats More Than You Own')
            continue
        else:
            new_balance = current_balance - withdraw
            update_balance_in_file('balance.txt', new_balance)
            print(f"Your New Balance Is: ${new_balance:.2f}\n")
            with open('historical_transactions.txt', 'a') as file:
                file.write(f'\nTransaction: -${withdraw:.2f}\nNew Balance: ${new_balance:.2f}\n' + str(now) +'\n')
    
    elif choice == '3':
        print('How Much Would You Like To Deposit?')
        deposit = float(input())
        current_balance = get_balance_from_file('balance.txt')
        new_balance = current_balance + deposit
        update_balance_in_file('balance.txt', new_balance)
        print(f"Your New Balance Is: ${new_balance:.2f}\n")
        with open('historical_transactions.txt', 'a') as file:
                file.write(f'\nTransaction: ${deposit:.2f}\nNew Balance: ${new_balance:.2f}\n' + str(now) +'\n')
                
    elif choice == '4':
        loop = False
        print('Exiting')
    else:
        print('Invalid Choice')
    