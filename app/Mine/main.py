import time
import hashlib

class Mine():
    difficultyHex = "0000f"

    awaitingMatch = True
    nonce = 0

    if len(difficultyHex) < 64:
        while len(difficultyHex) < 64:
            difficultyHex = difficultyHex + "0"
    elif len(difficultyHex) > 64:
        awaitingMatch == False
        print("Error: Difficulty too high")

    timestamp = round(time.time())

    while awaitingMatch:
        newHeaderHashInput = str(nonce)
        newHeaderHash = hashlib.sha256(newHeaderHashInput.encode('utf-8')).hexdigest()
        print(newHeaderHash)

        if int(newHeaderHash, 16) <= int(difficultyHex, 16):
            print("SUCCESS")

            awaitingMatch = False

        nonce += 1