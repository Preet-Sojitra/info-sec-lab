from pprint import pprint  # for pretty printing

key = input("Enter key: ")
plain_text = input("Enter text: ")

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


# For checking if duplicate words in plain text side by side
def checkDuplicateWords(plainText: str) -> str:
    bogus_letter = "x"

    for i in range(len(plainText)):
        if plainText[i] == " ":
            continue
        else:
            # check if next letter is same as current letter, then add bogus letter
            # added check for i < len(plainText) - 1, to handle index out of range error
            if i < len(plainText) - 1 and plainText[i + 1] == plainText[i]:
                plainText = plainText[: i + 1] + bogus_letter + plainText[i + 1 :]

    return plainText


# if last item in diagraph contains only one letter, then add bogus letter
def addBogusForOdd(diagraph: list) -> list:
    # print(diagraph)
    # print(diagraph[-1])
    if len(diagraph[-1]) == 1:
        # add extra letter "z"
        diagraph[-1] = diagraph[-1] + "z"

    # print(diagraph)
    return diagraph


# split plain text in pair of two
def genDiagraph(plainText: str) -> list:
    plainText = checkDuplicateWords(plainText)

    diagraph = [plainText[i : i + 2] for i in range(0, len(plainText), 2)]

    # if length of plain text is odd, then add bogus letter
    if len(plainText) % 2 != 0:
        diagraph = addBogusForOdd(diagraph)

    return diagraph


def sortWord(word: list, location: list) -> tuple:
    isSorted = False
    # if first letter is less than 2nd letter, then row of first should also be less than 2nd low
    if word[0] < word[1]:
        # check if location is less, if not then we will sort location
        if location[0][0] > location[1][0]:
            location = sorted(location, key=lambda x: x[0])
            word = sorted(word, reverse=True)
            isSorted = True

    # print("location in sort word function")
    # print(location)

    return word, location, isSorted


# Main encryption algorithm
def encrypt() -> str:
    keyTable = genKeyTable(key)
    diagraph = genDiagraph(plain_text)

    pprint(keyTable)
    print(diagraph)

    encrypted_text = []

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

        # Now we have location of two characters of each pair in diagraph,
        # Now check whether they are in same column

        # * CASE 1: SAME COLUMN
        if location[0][1] == location[1][1]:
            # for this we will take the letter below each character

            for location_row in location:
                encrypted_text.append(
                    keyTable[(location_row[0] + 1) % len(keyTable)][location_row[1]]
                )

        # * CASE 2: SAME ROW
        elif location[0][0] == location[1][0]:
            # for this we will take the right letter of each character
            for row_location in location:
                encrypted_text.append(
                    keyTable[row_location[0]][(row_location[1] + 1) % 5]
                )

        # * CASE 3: NOT SAME ROW OR COLUMN
        else:
            # for this we will make a matrix and will take the letter at the intersection of the row of first character and column of second character

            # check if need to sort the word
            # need to sort the word if first letter is less than second letter and row of first letter is greater than row of second letter
            word, location, isSorted = sortWord(word, location)
            # print(word, location, isSorted)

            # difference between column of first character and column of second character
            difference = abs(location[0][1] - location[-1][1])
            # print("Difference: " + str(difference))

            # need to form new matrix, according to relative position of two elments (i.e) column position
            if location[0][1] > location[1][1]:
                # this means first character is on the right of the second character, so we need to move left to first character and move right to second character according to difference

                new_matrix = [
                    [location[0][0], location[0][1], (location[0][1] - difference)],
                    [
                        location[1][0],
                        location[1][1],
                        (location[1][1] + difference)
                        % 5,  # if new column is greater than 5, then need to take mod 5 to map it again to beginning
                    ],
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

            # if word is sorted, then swap the rows of new_matrix because we swept the location also
            if isSorted:
                temp = new_matrix
                new_matrix = [new_matrix[1], temp[0]]

            # print(new_matrix)

            # now we have new matrix, now we need to find the letter at the intersection of the row of first character and column of second character
            for row_location in new_matrix:
                # print(row_location)
                encrypted_text.append(keyTable[row_location[0]][row_location[-1]])

    # pprint(encrypted_text)

    # convert list to string
    return "".join(encrypted_text)


encrypted_text = encrypt()
print(encrypted_text)
