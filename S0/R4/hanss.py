def r4(pancakes, flipper):
    acc = 0
    for n in range(len(pancakes) - flipper + 1):
        if not pancakes[n]:
            pancakes[n:n+flipper] = map(lambda b: not b, pancakes[n:n+flipper])
            acc += 1

    if not all(pancakes): return -1
    return acc

