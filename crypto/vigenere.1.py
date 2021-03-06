def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    position = alphabet.index(letter.lower())
    return position

def rotate_character(char, rot):
    if not char.isalpha():
        return char
    else:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        position = alphabet_position(char)
        num_to_move = (position + rot) % 26
        if char.isupper():
            new_letter = alphabet[num_to_move].upper()
        else:
            new_letter = alphabet[num_to_move]
        return new_letter

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
