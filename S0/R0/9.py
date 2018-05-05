def atbash(l):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    try:
        to_return = alphabet[25 - alphabet.index(l[0].lower())]
        if l[0].isupper(): to_return = to_return.upper()
        return to_return
    except (ValueError, IndexError):
        return l