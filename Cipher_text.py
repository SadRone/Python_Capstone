alphabet = ['a', 'b', 'c' , 'd' ,'e', 'f' ,'g', 'h','i' ,'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

encode = input(''' 'type 'encode' to encrypt, type 'decode' to decrypt: \n ''').lower()
input_word = input('type in your words: ')
shift = int(input("Type how many shift in number: "))

def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text, shift_amount):
    output_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the decoded results: {output_text}")

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:

        if encode_or_decode =="decode":
            shift_amount *= -1


        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the decoded results: {output_text}")


decrypt(input_word, shift)
