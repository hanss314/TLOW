def vigenere(text, key):
    en = ""
    for i, ch in enumerate(text):
        if ord(ch) in range(65, 91):
            en += chr((ord(ch) + ord(key[i % len(key)]) - 2) % 32 % 26 + 65)
        elif ord(ch) in range(97, 123):
            en += chr((ord(ch) + ord(key[i % len(key)]) - 2) % 32 % 26 + 97)
        else:
            en += ch
    return en