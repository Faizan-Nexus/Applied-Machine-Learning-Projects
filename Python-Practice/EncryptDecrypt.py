import random
import string

# chars = string.ascii_letters + string.digits + string.digits + string.punctuation
chars = string.printable
chars =  list(chars)

keys = chars.copy()
random.shuffle(keys)


text = input("Please enter the text to encrypt:")
cipher = ""

for letter in text:
    index = chars.index(letter)
    cipher += keys[index]
    
print(f"Your Encrypted Text: {cipher}")

encr = input("Enter the text to Decrypt: ")

word =""

for letter in encr:
    index = keys.index(letter)
    word += chars[index]
    
print(f"Your Decrypted Text: {word}")