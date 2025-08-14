# Task 1 - Caesar Cipher

def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Example usage
message = input("Enter message: ")
shift_val = int(input("Enter shift value: "))

encrypted = caesar_cipher(message, shift_val, mode="encrypt")
decrypted = caesar_cipher(encrypted, shift_val, mode="decrypt")

print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
