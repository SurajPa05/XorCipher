import secrets
import string 
import pyfiglet 

EASY_KEY_LEN = 8  #easy key length of 8
MEDIUM_KEY_LEN = 16  #medium key length of 16
HARD_KEY_LEN = 24  #hard key length of 24
key_lengths = {1: EASY_KEY_LEN, 2: MEDIUM_KEY_LEN, 3: HARD_KEY_LEN}  #key lengths for easy, medium and hard encryption
ALLOWED_CHARS = string.ascii_letters + string.digits + string.punctuation  #allowed characters for the key include (a-z A-Z 0-9 and special characters)


logo = pyfiglet.figlet_format("XOR CYPHER", font = "slant") 
print(logo) 
print("created by :  @Surajpa")
print("git hub    :  https://github.com/SurajPa05/XorCipher\n")

# Generates random key
def generate_key(key_len):
    return ''.join(secrets.choice(ALLOWED_CHARS) for _ in range(key_len))  #generates a random key of specified length using secrets.choice() function

# Encryption algorithm
def encrypter(text,key_len):
    key = generate_key(key_len)
    if  key and text:
        try:
            encrypted_bytes = ''.join(chr(ord(text[i]) ^ ord(key[i % len(key)])) for i in range(len(text)))  # XOR encryption converts the text to bytes and encrypts it using XOR operation with the key
            encrypted_hex = encrypted_bytes.encode().hex()  #converts the encrypted bytes to hex string
            return encrypted_hex, key  #returns the encrypted hex string and the key
        except Exception as e:  # Catch any unexpected errors
            print(f"Encryption went wrong: {str(e)}")
            return
    else:
        print("key or text is missing")
        return


# Decryption algorithm
def decrypter(encrypted_hex, key):
    try:
        encrpted_bytes = bytes.fromhex(encrypted_hex)  #decode the hex string to bytes
    except ValueError as e:
        print(f"Invalid hex input: {str(e)}")
        return
    if key and encrpted_bytes:
        try:
            decrypted_text = ''.join(chr(encrpted_bytes[i] ^ ord(key[i % len(key)])) for i in range(len(encrpted_bytes)))  #XOR decryption
            return decrypted_text  #returns the decrypted text
        except Exception as e:  # Catch any unexpected errors
            print(f"Decryption went wrong: {str(e)}")
            return None
    else:
        print("Key or Encrypted text is missing")
        return

# Main function to handle user input and call the appropriate functions
def Main():
    lines =[]
    print("choose an option : \n\t 1. Encrypt \n\t 2. Decrypt")
    try:
        ed_choice = int(input("choose an option from above : "))  #choose between encryption and decryption
    except ValueError:
        print("Invalid input, please enter a number.")
        return
    if(ed_choice == 1):
        print("Enter the text to be encrypted (Press Ctrl+D to finish):")
        while True:
            try:
                line = input()
            except EOFError:
                break
            lines.append(line)
        text = '\n'.join(lines)
        try:
            comp_choice = int(input("\nChoose an encryption type \n\t 1. Easy \n\t 2. Medium \n\t 3. Hard \n Enter your choice:  "))  # Choose encryption type
        except ValueError:  # Handle invalid input for encryption type
            print("Invalid input, please enter a number.")
            return
        if comp_choice in key_lengths:
                encrypted_hex, key = encrypter(text, key_lengths[comp_choice])
                if encrypted_hex and key:
                    print(f"Encrypted Text (Hex): {encrypted_hex}")
                    print(f"Encryption Key: {key}")
                else:
                    print("Invalid choice, please select a valid option between 1 and 3.")
    
    elif(ed_choice == 2):
        try:
            encrypted_text = str(input("Enter the encrypted text (Hex):\n "))
            key = str(input("Enter the key: "))
        except EOFError:
            print("Invalid input, please enter a valid string.")
            return
        decrypted_text = decrypter(encrypted_text, key)
        if decrypted_text:
            print(f"\nDecrypted Text: {decrypted_text}")
    else:
        print("Invalid choice, please select a valid option.")
    print("\n\n")


# Main loop to keep the program running
while(True):
    Main()
