#Created by JFS Jan 16 2018
#Modified by Nima Bidari October 11 2018

plainText = input("What is your plaintext? ")
shift = int(input("What is your shift? "))

def caesar(plainText, shift): 

    cipherText = ""

    for ch in plainText:
        if ch.isalpha():
            stayInAlphabet = ord(ch) + shift 
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
        cipherText = ""
        cipherText += finalLetter

    print("Your ciphertext is: " + cipherText)

    return cipherText

caesar(plainText, shift)