def create_matrix(key, plain_text):
    matrix = []

    for _row in range(key):
        matrix_row = []
        for _col in range(len(plain_text)):
            matrix_row = ["_"] * len(plain_text)
        matrix.append(matrix_row)
    # pprint(matrix)

    return matrix


def place_text_zigzag(matrix, text):
    row, col = 0, 0
    count = 0
    reverse = False
    while True:
        matrix[row][col] = text[count]

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

        if count == len(text):
            break

    return matrix
