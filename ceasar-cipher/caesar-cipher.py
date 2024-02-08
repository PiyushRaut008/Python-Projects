alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

# --------Long Code--------

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")
#
#
# def decrypt(cipher_text, shift_amount):
#     cipher_texta = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         cipher_texta += alphabet[new_position]
#     print(f"The decoded text is {cipher_texta}")
#
# if direction == "encrypt":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decrypt":
#     decrypt(cipher_text=text, shift_amount=shift)


# --------Short code-------
# def cipher(start_text, shift_amount, cipher_direction):
#     cipher_text = ""
#     for letter in start_text:
#         position = alphabet.index(letter)
#         if cipher_direction == "encode":
#             new_position = position + shift_amount
#             cipher_text += alphabet[new_position]
#         elif cipher_direction == "decode":
#             new_position = position - shift_amount
#             cipher_text += alphabet[new_position]
#     if cipher_direction == "encode":
#         print(f"The encoded text is {cipher_text}")
#     elif cipher_direction == "decode":
#         print(f"The decoded text is {cipher_text}")
#
# cipher(start_text=text, shift_amount=shift, cipher_direction=direction)


# ----------more method-------
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
      shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {direction}d result: {end_text}")

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = False
    print("Goodbye")


