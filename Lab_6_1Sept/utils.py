def gen_matrix():
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    matrix = []
    count = 0
    for _ in range(26):
        row = []
        for j in range(26):
            row.append(alphabets[(j + count) % 26])
        matrix.append(row)
        count = count + 1
    return matrix


# Just for printing matrix in pretty way
def print_matrix(matrix):
    print("\n".join([" ".join([str(cell) for cell in row]) for row in matrix]))


def fill_key(key, text):
    new_key = key
    for i in range(len(key), len(text)):
        new_key += key[i % len(key)]

    return new_key
