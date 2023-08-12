from pprint import pprint  # for pretty printing

key = input("Enter key: ")
cipher_text = input("Enter text: ")

alphabets = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


# generate 5x5 key table matrix
def genKeyTable(key: str) -> list:
    key_letters = []  # this will contain all the letters of the key

    # append every letters of key to key_letters if not already present
    for i in key:
        if i not in key_letters:
            key_letters.append(i)

    # append rest of the alphabets to key_letters that are not present in key
    for i in range(len(alphabets)):
        if alphabets[i] not in key_letters:
            key_letters.append(alphabets[i])

    # 5x5 matrix
    key_table = []

    # split key_letters into 5x5 matrix
    for i in range(5):
        key_table.append(key_letters[i * 5 : i * 5 + 5])

    return key_table


# split plain text in pair of two
def genDiagraph(cipherText: str) -> list:
    diagraph = [cipherText[i : i + 2] for i in range(0, len(cipherText), 2)]
    return diagraph


# Main decryption algorithm
def decrypt() -> str:
    keyTable = genKeyTable(key)
    diagraph = genDiagraph(cipher_text)

    pprint(keyTable)
    print(diagraph)

    plain_text = []

    for word in diagraph:
        # this will contain location of each character of each word in the key table
        location = []

        # character is each word in the each pair of diagraph
        for character in word:
            # find where that character is present
            for row_index, row in enumerate(keyTable):
                # since index() method will raise ValueError if character is not found, therefore added try except block
                try:
                    idx_of_char = row.index(character)
                    location.append([row_index, idx_of_char])

                    # print(index, idx_of_char)
                    break
                except ValueError:
                    continue

        # pprint(location)
        # print(location)

        # Now we have location of two characters of each pair in diagraph,
        # Now check whether they are in same column

        # * CASE 1: SAME COLUMN
        if location[0][1] == location[1][1]:
            # for this we will take the letter above each character

            for location_row in location:
                plain_text.append(keyTable[(location_row[0] - 1)][location_row[1]])

        # * CASE 2: SAME ROW
        elif location[0][0] == location[1][0]:
            # for this we will take the left letter of each character
            for row_location in location:
                plain_text.append(keyTable[row_location[0]][(row_location[1] - 1)])

        # * CASE 3: NOT SAME ROW OR COLUMN
        else:
            # reverse of the encryption algorithm

            # difference between column of first character and column of second character
            difference = abs(location[0][1] - location[-1][1])
            # print("Difference: " + str(difference))

            # need to form new matrix, according to relative position of two elments (i.e) column position
            if location[0][1] > location[1][1]:
                # this means first character is on the right of the second character, so we need to move left to first character and move right to second character according to difference

                new_matrix = [
                    [location[0][0], location[0][1], (location[0][1] - difference)],
                    [location[1][0], location[1][1], (location[1][1] + difference) % 5],
                ]

            else:
                # this means first character is on the left of the second character, so we need to move right to first character and move left to second character according to difference
                new_matrix = [
                    [location[0][0], location[0][1], (location[0][1] + difference) % 5],
                    [
                        location[1][0],
                        location[1][1],
                        (abs(location[1][1] - difference)),
                    ],
                ]
            # pprint(new_matrix)

            # just the reverse of the encryption algorithm
            for row_location in new_matrix:
                # print(row_location)
                plain_text.append(keyTable[row_location[0]][row_location[-1]])

    # convert list to string
    return "".join(plain_text)


plain_text = decrypt()
print(plain_text)
