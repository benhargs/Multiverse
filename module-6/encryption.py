
numb = int(input("Select a number between 1 & 25: "))
message = str(input("Input your message that you want to encrypt: "))

def shift(message, numb):
    encoded_message = []
    for char in message:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')

            encoded_char = chr((ord(char) - shift_base + numb) % 26 + shift_base)

            encoded_message.append(encoded_char)
        else:
            encoded_message.append(char)
    return ''.join(encoded_message)

encrypted_message = shift(message, numb)

print("Encrypted Message: ", encrypted_message)