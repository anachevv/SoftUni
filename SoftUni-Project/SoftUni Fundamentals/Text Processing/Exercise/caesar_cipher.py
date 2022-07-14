def encrypt_func(text):
    encrypted_text = ""

    for char in text:
        encrypted_text += chr(ord(char) + 3)

    return encrypted_text


text = input()

print(encrypt_func(text))
