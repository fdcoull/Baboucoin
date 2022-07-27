from app.baboucoin.Mine.main import Mine
from app.baboucoin.Wallet.main import Wallet

menuHeader = "Baboucoin version Dev-1.1.0\n"
menuDivider = "=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
menuCursor = "=> "

class Menu():
    def mainMenu():
        title = "Main Menu\n"
        options = ["1) Mine", "2) Wallet", "3) Exit"]

        print(menuHeader+menuDivider+title+menuDivider)

        for item in options:
            print(item)

    def mineMenu():
        title = "Mining Menu\n"

        print(menuHeader+menuDivider+title+menuDivider)

    def walletMenu():
        title = "Wallet menu\n"
        options = ["1) Login to wallet", "2) Create wallet"]

        print(menuHeader+menuDivider+title+menuDivider)

        for item in options:
            print(item)

    def walletLoginOption():
        title = "Wallet Menu > Login\n"

        print(menuHeader+menuDivider+title+menuDivider)

    def walletCreateOption():
        title = "Wallet Menu > Create\n"

        print(menuHeader+menuDivider+title+menuDivider)

    menu = True

    while(menu):
        mainMenu()

        #Main menu
        userInput = input(menuCursor)

        if userInput == '1':
            #Mining menu
            mineMenu()
            mine = Mine()
            mine.run()
            menu = False
        elif userInput == '2':
            #Wallet menu
            walletMenu()
            userInput = input(menuCursor)
            if userInput == '1':
                #Login option
                walletLoginOption()
                print("Enter private key:")
                print("Option unavailable for now")
                #print("Logging in...")

                menu = False
                #Run login module
            elif userInput == '2':
                #Create wallet option
                walletCreateOption()
                wallet = Wallet()
                wallet.create()
                menu = False
        elif userInput == '3':
            print("Exiting...")
            menu = False
        else:
            print("Invalid option")

menu = Menu()
