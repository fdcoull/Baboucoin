import rsa
import os

class Wallet():
    def create(self):
        KEY_LENGTH = 1024
        publicKey, privateKey = rsa.newkeys(KEY_LENGTH)

        #Get from root class
        menuCursor = "=> "

        pathExistsCheck = True

        while(pathExistsCheck):
            print("Input name of wallet profile (Your keys will be stored here):")
            userInput = input(menuCursor)
            pathExists = os.path.isdir('user/keys/' + userInput)

            if pathExists == False:
                os.mkdir('user/keys/' + userInput)
                print("Wallet profile created")

                with open('user/keys/' + userInput + '/public.pem', 'wb') as p:
                    p.write(publicKey.save_pkcs1('PEM'))
                with open('user/keys/' + userInput + '/private.pem', 'wb') as p:
                    p.write(privateKey.save_pkcs1('PEM'))

                pathExistsCheck = False
            else:
                print("Profile name already exists, please enter another")
