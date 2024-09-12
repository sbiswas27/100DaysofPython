alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#start with writing individual functions for encryption and decryption - later once we understand the code and run to check them we can merge it to a single function
# def encrypt(original_text, shift_amount):
#     encoded_message=''
#     for letter in original_text:
#         original_position = alphabet.index(letter)
#         new_position = original_position + shift_amount
        
#         # Avoid index out of range error
#         new_position = new_position % len(alphabet)

#         encoded_letters = alphabet[new_position]
#         encoded_message +=encoded_letters
#     print(encoded_message)

# def decrypt(original_text,shift_amount):
#     decoded_message=""
#     for letter in original_text:
#         new_position = alphabet.index(letter) - shift_amount
#         new_position %= len(alphabet)
#         decoded_message +=alphabet[new_position]
#     print(f"Here is the decoded result: {decoded_message}")


def ceaser(original_text,shift_amount,encode_or_decode):
    output_message = ""
  
    if encode_or_decode=='decode':
      shift_amount *= -1
      
    for letter in original_text:
      
  # for letters/numbers/symbols not in the code, adding them as is to the output text message so that they are not lost
      
      if letter not in alphabet:
        output_text += letter
        
      else:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
        
    print(f"Here is the {encode_or_decode}d result: {output_message}")

# Giving the user option to run the code multiple times! 
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    should_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if should_continue=='no':
        should_continue=False

