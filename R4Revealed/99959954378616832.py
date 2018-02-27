def pancakes(l, k):
    c, i, n = 0, 0, len(l) - sum(l)
    while i <= len(l) - k:
        if not l[i]:
            for j in range(i, i + k):
                l[j] = not l[j]
                n += (not l[j]) - l[j]
            c += 1
        i += 1
    return -1 if n else c
