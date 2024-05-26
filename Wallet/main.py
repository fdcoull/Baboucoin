from Crypto.PublicKey import RSA
from base64 import b64decode
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

class Wallet:
    def save():
        key = RSA.generate(1024)
        private_key = key.export_key()
        print(private_key)
        with open("privkey.pem", "wb") as f:
            f.write(private_key)
        
        public_key = key.publickey().export_key()
        with open("pubkey.pem", "wb") as f:
            f.write(public_key)

    def create():
        # New method of saving - outputs to terminal and doesnt save
        # Strips tags as output

        key = RSA.generate(1024)
        private_key = key.export_key()

        private_stripped = private_key.replace(b'-----BEGIN RSA PRIVATE KEY-----', b'')
        private_stripped = private_stripped.replace(b'\n', b'')
        private_stripped = private_stripped.replace(b'-----END RSA PRIVATE KEY-----', b'')

        public_key = key.publickey().export_key()

        public_stripped = public_key.replace(b'-----BEGIN PUBLIC KEY-----', b'')
        public_stripped = public_stripped.replace(b'\n', b'')
        public_stripped = public_stripped.replace(b'-----END PUBLIC KEY-----', b'')

        print(private_stripped)
        print(public_stripped)

    def getAddress():
        # Get public key from input private key

        print("Input private key:")

        key = input().encode()

        keyDecoded = b64decode(key)

        importedKey = RSA.import_key(keyDecoded)

        public_stripped = importedKey.publickey().export_key().replace(b'-----BEGIN PUBLIC KEY-----', b'')
        public_stripped = public_stripped.replace(b'\n', b'')
        public_stripped = public_stripped.replace(b'-----END PUBLIC KEY-----', b'')

        print(public_stripped)


    def loadFile():
        encoded_key = open("privkey.pem", "rb").read()
        key = RSA.import_key(encoded_key)

        print(key.export_key())
        print(key.public_key().export_key())

    def load():
        key = b'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCoQwutD8RfhaRVHpitV9FpJBvaWJC5zu6TzuhV9vddu1V447sVSVUYUe/WNBHktxD7DzVsn1OXjaoofiv0Bu4171QNDtQZYtJ0Q21SqRBToSn4TO4H6TAHUMw+AtZH5s15uqHuaV5eQTOJSRy4CUmvlTDN0pwbrKXEKWZ0/BWo4QIDAQAB'
        
        keyDecoded = b64decode(key)
        importedKey = RSA.import_key(keyDecoded)

        print(importedKey.export_key())

        return key

    def sign():
        encoded_key = open("privkey.pem", "rb").read()
        key = RSA.import_key(encoded_key)

        signer = PKCS1_v1_5.new(key)

        data = b'test'

        digest = SHA256.new(data)

        return signer.sign(digest)
    
    def verify(signature):
        key = b'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCoQwutD8RfhaRVHpitV9FpJBvaWJC5zu6TzuhV9vddu1V447sVSVUYUe/WNBHktxD7DzVsn1OXjaoofiv0Bu4171QNDtQZYtJ0Q21SqRBToSn4TO4H6TAHUMw+AtZH5s15uqHuaV5eQTOJSRy4CUmvlTDN0pwbrKXEKWZ0/BWo4QIDAQAB'
        
        signer = PKCS1_v1_5.new(RSA.import_key(b64decode(key)))

        data = b'tedst'

        digest = SHA256.new(data)

        #return signer.verify(digest, signature)
    
        if signer.verify(digest, signature):
            print("Valid")
        else:
            print("Invalid")

