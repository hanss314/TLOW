def r4(pancakes, k):
  ret, start = 0, int(''.join(['0' if x else '1' for x in pancakes]), 2)
  while start >= 2**k - 1:
    if start % 2 == 1: 
      ret, start = ret + 1, start ^ (2**k - 1)
    start = start >> 1
  return -1 if start else ret
