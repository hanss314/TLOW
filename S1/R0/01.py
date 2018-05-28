def vigenere(text, key, pos = 0):
    a, A = ord("a"), ord("A") #descriptive variable names
    if len(text) == 0: return ""
    else:
        char = text[0]
        if ord(char) in range(a, a + 26):
            char = chr((ord(char) - a + ord(key[pos].lower()) - a) % 26 + a)
        elif ord(char) in range(A, A + 26):
            char = chr((ord(char) - A + ord(key[pos].lower()) - a) % 26 + A)
        return char + vigenere(text[1:], key, (pos + 1) % len(key))