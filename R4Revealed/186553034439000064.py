def flip(cakes, size): # flipping is an abelian operation, and flipping twice is the identity
    count = 0          # that means it's a binary choice for each location to flip
    for i in range(len(cakes) - size + 1):  # assume the first i are correct
        if not cakes[i]:                    # do we need to flip the ith? this is our only chance
            for j in range(size):           # yes? now we use our multiflipper
                cakes[i+j] = not cakes[i+j] # now we've flipped them
            count += 1
    return count if all(i for i in cakes) else -1 # if they haven't all been flipped
                                                  # it means it's impossible
