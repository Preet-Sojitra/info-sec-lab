import pprint
from utils import gen_matrix, print_matrix, fill_key

key = input("Enter key: ")
cipher_text = input("Enter Cipher Text: ")

alphabets = "abcdefghijklmnopqrstuvwxyz"

"""
    Decryption Logic:
    In the matrix, we need to traverse the row the of the every key character and in that row we need to find the index of the column where cipher text character and the character at that column matches.
    Then for that index of column we need to find the corresponding character from the first row. 
    This will be the decrypted character
"""


def intersection(matrix, key_char, cipher_text_char):
    row_idx = alphabets.index(key_char)
    col_index = ""

    for i in range(26):
        if matrix[row_idx][i] == cipher_text_char:
            col_index = i
            break

    intersection_char = matrix[0][col_index]

    return intersection_char


def decrypt(key, cipher_text):
    matrix = gen_matrix()
    print_matrix(matrix)

    key = fill_key(key, cipher_text)
    # print(key)

    plain_text = ""

    for i in range(len(key)):
        plain_text += intersection(matrix, key[i], cipher_text[i])

    return plain_text


plain_text = decrypt(key, cipher_text)
print("Plain Text is: ", plain_text)
