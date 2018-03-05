def r5(state, spoon):
    if spoon < 0 and not state: return 1
    if not state: return 127
    if (state[-1] + spoon) % 256 not in state:
        return 3
    if state[-1] >= spoon and state[-1] - spoon not in state:
        return 2
    if (state[-1] ** 2) % 256 not in state:
        return 1
    return 0
