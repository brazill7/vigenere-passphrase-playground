from print_color import ColorOutputItem, print_c, Color
from custom_input import get_user_input

DEBUG = False

def generate_keyed_alphabet(key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.upper()
    
    unique_key = "".join(sorted(set(key), key=key.index)) #remove duplicate chars
    
    for char in unique_key:
        alphabet = alphabet.replace(char, "")

    result = unique_key + alphabet

    if DEBUG: 
        print_c([ColorOutputItem(Color.DEBUG, 'generate_keyed_alphabet() : => '), ColorOutputItem(Color.IMPORTANT, f"{result}\n")])

    return result


def generate_vigenere_table(keyed_alphabet):
    alphabet = keyed_alphabet
    table = []
    for i in range(26):
        table.append(alphabet[i:] + alphabet[:i])

    if DEBUG: print_c([ColorOutputItem(Color.DEBUG, 'generate_vigenere_table() : => '), ColorOutputItem(Color.IMPORTANT, f"{table}\n")])

    return table


def repeat_to_length(s, desired_length):
    return (s * (desired_length // len(s) + 1))[:desired_length]

def encrypt_vigenere(table, plaintext, passphrase):
    plaintext = plaintext.upper()
    passphrase = repeat_to_length(passphrase.upper(), len(plaintext))
    ciphertext = ""
    
    for p, k in zip(plaintext, passphrase):
        if p.isalpha():
            row = ord(k) - ord('A')
            col = ord(p) - ord('A')
            ciphertext += table[row][col]
        else:
            ciphertext += p  # Non-Alphabetic

    return ciphertext

def decrypt_vigenere(table, ciphertext, passphrase):
    ciphertext = ciphertext.upper()
    passphrase = repeat_to_length(passphrase.upper(), len(ciphertext))
    plaintext = ""
    
    for c, k in zip(ciphertext, passphrase):
        if c.isalpha():
            row = ord(k) - ord('A')
            col = table[row].index(c)
            plaintext += chr(col + ord('A'))
        else:
            plaintext += c  # Non-Alphabetic

    return plaintext


def main():
    decision = get_user_input('Would you like to use a keyed alphabet, as opposed to the normal alphabet?', '[yes] [literally-anything-else-is-no]', extra_newline=True)

    # Decide if we are using a keyed alphabet, or not
    if decision.lower().strip() == "yes":
        key = get_user_input('Enter a key for the keyed alphabet', extra_newline=True).upper()
        alphabet = generate_keyed_alphabet(key)
    else:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #Generate Vigenere Table
    vigenere_table = generate_vigenere_table(alphabet)

    passphrase = get_user_input('Enter a passphrase for the encryption/decryption', extra_newline=True)

    plaintext = get_user_input('Enter plaintext to be encrypted', extra_newline=True).replace(' ', '')
    ciphertext = encrypt_vigenere(vigenere_table, plaintext, passphrase)
    decrypted_text = decrypt_vigenere(vigenere_table, ciphertext, passphrase)

    print("Ciphertext: " + ciphertext)
    print("Decrypted Text: " + decrypted_text)

    

if __name__ == '__main__':
    main()