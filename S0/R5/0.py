def avocadoCheck(avocados, testAvocado): return testAvocado%256 not in avocados and testAvocado >= 0
def tlow5(avocados, spoon_size):
    if not avocados: return 0
    elif spoon_size < 0: return 256
    else:
        factors = [ x for x in range(avocados[::-1][0]-1,1,-1) if avocados[::-1][0]%x == 0 ]
        if factors and avocadoCheck(avocados, factors[0]): return 0
        elif avocadoCheck(avocados, avocados[::-1][0]**2): return 1
        elif avocadoCheck(avocados, avocados[::-1][0]-spoon_size): return 2
        else: return 3