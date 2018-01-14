def Atbash(InputChar):                  #Who Needs 10 Lines when you can do it in 5
	up = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
	down = 'zyxwvutsrqponmlkjihgfedcba'
	Output = (up[ord(InputChar) - 65]) if InputChar.isupper() == True else (down[ord(InputChar) - 97]) if InputChar.islower() == True else InputChar
	return Output