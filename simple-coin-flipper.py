import random as rd

coin = {
    1:"HEADS",
    2:"TAILS"
}

coin2 = {
    1:"HEADS",
    2:"TAILS"
}

coin3 = {
    1:"HEADS",
    2:"TAILS"
}

coin4 = {
    1:"HEADS",
    2:"TAILS"
}

def mainMenu():
    try:
        print(f"WELCOME TO THE SIMPLE COIN FLIPPER")
        print(f"This program will help you flip a coin and see if it's heads or tails")
        print(f"---CHOOSE MENU---\n1. FLIP A COIN\n2. FLIP TWO COINS\n3. FLIP THREE COINS\n4. FLIP FOUR COINS\n5. EXIT")
        menu = int(input("Enter your menu choice: "))
        print()
        opsiMenu(menu)
        print()
    except Exception as exception:
        print("Error: %s!\n\n" % exception)

def opsiMenu(menu):
    if menu == 1:
        coinFlipper()
    elif menu == 2:
        coinFlipper2()
    elif menu == 3:
        coinFlipper3()
    elif menu == 4:
        coinFlipper4()
    elif menu == 5:
        print(f"============================================")
        print(f"Thank you for using the Simple Coin Flipper!")
        print(f"============================================")
        exit()
    else:
        print(f"=====!WARNING!======")
        print(f"INVALID MENU CHOICE!")
        print(f"====================")
        print()
        mainMenu()

def coinFlipper():
    print(f"==============================")
    print(f"You have chosen to flip a coin")
    print(f"------------------------------")
    flipcoin = coin[rd.randint(1,2)]
    print(f"|Results:                   |")
    print(f"|           {flipcoin}           |")
    print(f"------------------------------")
    print(f"==============================")
    print()
    mainMenu()

def coinFlipper2():
    print(f"=================================")
    print(f"You have chosen to flip two coins")
    print(f"---------------------------------")
    flipcoin = coin[rd.randint(1,2)]
    flipcoin2 = coin2[rd.randint(1,2)]
    print(f"|Results:                       |")
    print(f"|     Coin 1    |     Coin 2    |")
    print(f"---------------------------------")
    print(f"|               |               |")
    print(f"|     {flipcoin}     |     {flipcoin2}     |")
    print(f"|               |               |")
    print(f"=================================")
    print()
    mainMenu()


def coinFlipper3():
    print(f"==============================================")
    print(f"      You have chosen to flip three coins     ")
    print(f"----------------------------------------------")
    flipcoin = coin[rd.randint(1,2)]
    flipcoin2 = coin2[rd.randint(1,2)]
    flipcoin3 = coin3[rd.randint(1,2)]
    print(f"|Results:                                    |")
    print(f"|     Coin 1    |    Coin 2    |    Coin 3   |")
    print(f"----------------------------------------------")
    print(f"|               |              |             |")
    print(f"|     {flipcoin}     |     {flipcoin2}    |    {flipcoin3}    |")
    print(f"|               |              |             |")
    print(f"==============================================")
    print()
    mainMenu()

def coinFlipper4():
    print(f"===========================================================")
    print(f"             You have chosen to flip four coins            ")
    print(f"-----------------------------------------------------------")
    flipcoin = coin[rd.randint(1,2)]
    flipcoin2 = coin2[rd.randint(1,2)]
    flipcoin3 = coin3[rd.randint(1,2)]
    flipcoin4 = coin4[rd.randint(1,2)]
    print(f"|Results:                                                 |")
    print(f"|     Coin 1    |    Coin 2    |    Coin 3   |   Coin 4   |")
    print(f"-----------------------------------------------------------")
    print(f"|               |              |             |            |")
    print(f"|     {flipcoin}     |     {flipcoin2}    |    {flipcoin3}    |    {flipcoin4}   |")
    print(f"|               |              |             |            |")
    print(f"===========================================================")
    print()
    mainMenu()

mainMenu()
