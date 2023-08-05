user_input = input("Enter string: ")
# print(user_input)

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

encrypted_string = ""

for i in user_input:
    if i in alphabets:
        encrypted_string += alphabets[(alphabets.index(i) + key) % 26]
    else:
        encrypted_string += i

# print(encrypted_string)

with open("encrypted.txt", "w") as file:
    file.write(encrypted_string)
    print("Encrypted Successfully")
