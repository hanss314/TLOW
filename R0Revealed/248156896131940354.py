from string import ascii_lowercase, ascii_uppercase # only what we need
def atbash_cipher(char): # our function definition.
	if char in ascii_lowercase: # The character is a lowercase letter:
		return ascii_lowercase[25 - ascii_lowercase.index(char)] # Python strings are zero-indexed, thus 25 and not 26

	elif char in ascii_uppercase: # The character is an uppercase letter:
		return ascii_uppercase[25 - ascii_uppercase.index(char)] # same logic applies

	else: # The character is neither an uppercase nor a lowercase letter:
		return char # our job here is done