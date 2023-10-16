K = int(input())
message = input()
encrypted_message = ""
for char in message:
    if char.isalpha():
        ascii_offset = ord('a') if char.islower() else ord('A')
        encrypted_char = chr((ord(char) - ascii_offset + K) % 26 + ascii_offset)
        encrypted_message += encrypted_char
    else:
        encrypted_message += char
print(encrypted_message)
