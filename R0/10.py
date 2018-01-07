def atbash(st):
  reversible = "abcdefghijklmABCDEFGHIJKLMNOPQRSTUVWXYZnopqrstuvwxyz"
  try:
    return reversible[51-reversible.index(st)]
  except ValueError:
    return st
