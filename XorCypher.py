import secrets
import string 
import pyfiglet 


#encryption algorithm
def encrypter(text,key):
    Xored = ''
    for i in range (len(text)):
        Xored += chr(ord(text[i]) ^ ord(key[i%len(key)]))
    Encrypted = Xored.encode().hex()
    print(Encrypted)   

#decryption algorithm
def decrypter():
    print("decryptes the text")

#generates random key
def Generate_Key(text,key_len):
    key = ''
    charset = string.ascii_letters + string.digits + string.punctuation
    for i in range(key_len):
        key += secrets.choice(charset)
    encrypter(text,key)


def Main():

    logo = pyfiglet.figlet_format("XOR CYPHER", font = "slant"   ) 
    print(logo) 
    text = input("Enter the text you want to encrypt \n")
    comp = int(input("\nChoose an encryption type \n\t 1.easy \n\t 2.medium \n\t 3.hard \nChoose An option from above : "))
    
    if comp == 1:
        Generate_Key(text,8)
        print("option 1")
    elif comp == 2:
        Generate_Key(text,16)
    elif comp == 3:
        Generate_Key(text,24)
    else:
        print("Wrong Choice !")

Main()
