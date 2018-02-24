def tlow4(pancakes, K):
    pancakes = int(''.join(map(str, pancakes)).replace("False", '1').replace("True", '0'), 2)
    flipper = 2**K - 1
    flips = 0
    while pancakes >= flipper:
        if pancakes % 2 == 0: pancakes //= 2
        else:
            flips += 1
            pancakes ^= flipper
    return -1 if pancakes else flips