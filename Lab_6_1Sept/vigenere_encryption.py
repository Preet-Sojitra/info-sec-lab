import pprint
from utils import gen_matrix, print_matrix, fill_key

key = input("Enter key: ")
plain_text = input("Enter Plain Text: ")

alphabets = "abcdefghijklmnopqrstuvwxyz"


def intersection(matrix, key_char, plain_text_char):
    row_idx = alphabets.index(plain_text_char)
    col_idx = alphabets.index(key_char)
    # print(plain_text_char, ": ", row_idx, key_char, ": ", col_idx)

    intersection_char = matrix[row_idx][col_idx]

    return intersection_char


def encrypt(key, plain_text):
    matrix = gen_matrix()
    print_matrix(matrix)

    key = fill_key(key, plain_text)
    # print(key)

    cipher_text = ""

    for i in range(len(key)):
        cipher_text += intersection(matrix, key[i], plain_text[i])

    return cipher_text


cipher_text = encrypt(key, plain_text)
print("Cipher Text is: ", cipher_text)
