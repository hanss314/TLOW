def shift(char: int, dist: str) -> int:
    return (char - 97 + dist) % 26 + 97 if 96 < char < 122 else \
           (char - 65 + dist) % 26 + 65 if 64 < char < 90  else \
           char

def s1r0(text: str, key: str) -> str:
    key = [ord(i) - 97 for i in key.lower()] * len(text)

    return ''.join(chr(shift(ord(i), d)) 
                   for i, d in zip(text, key))
