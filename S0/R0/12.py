def atbash(char):
  if not char.isalpha(): return char
  return chr(27-(ord(char)-64)+64) if 64 < ord(char) < 91 else chr(27-(ord(char)-96)+96)
