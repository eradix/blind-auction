import os

'''clear the screen'''
def clean_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

# check if variable is valid amount
def is_valid_amount(variable):
    try:
        int_value = int(variable)
        return True
    except ValueError:
        return False
    

# get user decision to continue app
def should_continue():
    while True:
        user_input = input("Are there any other bidders? Type 'yes or 'no'. \n").lower().strip()
        
        if user_input == "yes":
            return True
        elif user_input == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# get the highest bidder
def get_highest_bidder(bidders_dic):
    highest_bidder = {}    
    for bidder in bidders_dic:
        if highest_bidder == {}:
            highest_bidder['name'] = bidder['name']
            highest_bidder['amount'] = bidder['amount']
        elif bidder['amount'] > highest_bidder['amount']:
            highest_bidder['name'] = bidder['name']
            highest_bidder['amount'] = bidder['amount']

    return highest_bidder
