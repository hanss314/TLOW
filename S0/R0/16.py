def atbash_cipher(c):
    s = "zyxwvutsrqponmlkjihgfedcba" if c.islower() else "ZYXVWUTSRQPONMLKJIHGFEDCBA"
    if c not in s: 
        return c  
    else: 
        return s[::-1][s.index(c)] # [::-1] reverses string
