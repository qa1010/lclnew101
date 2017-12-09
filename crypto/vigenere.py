from helpers import alphabet_position, rotate_character

def encrypt(text, keyword):
    message = ""
    index = 0
    for char in text:
        if char.isalpha():
            rot = alphabet_position(keyword[index % len(keyword)])
            message += rotate_character(char, rot)
            index += 1
        else:
            message += char
    return message
