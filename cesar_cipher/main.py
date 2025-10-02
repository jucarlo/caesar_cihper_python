from encrypt import encrypt
from decrypt import decrypt

def caesar(original_text, shift_amount, action):
    result = ""
    if action == "1":
        print("encrypting...")
        result = encrypt(original_text, shift_amount)
    else:
        print("decrypting...")
        result = decrypt(original_text, shift_amount)
    print(f"Here is your result:\n {result}")

active = True
while active:
    direction = input("Type '1' to encrypt, type '2' to decrypt:\n")

    if direction not in ("1", "2"):
        print("DIRECTION: " + direction)
        continue

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart = input("Do you want to go again [y/n]\n").lower()
    if restart == "n":
        active = False
        print("Goodbye!")