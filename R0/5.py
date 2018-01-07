def atbash(char):
    if(65 <= ord(char) <= 90):
        return(chr(90-ord(char)+65))
    elif(97 <= ord(char) <= 122):
        return(chr(122-ord(char)+97))
    else:
        return char