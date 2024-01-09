# Baboucoin
# Created by Finlay Daniel Coull
# 2022-07-27
# Mine module

#TODO
#-Check if new block added to blockchain - maybe by checking blockchain height at process start and checking its unchanged every iteration
#-Calculate merkle root
#-Implement into menu

import hashlib
import json
import time

blockchainLocation = 'database/blockchain/blockchain.json'

class Mine():
    def run(self):
        #Initial variables
        difficultyHex = "00000f"
        merkleTreeRoot = "example"

        #Get from root class
        menuCursor = "=> "

        print("Input public wallet key:")
        publicKey = input(menuCursor)

        #Read blockchain
        with open(blockchainLocation, "r") as file:
            blockchain = json.load(file)

        if blockchain:
            #Get previous hash
            print("data true")
            blockchainHeight = len(blockchain)
            blockchainHeightPrevious = blockchainHeight - 1
            previousHeader = blockchain[blockchainHeightPrevious]["header"]["previousHash"] + blockchain[blockchainHeightPrevious]["header"]["difficulty"] + str(blockchain[blockchainHeightPrevious]["header"]["timestamp"]) + blockchain[blockchainHeightPrevious]["header"]["merkleTreeRoot"] + str(blockchain[blockchainHeightPrevious]["header"]["nonce"])
            previousHash = hashlib.sha256(previousHeader.encode('utf-8')).hexdigest()
            print(previousHash)
        else:
            #Set previous hash to 0
            print("data false")
            previousHash = "0"

        #Declare loop variables
        awaitingMatch = True
        nonce = 0

        #Add suffix zeros to difficulty
        if len(difficultyHex) < 64:
            while len(difficultyHex) < 64:
                difficultyHex = difficultyHex + "0"
        elif len(difficultyHex) > 64:
            awaitingMatch == False
            print("Error: Difficulty too high")

        #Search for hash below difficulty target
        while awaitingMatch:
            #Emergency stop check
            if nonce < 50000000:
                #Declare current timestamp
                timestamp = round(time.time(), 4)

                #Calculate hash
                newHeaderHashInput = previousHash + difficultyHex + str(timestamp) + merkleTreeRoot + str(nonce)
                newHeaderHash = hashlib.sha256(newHeaderHashInput.encode('utf-8')).hexdigest()
                print(newHeaderHash)

                #Target hit check
                if int(newHeaderHash, 16) <= int(difficultyHex, 16):
                    print("SUCCESS")

                    #Set dictionaries ready for append to blockchain
                    newHeader = {
                            "previousHash": previousHash,
                            "difficulty": difficultyHex,
                            "timestamp": timestamp,
                            "merkleTreeRoot": merkleTreeRoot,
                            "nonce": nonce
                    }

                    newBody = [
                        {"from": "0", "signature": "example", "to": publicKey, "value": 100}
                    ]

                    #Below will be taken from mempool
                    #newTransaction = {
                    #    "from": "danil", "signature": "example", "to": "example", "value": 100
                    #}

                    #newBody.append(newTransaction)

                    newBlock = {
                        "header": newHeader,
                        "body": newBody
                    }

                    #Append to blockchain
                    blockchain.append(newBlock)

                    #Write to blockchain
                    with open(blockchainLocation, "w") as file:
                        json.dump(blockchain, file)

                    awaitingMatch = False

                nonce += 1
            else:
                awaitingMatch = False
                print("Error: Too many tries")
