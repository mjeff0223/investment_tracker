from app_functionality import prtfolio_class

def show_homepage():
    print("")
    print("          === Portfolio Homepage ===          ")
    print("------------------------------------------- ")
    print("| 1.    View Portfolio     | 2.    Input Buy or Sell  |")
    print("-------------------------------------------  ")
    print("------------------------------------------")
    print("| 3.  Get Stock Data     | 4.    Get Stock News (Coming Soon)   |")
    print("------------------------------------------")
    print("              5. Exit                      |   ")


def navigate_menu():
    user_choice = input("Hello, please Select an option from the menu by typing the corresponding number: ")
    if user_choice == "1":
        if prtfolio_class.portfolio != {}:
            prtfolio_class.show_portfolio(prtfolio_class.portfolio)
        else:
            print("\nYou have not made any purchases yet\n")
    elif user_choice == "2":
        prtfolio_class.add_to_portfolio(prtfolio_class.portfolio)
        print("Transaction Successful")
    elif user_choice == "3":
        prtfolio_class.get_stock_data()
    elif user_choice == "4":
        print("This feature is coming soon!")

    elif user_choice == "5":
        exit()
