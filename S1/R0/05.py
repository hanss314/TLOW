import string
copycase = lambda old,new: new.upper() if old in string.ascii_uppercase else new.lower()
def tlows1r0(plaintext,key):
  ciphertext = ""
  for i in range(len(plaintext)):
    if plaintext[i].lower() not in string.ascii_lowercase:
      ciphertext += plaintext[i]
    else:
      ciphertext += copycase(plaintext[i],chr(((ord(plaintext[i].lower()) + ord(key[i%len(key)].lower()) - 2*ord("a")) % 26) + ord("a")))  
  return ciphertext
