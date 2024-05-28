# Baboucoin

from Mine.main import Mine
from Blockchain.main import Blockchain
from Wallet.main import Wallet

print("Baboucoin")
print ("""1. Wallet\n
        2. Mine\n
        3. Admin tools\n
        """)

selected = input("\nEnter option: ")

if selected == "1":
    print("Wallet")
    print(""" 1. Create\n
        2. Get address
        3. Load
        4. Get balance
        5. Send
    """)
    selected = input("\nEnter option: ")
    if selected == "1":
        Wallet.create()
    elif selected == "2":
        private = input("Enter private key: ").encode()
        print(Wallet.getAddress(private))
    elif selected == "3":
        print(Wallet.loadFile())
        print(Wallet.load())
    elif selected == "4":
        print(Blockchain.getBalance())
    elif selected == "5":
        Blockchain.send()
    elif selected == "6":
        signature = Wallet.sign()
        print(signature)
        print(Wallet.verify(signature))
elif selected == "2":
    print("Test 2")
    Mine.mine()
elif selected == "3":
    print("--- Admin tools ---")
    print(""" 1. Clear local blockchain\n
          2. View blockchain
    """)
    selected = input("\nEnter option: ")
    if selected == "1":
        Blockchain.initialise()
    elif selected == "2":
        Blockchain.display()