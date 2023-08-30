from pprint import pprint
from utils import create_matrix, place_text_zigzag

key = int(input("Enter the key: "))
plain_text = input("Enter the plain text: ")


def encrypt(key, plain_text):
    # We need to create a matrix of size of key * length of plain text
    matrix = create_matrix(key, plain_text)

    # now we need to fill the matrix diagonally with the plain text
    # we need to fill the matrix in a zig zag manner
    matrix = place_text_zigzag(matrix, plain_text)
    print(matrix)

    # traverse the matrix horizontally and add it to cipher text
    cipher_text = ""

    for row in range(len(matrix)):
        for col in matrix[row]:
            if col != "_":
                cipher_text += col
    # print(cipher_text)

    return cipher_text


cipher_text = encrypt(key, plain_text)
print("Cipher text is: ", cipher_text)
