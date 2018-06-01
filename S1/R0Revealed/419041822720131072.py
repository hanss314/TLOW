def slr0(text, key):
    keys = [ord(c.lower()) - ord('a') for c in key]
    f = lambda ch, i: (ord(ch) - ord('a') + keys[i % len(key)]) % 26 + ord('a') if (ord(ch) - ord('a')) // 26 == 0 \
    else (ord(ch) - ord('A') + keys[i % len(key)]) % 26 + ord('A') if (ord(ch) - ord('A')) // 26 == 0 \
    else ord(ch)
    return ''.join([chr(f(text[i], i)) for i in range(len(text))])
