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
        2. Get address
        3. Load
    """)
    selected = input("\nEnter option: ")
    if selected == "1":
        Wallet.create()
    elif selected == "2":
        Wallet.getAddress()
    elif selected == "3":
        print(Wallet.loadFile())
        print(Wallet.load())
    elif selected == "4":
        signature = Wallet.sign()
        print(signature)
        print(Wallet.verify(signature))
elif selected == "2":
    print("Test 2")
    Mine.mine()
elif selected == "3":
    Blockchain.initialise()
elif selected == "4":
    Blockchain.display()
elif selected == "5":
    Blockchain.checkPreviousHash()