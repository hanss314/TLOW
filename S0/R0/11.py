def atbash_cipher(msg) :
    output = ''
    for char in msg:
        if char >= 'a' and char <= 'z':
            output = output + chr(219 - ord(char))
        elif char >= 'A' and char <= 'Z':
            output = output + chr(155 - ord(char))
        else:
            output = output + char
    return output
