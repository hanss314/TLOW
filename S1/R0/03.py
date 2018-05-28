def s1r0(input, key):
    result = ""
    for i, e in enumerate(input.upper()):
        if e.isupper():
            result += chr((ord(e) + ord(key.upper()[i % len(key)])) % 26
                      + ord('a' if input[i].islower() else 'A'))
        else:
            result += e
    return result
