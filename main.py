# Baboucoin

from Mine.main import Mine
from Blockchain.main import Blockchain
from Wallet.main import Wallet

print("Baboucoin")
print ("""1. Wallet\n
        2. Mine\n
        """)

selected = input("\nEnter option: ")

if selected == "1":
    print("Wallet")
    print(""" 1. Create\n
        2. Load
    """)
    selected = input("\nEnter option: ")
    if selected == "1":
        Wallet.save()
    elif selected == "2":
        print(Wallet.load())

elif selected == "2":
    print("Test 2")
    Mine.mine()
elif selected == "3":
    Blockchain.initialise()
elif selected == "4":
    Blockchain.display()
elif selected == "5":
    Blockchain.checkPreviousHash()