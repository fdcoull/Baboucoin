import sqlite3
from contextlib import closing
import hashlib


class Blockchain:
    def initialise():
        # Create database connection
        connection = sqlite3.connect("blockchain.db")
        cursor = connection.cursor()

        # Create headers table
        cursor.execute("DROP TABLE IF EXISTS headers")
        cursor.execute("""CREATE TABLE headers (
            height INTEGER, 
            previous_hash TEXT,
            difficulty TEXT, 
            timestamp INTEGER, 
            nonce INTEGER, 
            PRIMARY KEY('height' AUTOINCREMENT)
        )""")
        
        # Create transactions table
        cursor.execute("DROP TABLE IF EXISTS transactions")
        cursor.execute("""CREATE TABLE transactions (
            height INTEGER, 
            sender TEXT, 
            recipient TEXT, 
            value DECIMAL(6,3), 
            signature TEXT
        )""")

        # Create mempool table
        cursor.execute("DROP TABLE IF EXISTS mempool")
        cursor.execute("""CREATE TABLE mempool (
            sender TEXT,
            recipient TEXT,
            value DECIMAL(6,3),
            signature TEXT
        )""")

        # test addition
        #cursor.execute("INSERT INTO headers (previous_hash, difficulty, timestamp, nonce) VALUES ('AB123', '000F', 17, 1)")
        #cursor.execute("INSERT INTO headers (difficulty, timestamp, nonce) VALUES ('000F', 18, 24)")

        #cursor.execute("INSERT INTO transactions (height, timestamp, sender, recipient, value, signature) VALUES (1, 23, 'a', 'b', 50.123, 'jhsdhghg')")

        #cursor.execute("INSERT INTO mempool (timestamp, sender, recipient, value, signature) VALUES (23, 'a', 'b', 50.123, 'jhsdhghg')")

        rows = cursor.execute("SELECT * FROM headers").fetchall()
        print(rows)

        rows = cursor.execute("SELECT * FROM transactions").fetchall()
        print(rows)

        rows = cursor.execute("SELECT * FROM mempool").fetchall()
        print(rows)

        connection.commit()
        connection.close()

    def checkHeight():
        connection = sqlite3.connect("blockchain.db")
        cursor = connection.cursor()

        row = cursor.execute("SELECT height FROM headers ORDER BY height DESC LIMIT 1").fetchall()

        if len(row) < 1:
            # Set height to -1 if blockchain empty
            height = -1
        else:
            # Set height to current height if blockchain not empty
            height = row[0][0]

        print(height)

        connection.close()

        return height
    
    def checkPreviousHash():
        connection = sqlite3.connect("blockchain.db")
        cursor = connection.cursor()

        row = cursor.execute("SELECT * FROM headers ORDER BY height DESC LIMIT 1").fetchall()

        if len(row) < 1:
            # Set previous hash to none if blockchain empty
            previousHash = None
        else:
            # Calculate previous hash by concatenating previous block fields and hashing
            previousHashInput = str(row[0][0]) + str(row[0][1]) + str(row[0][2]) + str(row[0][3]) + str(row[0][4])
            previousHash = hashlib.sha256(previousHashInput.encode('utf-8')).hexdigest()

        return previousHash
    
    def add(height, previousHash, difficulty, timestamp, nonce, address):
        print("Added")
        connection = sqlite3.connect("blockchain.db")
        cursor = connection.cursor()

        cursor.execute("INSERT INTO headers (height, previous_hash, difficulty, timestamp, nonce) VALUES (" + str(height) + ", '" + str(previousHash) + "', '" + difficulty + "', " + str(timestamp) + ", " + str(nonce) + ")")
        cursor.execute("INSERT INTO transactions (height, sender, recipient, value, signature) VALUES (" + str(height) + ", NULL, '" + str(address) + "', " + str(10) + ", NULL)")


        # Also add transactions here (mempool)
        connection.commit()
        connection.close()

    def display():
        # Display blockchain headers
        connection = sqlite3.connect("blockchain.db")
        cursor = connection.cursor()

        print("Blockchain")
        rows = cursor.execute("SELECT * FROM headers").fetchall()
        print(rows)

        print("Transactions")
        rows = cursor.execute("SELECT * FROM transactions").fetchall()
        print(rows)

    def getBalance():
        # Get balance of a given address

        address = input("\nEnter wallet address: ")

        connection = sqlite3.connect("blockchain.db")
        cursor = connection.cursor()
        rows = cursor.execute("SELECT (SELECT COALESCE(SUM(value), 0) FROM transactions WHERE recipient = '" + address + "') - (SELECT COALESCE(SUM(value), 0) FROM transactions WHERE sender = '" + address + "')").fetchall()
        print(rows)
        connection.close()

