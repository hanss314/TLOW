def atbash_cipher(input): # I liked the sound of "FLOW" more than "TLOW"
    aZ = map(chr, (range(ord('a'), ord('z')+1) + range(ord('A'), ord('Z')+1)))
    Za = sorted(aZ, reverse=True)
    convert = dict(zip(aZ, Za))
    return convert[input]if(input in convert)else(input)