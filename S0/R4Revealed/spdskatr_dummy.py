def tlow(pancakes, size):
    result = 0
    for i in range(len(pancakes) - size + 1):
        if not pancakes[i]:
            for j in range(size):
                pancakes[i + j] ^= True
            result += 1
    return -1 if False in pancakes else result
