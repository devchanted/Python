alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser(text,shift,direction):
    plain_text = ""
    if direction == "encode":
        for letter in text:
            position = alphabet.index(letter)
            new_position = position + shift
            plain_text += alphabet[new_position]
        print(f"The Encoded text is {plain_text}")
    elif direction == "decode":
        for letter in text:
            position = alphabet.index(letter)
            new_position = position - shift
            plain_text += alphabet[new_position]
        print(f"The Decoded text is {plain_text}")
    else:
        print("Invalid Entry")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

ceaser(text,shift,direction)