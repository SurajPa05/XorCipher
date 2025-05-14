import secrets
import string 
import pyfiglet 

EASY_KEY_LEN = 8
MEDIUM_KEY_LEN = 16
HARD_KEY_LEN = 24
ALLOWED_CHARS = string.ascii_letters + string.digits + string.punctuation

logo = pyfiglet.figlet_format("XOR CYPHER", font = "slant") 
print(logo) 


#generates random key
def Generate_Key(key_len):
    return ''.join(secrets.choice(ALLOWED_CHARS) for _ in range(key_len))

#encryption algorithm
def encrypter(text,key_len):
    key = Generate_Key(key_len)
    if(len(key) != 0 and len(text)!= 0):
        try:
            encrypted_bytes = ''.join(chr(ord(text[i]) ^ ord(key[i % len(key)])) for i in range(len(text)))
            encrypted_hex = encrypted_bytes.encode().hex()
            print("Key for Decryption : " + key + "\nencrypted text :\n" + encrypted_hex)
        except:
            print("Encryption went wrong !!")
    else:
        print("Key or Text is missing")


#decryption algorithm
def decrypter(encrypted_hex, key):
    try:
        encrpted_bytes = bytes.fromhex(encrypted_hex)  
    except:
        print("Failed to extract byte from hex !")
    if(len(key) != 0 and len(encrpted_bytes)!= 0):
        try:
            decrypted_text = ''.join(chr(encrpted_bytes[i] ^ ord(key[i % len(key)])) for i in range(len(encrpted_bytes)))
        except:
            print("Decryption went wrong !!")
        print("Decrypted message:\n" + decrypted_text)

def Main():
    contents =[]
    print("Choose an option\n\t 1.Encryption\n\t 2. decryption")
    try:
        ED_Choose = int(input("Choose an option : "))
    except:
        print("Invalid characters")
    if(ED_Choose == 1):
        print("Enter the text you want to encrypt press ctrl+D to stop entering")
        while True:
            try:
                line = input()
            except EOFError:
                break
            contents.append(line)
            text = '\n'.join(contents)
        Comp_Level = int(input("\nChoose an encryption type \n\t 1.easy \n\t 2.medium \n\t 3.hard \nChoose An option from above : "))
        if Comp_Level == 1:
            encrypter(text,8)
            print("option 1")
        elif Comp_Level == 2:
            encrypter(text,16)
        elif Comp_Level == 3:
            encrypter(text,24)
        else:
            print("Invalid Choice")
    elif(ED_Choose == 2):
        try:
            encrypted_text = str(input("Enter the encrypted text :"))
            key = str(input("Enter the key : "))
        except:
            print("invalid input")
        decrypter(encrypted_text,key)
    else:
        print("Wrong choice!")

while(True):
    Main()
