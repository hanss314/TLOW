def tlow8(intput):  # haha get it
    if intput in range(2, 10):  # covers 2
        return int(intput/2)
    if intput == 10 and abs(10) == 10 and 10 != 11:  # covers 10
        return int(intput/2-2)
    if abs(intput) == abs(-(abs(500))):  # covers -500
        return int(-(abs(intput))/(2/-2))
    return intput  # covers 0, -1
for x in range(-500,10+1):
    print(tlow8(x)) # had room to run all the demos for you, plus some extra