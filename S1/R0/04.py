def s1r0(input, inputkey):
    keyC, key, output = -1, [], ""
    for char in inputkey: key.append(ord(char.lower()) - ord('a'))
    for char in input:
        keyC += 1
        if char.isalpha():
            orda = ord('a') if char.islower() else ord('A')
            output += chr((ord(char)-orda+key[keyC%4])%26+orda)
        else: output += char
    return output