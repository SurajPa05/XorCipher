import random
import secrets
import string 

#encryption algorithm
def encrypter(text,key):
    Xored = ''
    for i in range (len(text)):
        Xored += chr(ord(text[i]) ^ ord(key[i%len(key)]))
    Encrypted = Xored.encode().hex()
    print(Encrypted)   

#decryption algorithm
def decrypter(Encrypted_text,key):
    bytetext = Encrypted_text.decode().hex()
    print(bytetext)

#generates random key
def Generate_Key(text,key_len):
    key = ''
    charset = string.ascii_letters + string.digits + string.punctuation
    for i in range(key_len):
        key += secrets.choice(charset)
    encrypter(text,key)


def Main():
    text = ""
    text = input("Enter the text you want to encrypt\n")
    comp = int(input("Choose the encryption method :"))
    if comp == 1:
        Generate_Key(text,8)
    elif comp == 2:
        Generate_Key(text,16)
    elif comp == 3:
        Generate_Key(text,24)
    else:
        print("Wrong Choice !")

Main()
