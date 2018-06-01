def vigenere(plaintext, key):
    output = bytearray(plaintext, "ASCII")  # List of each character's ASCII value
    for index, letter in enumerate(output):
        if plaintext[index].isalpha():
            if plaintext[index].isupper(): avalue = 65  # Value of uppercase A
            if plaintext[index].islower(): avalue = 97  # Value of lowercase a
            a0z25ofletter = output[index] - avalue
            displacement = bytes(key.upper(), "ASCII")[index % len(key)] - 65
            output[index] = avalue + ((a0z25ofletter + displacement) % 26)
    return bytearray.decode(output, "ASCII")
