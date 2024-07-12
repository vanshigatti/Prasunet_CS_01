# Function to encrypt plaintext using Caesar Cipher algorithm
def caesar_cipher_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            encrypted_text += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text 

# Function to decrypt encrypted text using Caesar Cipher algorithm
def caesar_cipher_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            decrypted_text += chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

plaintext = input("Enter the plaintext: ").upper() 
shift = int(input("Enter the shift value: ")) 
encryption = caesar_cipher_encrypt(plaintext, shift)
decryption = caesar_cipher_decrypt(encryption, shift)
print("Encrypted text:", encryption)
print("Decrypted text:", decryption)
