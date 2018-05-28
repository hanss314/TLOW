def s1r0 (text,key):
    output = ""
    for char in text: 
        if (65 <= ord(char) and ord(char) <= 90) or (97 <= ord(char) and ord(char) <= 122):
            case = 97 if (97 <= ord(char) and ord(char) <= 122) else 65
            shift = (chr(((ord(char)+(ord((key[(len(output) % len(key))]).lower()))-97-case) % 26)+ case))
            output = output + shift
        else:
            output = output+char
    return output;
            