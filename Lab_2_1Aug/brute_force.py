password = input("Enter 3 character password: ")

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

# print(len(password))

for i in range(len(alphabets)):
    guessed_password = ""
    guessed_password = alphabets[i]

    for j in range(len(alphabets)):
        guessed_password = alphabets[i] + alphabets[j]

        for k in range(len(alphabets)):
            guessed_password = alphabets[i] + alphabets[j] + alphabets[k]
            # All combinations of passwords
            # print(guessed_password, end=" ")

            if guessed_password == password:
                print("Correct password is: ", password)
                break
