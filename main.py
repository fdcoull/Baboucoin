# Baboucoin

from Mine.main import Mine
from Blockchain.main import Blockchain

print("Baboucoin")
print ("""1. Wallet\n
        2. Mine\n
        """)

selected = input("Enter option: ")

if selected == "1":
    print("Test 1")
elif selected == "2":
    print("Test 2")
elif selected == "3":
    Blockchain.initialise()