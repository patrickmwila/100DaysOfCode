import art
import encryption

print(art.logo)

run_again = True
while run_again:
    direction = input("Type 'encode' to encrypt or type 'decode' to decrypt\n")
    text = input("Type your message\n")
    shift_value = int(input("Enter the shift number\n"))

    shift_value %= 26

    encryption.caesar(direction=direction, text=text, number=shift_value)

    print("Type 'yes' if you want to go again or any key to quit")
    exe = input().lower()

    if exe == "yes":
        continue
    else:
        run_again = False
        print("Goodbye")
