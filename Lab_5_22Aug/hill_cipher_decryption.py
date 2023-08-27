from pprint import pprint
from utils import key_matrix, gen_text_vector, multiplication

# ! This is only for 2x2 and 3x3 key matrix

key = input("Enter the key: ").lower()
cipher_text = input("Enter the cipher text: ").lower()

alphabets = "abcdefghijklmnopqrstuvwxyz"


# first we need to make the dimension of the key matrix nxn
def filler(key: str) -> str:
    if len(key) != 4 or len(key) != 9:
        count = 0
        while True:
            key += alphabets[count]
            count += 1
            if len(key) == 4 or len(key) == 9:
                break

    return key


def multiplicative_inverse(num: int) -> int:
    for i in range(26):
        if (num * i) % 26 == 1:
            num = i
            break
    return num


def inv_2x2(matrix: list[list[int]]) -> list[list[int]]:
    det_matrix = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    adj_matrix = [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]

    if det_matrix < 0:
        det_matrix = 26 - ((-det_matrix) % 26)
    else:
        det_matrix = det_matrix % 26

    # find the multiplicative inverse of det_matrix
    inverse = multiplicative_inverse(det_matrix)
    # print(inverse)

    inv_key_matrix = []
    # Now multiply the adj_matrix with inverse
    for i in range(len(adj_matrix)):
        row = []
        for j in range(len(adj_matrix[0])):
            row.append((adj_matrix[i][j] * inverse) % 26)
        inv_key_matrix.append(row)

    # print(inv_key_matrix)

    return inv_key_matrix


def inv_3x3(matrix: list[list[int]]) -> list[list[int]]:
    det_matrix = (
        (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]))
        - (matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]))
        + (matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))
    )

    if det_matrix < 0:
        det_matrix = 26 - ((-det_matrix) % 26)
    else:
        det_matrix = det_matrix % 26

    inverse = multiplicative_inverse(det_matrix)
    # print(inverse)

    adj_matrix = [
        [
            (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]),
            -(matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]),
            (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]),
        ],
        [
            -(matrix[0][1] * matrix[2][2] - matrix[0][2] * matrix[2][1]),
            (matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]),
            -(matrix[0][0] * matrix[2][1] - matrix[0][1] * matrix[2][0]),
        ],
        [
            (matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]),
            -(matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0]),
            (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]),
        ],
    ]

    # take the transpose of adj_matrix
    for i in range(len(adj_matrix)):
        for j in range(i, len(adj_matrix[0])):
            adj_matrix[i][j], adj_matrix[j][i] = adj_matrix[j][i], adj_matrix[i][j]

    inv_key_matrix = []

    for i in range(len(adj_matrix)):
        row = []
        for j in range(len(adj_matrix[0])):
            row.append((adj_matrix[i][j] * inverse) % 26)
        inv_key_matrix.append(row)

    return inv_key_matrix


def decrypt(key, cipher_text) -> str:
    # remove spaces from the cipher text
    cipher_text = cipher_text.replace(" ", "")

    if len(key) == 4 or len(key) == 9:
        pass
    else:
        key = filler(key)

    matrix = key_matrix(key)
    # pprint(matrix)

    inv_key_matrix = []
    # Now find inverse of matrix
    if len(matrix) == 2:
        inv_key_matrix = inv_2x2(matrix)
    elif len(matrix) == 3:
        inv_key_matrix = inv_3x3(matrix)

    # print(inv_key_matrix)

    cipher_text_vector = gen_text_vector(cipher_text, len(inv_key_matrix))
    # print(cipher_text_vector)

    final_result = multiplication(inv_key_matrix, cipher_text_vector)
    print(final_result)

    # convert the final result into plain text
    plain_text = ""
    for pair in final_result:
        for char in pair:
            plain_text += alphabets[char]

    # print(cipher_text)
    return plain_text


plain_text = decrypt(key, cipher_text)
print("Plain Text: ", plain_text)
