def tlow6(code):
    if not code.startswith('This is TLOWScript'): print('NotTLOWException'); return
    n = addr = 0; reg = [0 for _ in range(256)]; jump = []; code = code[18:]
    while n < len(code):
        if code[n] in 'is': reg[addr] += 1 if code[n] == 'i' else -1
        if code[n] in 'fb': addr += 1 if code[n] == 'f' else -1
        if code[n] in 'po': print(chr(reg[addr]) if code[n] == 'p' else reg[addr], end='')
        if code[n] == 'm':  jump.append(n - 1)
        if code[n] == 'j':  n = jump[-1] if reg[addr] else n; jump.pop()
        n += 1
