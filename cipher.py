cipher_dict = {
    "a": "f",
    "b": "g",
    "c": "h",
    "d": "i",
    "e": "j",
    "f": "k",
    "g": "l",
    "h": "m",
    "i": "n",
    "j": "o",
    "k": "p",
    "l": "q",
    "m": "r",
    "n": "s",
    "o": "t",
    "p": "u",
    "q": "v",
    "r": "w",
    "s": "x",
    "t": "y",
    "u": "z",
    "v": "a",
    "w": "b",
    "x": "c",
    "y": "d",
    "z": "e",
}

plaintext = input("Please enter your sentence: ")
plaintext = plaintext.lower()
ciphertext = ""

for char in plaintext:
    if char in cipher_dict:
        char = cipher_dict[char]
    ciphertext += char

print(ciphertext)
