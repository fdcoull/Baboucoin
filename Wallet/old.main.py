import rsa
import sqlite3

class Wallet:
    def create():
        print("TEST")
        (pubkey, privkey) = rsa.newkeys(256, poolsize=8)

        print("Public: " + str(pubkey))
        print("Private: " + str(privkey))

    def save():
        (pubkey, privkey) = rsa.newkeys(512, poolsize=8)
        with open('pubkey.pem', 'wb') as f:
            f.write(pubkey.save_pkcs1('PEM'))

        with open('privkey.pem', 'wb') as f:
            f.write(privkey.save_pkcs1('PEM'))

        print("Public: " + str(pubkey))
        print("Private: " + str(privkey))

    # Copy of above for testing
    def save2():
        (pubkey, privkey) = rsa.newkeys(512, poolsize=8)
        with open('pubkey2.pem', 'wb') as f:
            f.write(pubkey.save_pkcs1('PEM'))

        with open('privkey2.pem', 'wb') as f:
            f.write(privkey.save_pkcs1('PEM'))

        print("Public: " + str(pubkey))
        print("Private: " + str(privkey))

    def load():
        with open('privkey.pem', mode='rb') as f:
            keydata = f.read()
        privkey = rsa.PrivateKey.load_pkcs1(keydata)

        with open('pubkey.pem', mode='rb') as f:
            keydata = f.read()
        pubkey = rsa.PublicKey.load_pkcs1(keydata)
        return pubkey, privkey
    
    # Copy of above for testing
    def load2():
        with open('privkey2.pem', mode='rb') as f:
            keydata = f.read()
        privkey = rsa.PrivateKey.load_pkcs1(keydata)

        with open('pubkey2.pem', mode='rb') as f:
            keydata = f.read()
        pubkey = rsa.PublicKey.load_pkcs1(keydata)
        return pubkey, privkey

    def sign(privkey, transaction):
        input = transaction.encode()
        signature = rsa.sign(input, privkey, 'SHA-1')
        return signature

    def verify(pubkey, signature, transaction):
        input = transaction.encode()
        rsa.verify(input, signature, pubkey)

    def send(privkey, recipient, value):

        
        connection = sqlite3.connect("blockchain.db")
        cursor = connection.cursor()

        cursor.execute("INSERT INTO transactions (height, sender, recipient, value, signature) VALUES (" + str(1) + ", NULL, '" + str("8231075866143642093823703637821689530337535818906173134516500457285787727786471866729831589214323132616875859186915672879867764390257674825430419460414781") + "', " + str(10) + ", NULL)")

        connection.commit()
        connection.close()
