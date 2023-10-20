from Crypto.Cipher import AES

# key = input("Enter 16 character key: ")

# # check if key is 16 characters
# if len(key) != 16:
#     print("Key must be 16 characters")
#     exit()

# convert key to 16 bytes
# convert key to 16 bytes
# key = hex()

# Convert key to ascii
# key_ascii = []

# for i in range(0, len(key)):
#     key_ascii.append(ord(key[i]))

# # convert the ascii key to hex
# key_hex = []

# for i in range(0, len(key_ascii)):
#     key_hex.append(hex(key_ascii[i]))

# # print(key_hex)

# # remove the 0x from the hex
# key_hex = [i[2:] for i in key_hex]
# # print(key_hex)

# final_key = "".join(key_hex)
# print(final_key)

# plaintext = input("Enter plaintext: ")

# aes_cipher = AES.new(final_key, AES.MODE_ECB)


key = b"Sixteen byte key"
cipher = AES.new(key, AES.MODE_EAX)

data = b"Two One Nine Two"

print(data)

nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(data)

print(ciphertext)
# print(tag)

print(type(ciphertext))

# convert to ascii
# plaintext_ascii = []
# ascii = ciphertext.decode("ascii")
# print(ascii)
