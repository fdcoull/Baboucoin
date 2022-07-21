#CryptoMine v1

import hashlib
import time

#Global settings
#Mine

match = 0

counter = 0

difficultyHex = "00000f"

seed = ""

seedInput = []

#Mine class

class Mine():
    def __init__(self, difficultyHex, seed):
        self.difficultyHex = difficultyHex
        self.seed = seed

    def mine(self):

        match = 0
        counter = 0

        if len(self.difficultyHex) != 64:
            while len(self.difficultyHex) < 64:
                self.difficultyHex = self.difficultyHex + "0"

        while match != 1:
            input = (self.seed + str(counter)).encode('utf-8')
            output = hashlib.sha256(input).hexdigest()
            print(output)

            if int(output, 16) <= int(self.difficultyHex, 16):
                print(counter)
                break

            if counter > 5000000:
                print("emergency stop")
                break

            counter += 1

runMine = Mine(difficultyHex, seed)

triesCount = int(input("Enter number of seed inputs to test: "))

i = 0

while i < triesCount:
    currentSeed = i + 1
    seedInputMessage = "Test " + str(currentSeed) + ": "
    seedInput.append(input(seedInputMessage))
    runMine.seed = seedInput[i]
    runMine.mine()
    i += 1
