import string
def atbash(letter):
  if letter in string.ascii_uppercase:
    return chr(ord("Z") - ord(letter) + ord("A"))
  elif letter in string.ascii_lowercase:
    return chr(ord("z") - ord(letter) + ord("a"))
  else:
    return letter
