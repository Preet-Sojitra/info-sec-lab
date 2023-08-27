def key_matrix(key: str) -> list[list[int]]:
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    matrix = []

    for i in range(len(key)):
        matrix.append(alphabets.index(key[i]))

    key_matrix = []
    # Split the key matrix in nxn matrix
    if len(matrix) == 4:
        for i in range(0, len(matrix), 2):
            key_matrix.append(matrix[i : i + 2])

    elif len(matrix) == 9:
        for i in range(0, len(matrix), 3):
            key_matrix.append(matrix[i : i + 3])

    elif len(matrix) == 16:
        for i in range(0, len(matrix), 4):
            key_matrix.append(matrix[i : i + 4])

    # print("Key Matrix: ")
    # print(key_matrix)

    return key_matrix


def gen_text_vector(text: str, matrix_len: int) -> list[list[int]]:
    alphabets = "abcdefghijklmnopqrstuvwxyz"

    # Split the plain text in diagraph if length of key matrix is 2 and triagraph if length of key matrix is 3

    # print("Plain Text: ", plain_text)

    diagraph = []
    if matrix_len == 2:
        for i in range(0, len(text), 2):
            diagraph.append(text[i : i + 2])

        # check if last diagraph is single character then add x at the end
        # if len(diagraph[-1]) == 1:
        #     diagraph[-1] += "x"

    elif matrix_len == 3:
        for i in range(0, len(text), 3):
            diagraph.append(text[i : i + 3])

        # check if last diagraph is single character then add x at the end
        # if len(diagraph[-1]) == 2:
        #     diagraph[-1] += "x"

    # print("Diagraph: ")
    # print(diagraph)

    text_vector = []

    for pair in diagraph:
        indices = []
        for char in pair:
            indices.append(alphabets.index(char))
        text_vector.append(indices)

    # print("Plain Text Vector: ")
    # print(plain_text_vector)

    return text_vector


def multiplication(
    key_matrix: list[list[int]], text_vector: list[list[int]]
) -> list[list[int]]:
    # multiply the key matrix for each list in plain text vector
    final_result = []
    for i in range(len(text_vector)):
        result = []
        # print("Plain Text Vector: ", i)
        # print(plain_text_vector[i])
        for j in range(len(text_vector[i])):
            # Now we have access to single 1D list in plain text vector : [18, 7]
            # and we have 2D key matrix : [[7, 8], [11, 11]]
            # multiply the key matrix with plain text vector
            sum = 0
            for k in range(len(key_matrix)):
                sum += key_matrix[j][k] * text_vector[i][k]

            result.append(sum % 26)

        final_result.append(result)

    # pprint(final_result)
    return final_result
