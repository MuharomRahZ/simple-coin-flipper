import random as rd

coin = {
    1:"HEADS",
    2:"TAILS"
}

def mainMenu():
    try:
        print(f"WELCOME TO THE SIMPLE COIN FLIPPER")
        print(f"This program will help you flip a coin and see if it's heads or tails")
        print(f"---CHOOSE MENU---\n1. FLIP A COIN\n2. EXIT")
        menu = int(input("Enter your menu choice: "))
        opsiMenu(menu)
        print()
    except Exception as exception:
        print("Error: %s!\n\n" % exception)

def opsiMenu(menu):
    if menu == 1:
        coinFlipper()
    elif menu == 2:
        print("Thank you for using the Simple Coin Flipper!")
        exit()
    else:
        print("Invalid menu choice!")
        mainMenu()

def coinFlipper():
    print(f"==============================")
    print(f"You have chosen to flip a coin")
    print(f"------------------------------")
    flipcoin = coin[rd.randint(1,2)]
    print(f"The coin has been flipped and it's {flipcoin}")
    print(f"------------------------------")
    print(f"==============================")
    print()
    mainMenu()

mainMenu()
