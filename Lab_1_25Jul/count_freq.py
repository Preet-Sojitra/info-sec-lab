user_input = input("Enter text: ")

# find frequency of each character
freq = {}
for i in user_input:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)
