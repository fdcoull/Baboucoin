import time
import hashlib

from Blockchain.main import Blockchain

class Mine():
    def mine():
        address = input("\nEnter wallet address: ")

        difficultyHex = "0000f"

        awaitingMatch = True
        nonce = 0

        # Get details from previous block
        height = Blockchain.checkHeight() + 1
        previousHash = Blockchain.checkPreviousHash()

        # Check difficulty hash isn't over digits and append trailing 0s
        if len(difficultyHex) < 64:
            while len(difficultyHex) < 64:
                difficultyHex = difficultyHex + "0"
        elif len(difficultyHex) > 64:
            awaitingMatch == False
            print("Error: Difficulty too high")
        

        while awaitingMatch:
            # Set timestamp
            timestamp = round(time.time())

            # Set new header hash input by concatenating fields
            newHeaderHashInput = str(height) + str(previousHash) + difficultyHex + str(timestamp) + str(nonce)

            # Hash header
            newHeaderHash = hashlib.sha256(newHeaderHashInput.encode('utf-8')).hexdigest()
            print(newHeaderHash)

            # Check if header hex is less than or equal to difficulty hex
            if int(newHeaderHash, 16) <= int(difficultyHex, 16):
                print("SUCCESS")
                Blockchain.reward(height, previousHash, difficultyHex, timestamp, nonce, address)

                awaitingMatch = False

            nonce += 1