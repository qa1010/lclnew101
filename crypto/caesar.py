from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    message = ""
    for char in text:
        message += rotate_character(char, rot)
    return message
