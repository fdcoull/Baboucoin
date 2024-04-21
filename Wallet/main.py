import rsa

class Wallet:
    def create():
        (pubKey, privKey) = rsa.newkeys(1024)
        with open('pubkey.pem', 'wb') as f:
            f.write(pubKey.save_pkcs1('PEM'))

        with open('privkey.pem', 'wb') as f:
            f.write(privKey.save_pkcs1('PEM'))

    def read():
        with open('pubkey.pem', 'rb') as f:
            pubKey = rsa.PublicKey.load_pkcs1(f.read())

        with open('privkey.pem', 'rb') as f:
            privKey = rsa.PrivateKey.load_pkcs1(f.read())

        return pubKey, privKey

    def sign_sha1(msg, key):
        return rsa.sign(msg.encode('ascii'), key, 'SHA-1')

    def verify_sha1(msg, signature, key):
        try:
            return rsa.verify(msg.encode('ascii'), signature, key) == 'SHA-1'
        except:
            return False

    create()
    pubKey, privKey = read()

    message = "abc" + "abc" + str(20)

    signature = sign_sha1(message, privKey)

    if verify_sha1(message, signature, pubKey):
        print('Signature verified')
    else:
        print("Could not verify")