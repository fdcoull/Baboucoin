from Crypto.PublicKey import RSA
from base64 import b64decode
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

class Wallet:
    def create():
        # Generate new key pair for wallet

        # Generate RSA key pair
        key = RSA.generate(1024)
        private_key = key.export_key()
        public_key = key.publickey().export_key()

        # Strip tags from keys
        private_stripped = Wallet.stripKeyTags(private_key)
        public_stripped = Wallet.stripKeyTags(public_key)

        # Output result to user
        print(private_stripped)
        print(public_stripped)

    def getAddress(private):
        # Get public key from input private key

        # Decode private key and import
        keyDecoded = b64decode(private)
        importedKey = RSA.import_key(keyDecoded)

        # Export public key and strip tags
        publicKey = Wallet.stripKeyTags(importedKey.publickey().export_key())

        return publicKey

    def stripKeyTags(key):
        # Strip tags from keys

        # Remove newlines
        keyStripped = key.replace(b'\n', b'')
        
        if b'-----BEGIN PUBLIC KEY-----' in keyStripped:
            # Replace public key tags
            keyStripped = keyStripped.replace(b'-----BEGIN PUBLIC KEY-----', b'')
            keyStripped = keyStripped.replace(b'-----END PUBLIC KEY-----', b'')
        elif b'-----BEGIN RSA PRIVATE KEY-----' in keyStripped:
            # Replace private key tags
            keyStripped = keyStripped.replace(b'-----BEGIN RSA PRIVATE KEY-----', b'')
            keyStripped = keyStripped.replace(b'-----END RSA PRIVATE KEY-----', b'')

        return keyStripped

    def sign(private, message):
        # Sign transaction using private key

        # Import key to create signer
        key = RSA.import_key(private)
        signer = PKCS1_v1_5.new(key)

        # Process transaction data
        data = message.encode()
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



