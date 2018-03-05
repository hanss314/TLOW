import random
def evilbot(avocadoes,spoon):
    if spoon < 0 or avocadoes == []: 
        return 2**random.randint(33,255)-1
    else: 
        return 3
