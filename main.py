from art import logo
from functions import clean_screen, should_continue, is_valid_amount, get_highest_bidder

if __name__ == '__main__':

    bidders = []

    has_bidder = True

    while has_bidder:
        '''print logo'''
        print(logo)

        bidder_info = {}

        name = input("What is your name?: ").strip()
        bidder_info['name'] = name

        has_no_bid = True
        while has_no_bid:
            bid_amount = input("What is your bid?: $").strip()

            if is_valid_amount(bid_amount):
                bid_amount = int(bid_amount)
                has_no_bid = False
            else:
                print("Invalid input. Please input a valid amount")
        
        bidder_info['amount'] = bid_amount

        bidders.append(bidder_info)


        if should_continue() == False:
            has_bidder = False
        else:
            clean_screen()
    

    highest_bidder = get_highest_bidder(bidders)
    
    clean_screen()
    print(logo)
    print(f"The winner is {highest_bidder['name']} with a bid of ${highest_bidder['amount']}.")


