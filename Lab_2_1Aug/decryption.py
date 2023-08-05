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

key = int(input("Enter key: "))

decrypted_string = ""

for i in cypher_text:
    if i in alphabets:
        decrypted_string += alphabets[(alphabets.index(i) - key) % 26]
    else:
        decrypted_string += i

print("Decrypted string: ", decrypted_string)
