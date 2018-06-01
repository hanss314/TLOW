def s1r0(text, key):
  Tshift = [0 if not x.isalpha() else 65 if ord(x) <= 90 else 97 for x in text]
  Kshift = [65 if ord(x) <= 90 else 97 for x in key]
  # Capital letter, lowercase letter, or nonalpha
  Kvalue = [ord(key[i]) - Kshift[i] for i in range(len(key))]
  Tvalue = [ord(text[i]) - Tshift[i] for i in range(len(text))]
  # Numerical value (0-25)
  return ''.join([chr((Tvalue[i] + Kvalue[i % len(key)]) % 26 + Tshift[i]) 
                 if Tshift[i] > 0 else text[i] for i in range(len(text))])
  # Adds the numerical values and readds the shift
