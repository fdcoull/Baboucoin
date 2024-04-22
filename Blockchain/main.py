import sqlite3
from contextlib import closing



class Blockchain:
    def initialise():
        # Create database connection
        connection = sqlite3.connect("blockchain.db")
        cursor = connection.cursor()

        # Create headers table
        cursor.execute("DROP TABLE IF EXISTS headers")
        cursor.execute("""CREATE TABLE headers (
            height INTEGER, 
            difficulty TEXT, 
            timestamp INTEGER, 
            nonce INTEGER, 
            PRIMARY KEY('height' AUTOINCREMENT)
        )""")
        
        # Create transactions table
        cursor.execute("DROP TABLE IF EXISTS transactions")
        cursor.execute("""CREATE TABLE transactions (
            height INTEGER, 
            timestamp INTEGER, 
            sender TEXT, 
            recipient TEXT, 
            value DECIMAL(6,3), 
            signature TEXT
        )""")

        # Create mempool table
        cursor.execute("DROP TABLE IF EXISTS mempool")
        cursor.execute("""CREATE TABLE mempool (
            timestamp INTEGER,
            sender TEXT,
            recipient TEXT,
            value DECIMAL(6,3),
            signature TEXT
        )""")

        # test addition
        cursor.execute("INSERT INTO headers (difficulty, timestamp, nonce) VALUES ('000F', 17, 1)")
        cursor.execute("INSERT INTO headers (difficulty, timestamp, nonce) VALUES ('000F', 18, 24)")

        cursor.execute("INSERT INTO transactions (height, timestamp, sender, recipient, value, signature) VALUES (1, 23, 'a', 'b', 50.123, 'jhsdhghg')")

        cursor.execute("INSERT INTO mempool (timestamp, sender, recipient, value, signature) VALUES (23, 'a', 'b', 50.123, 'jhsdhghg')")

        rows = cursor.execute("SELECT * FROM headers").fetchall()
        print(rows)

        rows = cursor.execute("SELECT * FROM transactions").fetchall()
        print(rows)

        rows = cursor.execute("SELECT * FROM mempool").fetchall()
        print(rows)

        connection.close()
