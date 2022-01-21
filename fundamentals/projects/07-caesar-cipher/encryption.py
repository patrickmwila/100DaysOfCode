alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(text, direction, number):
    end_text = ""
    for char in text:
        if direction == "encode":
            if char in alphabet:
                shift = alphabet.index(char) + number
                end_text += alphabet[shift]
            else:
                end_text += char

        elif direction == "decode":
            if char in alphabet:
                shift = alphabet.index(char) - number
                end_text += alphabet[shift]
            else:
                end_text += char

        else:
            print("An error occurred!")
            break
    print(f"The {direction}d text is: {end_text}")
