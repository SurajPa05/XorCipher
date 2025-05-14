import secrets
import string 
import pyfiglet 


#encryption algorithm
def encrypter(text,key):
    Xored = ''
    for i in range (len(text)):
        Xored += chr(ord(text[i]) ^ ord(key[i%len(key)]))
    Encrypted = Xored.encode().hex()
    print("Key for Decryption : " + key)
    print("encrypted text :\n" + Encrypted)   


#decryption algorithm
def decrypter(encrypted_hex, key):
    xored_bytes = bytes.fromhex(encrypted_hex)  
    decrypted_text = ''
    for i in range(len(xored_bytes)):
        decrypted_text += chr(xored_bytes[i] ^ ord(key[i % len(key)]))
    print("Decrypted message:\n" + decrypted_text)



#generates random key
def Generate_Key(text,key_len):
    key = ''
    charset = string.ascii_letters + string.digits + string.punctuation
    for i in range(key_len):
        key += secrets.choice(charset)
    encrypter(text,key)


def Main():

    logo = pyfiglet.figlet_format("XOR CYPHER", font = "slant") 
    print(logo) 
    print("Choose an option\n\t 1.Encryption\n\t 2. decryption")
    op_choose = int(input("Choose an option : "))
    if(op_choose == 1):
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
    elif(op_choose == 2):
        encrypted_text = str(input("Enter the encrypted text : \n"))
        key = str(input("\nEnter the key : "))
        decrypter(encrypted_text,key)
    else:
        print("Wrong choice!")


Main()
