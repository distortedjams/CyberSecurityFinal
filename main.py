#Import file where we are going to store our funcitons
from functions import *


print("Welcome to the main center of communication")

while True:

    fInput = int(input('Please select a process 1: Encryption, 2: Decryption'))

    if fInput == 1:

        #This is where the encryption portion goes

        sInput = int(input('Please select a encryption method 1.AES? 2. DES 3. 3DES'))

        if sInput == 1:

                aes_encrypt()

        elif sInput == 2:

                des_encrypt()

        elif sInput == 3:

                des3_encrypt()

        else:

            print("ERROR: Incorrect input please try again")

    elif fInput == 2:

        #This is where the decryption portion goes

        sInput = int(input('Please select a decryption method 1.AES? 2. DES 3. 3DES'))

        if sInput == 1:

            aes_decrypt()

        elif sInput == 2:

            des_decrypt()

        elif sInput == 3:

            des3_decrypt()

        else:

            print("ERROR: Incorrect input please try again")

    else:

        #User inputted a weird input make them do it again

        print("ERROR: Incorrect input please try again")
