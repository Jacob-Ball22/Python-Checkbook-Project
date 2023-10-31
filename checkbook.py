#imports
import os
import subprocess
import datetime
from checkbook_functions import * 

#starts checkbook if .txt file is present
if os.path.exists('balance.txt'):
    print('~~~ Welcome to your terminal checkbook! ~~~')
#creates .txt file then starts if not already present
else:
    print('.txt file does not exist, creating file.')
    with open('balance.txt', 'w') as bal:
        bal.write('0.00')
    print('~~~ Welcome to your terminal checkbook! ~~~')
    
    
#sets current balance to be retrived by the if statements and current date
current_balance = get_balance_from_file('balance.txt')
now = datetime.datetime.now()

#the main menu that will be repeated until exit is chosen
loop = True
while loop == True:
    #print statements for choices
    print('What would you like to do?\n')
    print('1) view current balance')
    print('2) record a debit (withdraw)')
    print('3) record a credit (deposit)')
    print('4) exit' )
    #your entry print statement and input
    print('Your Choice?\n')
    choice = input()

    #shows current balance through get_balance_from_file function
    if choice == '1':
        print('Your Current Balance Is $' + str(current_balance)+'\n')
    #uses withdrawmoney function to get withdrawn amount from input
    elif choice == '2':
        print('How Much Would You Like To Withdraw?')
        withdraw = withdraw_money(float(input()), current_balance, now)
    #uses depositmoney function to get deposited amount from function   
    elif choice == '3':
        print('How Much Would You Like To Deposit?')
        deposit = deposit_money(float(input()), current_balance, now)
    #if choice is equal to 4 then, it sets loop to false so it ends the while statement
    elif choice == '4':
        loop = False
        print('Exiting')
    #given any non useable inputs it will put out 'invalid choice'   
    else:
        print('Invalid Choice')
    