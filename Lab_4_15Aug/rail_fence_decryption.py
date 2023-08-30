from pprint import pprint
from utils import create_matrix, place_text_zigzag as identify_text_position

key = int(input("Enter the key: "))
cipher_text = input("Enter the cipher text: ")


def traverse_horizontally(matrix, cipher_text):
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "*":
                matrix[row][col] = cipher_text[count]
                count += 1

    return matrix


def traverse_diagonally(matrix, cipher_text):
    row, col = 0, 0
    count = 0
    reverse = False
    plain_text = ""

    while True:
        plain_text += matrix[row][col]
        col += 1
        count += 1

        if reverse == False:
            row += 1
        elif reverse == True:
            row -= 1

        if row == len(matrix):
            row -= 2
            reverse = True
        if row == 0:
            reverse = False

        if count == len(cipher_text):
            break

    return plain_text


def decrypt(key, cipher_text):
    # We need to create a matrix of size of key * length of cipher text
    matrix = create_matrix(key, cipher_text)

    # now we need to fill the matrix in zig zag manner with "*" to identify where to put the cipher text
    matrix = identify_text_position(matrix, "*" * len(cipher_text))
    # pprint(matrix)

    # now we have identified where we need to put the cipher text. So we will traverse the matrix horizontally and put the cipher text one by one where "*" occurs in matrix
    matrix = traverse_horizontally(matrix, cipher_text)
    print(matrix)

    # Now we will traverse the matrix diagonally to obtain the plain text
    plain_text = traverse_diagonally(matrix, cipher_text)
    # print(plain_text)

    return plain_text


plain_text = decrypt(key, cipher_text)
print("Plain text is: ", plain_text)
