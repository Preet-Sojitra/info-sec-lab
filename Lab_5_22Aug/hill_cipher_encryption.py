from pprint import pprint
from utils import key_matrix, gen_text_vector as plain_text_vector, multiplication

# ! This program is only for 2x2 and 3x3 key matrix

key = (input("Enter the key: ")).lower()
plain_text = (input("Enter the plain text: ")).lower()

alphabets = "abcdefghijklmnopqrstuvwxyz"


def filler(key: str, plain_text: str) -> tuple[str, str]:
    # Filler for key
    if len(key) != 4 or len(key) != 9:
        count = 0
        while True:
            key += alphabets[count]
            count += 1
            if len(key) == 4 or len(key) == 9:
                break

    # Filler for plain text
    if len(plain_text) % 2 != 0 or len(plain_text) % 3 != 0:
        while True:
            plain_text += "x"

            if len(plain_text) % 2 == 0 or len(plain_text) % 3 == 0:
                break

    return key, plain_text


def encrypt(key: str, plain_text: str) -> str:
    # remove all the spaces from the plain text
    plain_text = plain_text.replace(" ", "")

    # use filler function
    if len(key) == 4 or len(key) == 9:
        pass
    else:
        key, plain_text = filler(key, plain_text)

    # print(key, plain_text)

    matrix = key_matrix(key)
    text_vector = plain_text_vector(plain_text, len(matrix))

    final_result = multiplication(matrix, text_vector)
    # pprint(final_result)

    # convert the final result into cipher text
    cipher_text = ""
    for pair in final_result:
        for char in pair:
            cipher_text += alphabets[char]

    # print(cipher_text)
    return cipher_text


cipher_text = encrypt(key, plain_text)
print("Encrypted Text: ", cipher_text)
