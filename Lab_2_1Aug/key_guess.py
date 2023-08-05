with open("encrypted.txt", "r") as f:
    cypher_text = f.read()

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
    "j",
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

decrypted_strings = []

for key in range(26):
    decrypted_string = ""
    for letter in cypher_text:
        if letter in alphabets:
            index = alphabets.index(letter)
            decrypted_string += alphabets[(index - key) % 26]
        else:
            decrypted_string += letter

    decrypted_strings.append(decrypted_string)


print(decrypted_strings)
