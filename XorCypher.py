import secrets
import string 
import pyfiglet 

EASY_KEY_LEN = 8           #easy key length of 8
MEDIUM_KEY_LEN = 16        #medium key length of 16
HARD_KEY_LEN = 24          #hard key length of 24
ALLOWED_CHARS = string.ascii_letters + string.digits + string.punctuation   #allowed characters for the key include (a-z A-Z 0-9 and special characters)

logo = pyfiglet.figlet_format("XOR CYPHER", font = "slant") 
print(logo) 


#generates random key
def Generate_Key(key_len):
    return ''.join(secrets.choice(ALLOWED_CHARS) for _ in range(key_len)) #generates a random key of specified length using secrets.choice() function

#encryption algorithm
def encrypter(text,key_len):
    key = Generate_Key(key_len)
    if not key or not text:
        try:
            encrypted_bytes = ''.join(chr(ord(text[i]) ^ ord(key[i % len(key)])) for i in range(len(text))) # XOR encryption converts the text to bytes and encrypts it using XOR operation with the key
            encrypted_hex = encrypted_bytes.encode().hex() #converts the encrypted bytes to hex string
            print("Encrypted message:\n" + encrypted_hex) 
            print("Key: " + key)
        except:
            print("Encryption went wrong !!")
            return
    else:
        print("Key or Text is missing")
        return


#decryption algorithm

def decrypter(encrypted_hex, key):
    try:
        encrpted_bytes = bytes.fromhex(encrypted_hex)  #decode the hex string to bytes
    except ValueError as e:
        print(f"Invalid hex input: {str(e)}")
        return
    if not key or not encrpted_bytes:
        try:
            decrypted_text = ''.join(chr(encrpted_bytes[i] ^ ord(key[i % len(key)])) for i in range(len(encrpted_bytes)))  # XOR decryption
            print("Decrypted message:\n" + decrypted_text)
        except:
            print("Decryption went wrong !!")
    else:
        print("Key or Encrypted text is missing")
        return

# Main function to handle user input and call the appropriate functions
def Main():
    contents =[]
    print("choose an option : \n\t 1. Encrypt \n\t 2. Decrypt")
    try:
        ED_Choose = int(input("choose an option from above : ")) #choose between encryption and decryption
    except ValueError:
        print("Invalid input, please enter a number.")
        return
    if(ED_Choose == 1):
        print("Enter the text to be encrypted (Press Ctrl+D to finish):")
        while True:
            try:
                line = input()
            except EOFError:
                break
            contents.append(line)
            text = '\n'.join(contents)
        Comp_Level = int(input("\nChoose an encryption type \n\t 1. Easy \n\t 2. Medium \n\t 3. Hard \n Enter your choice:  ")) # choose between easy, medium and hard encryption
        if Comp_Level == 1:
            encrypter(text,8)
        elif Comp_Level == 2:
            encrypter(text,16)
        elif Comp_Level == 3:
            encrypter(text,24)
        else:
            print("Invalid choice, please select a valid options between 1 and 3.")
    elif(ED_Choose == 2):
        try:
            encrypted_text = str(input("Enter the encrypted text :\n "))
            key = str(input("Enter the key : "))
        except EOFError:
            print("Invalid input, please enter a valid string.")
            return
        decrypter(encrypted_text,key)
    else:
        print("Invalid choice, please select a valid option.")
    print("\n\n")

# Main loop to keep the program running
while(True):
    Main()
