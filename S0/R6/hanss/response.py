ops = {'p': lambda s, h: print(s[-1]), 'pc': lambda s, h: print(chr(s[-1]), end=''), 'a': lambda s, h: s.append((s.pop()+s.pop()) % 2**64), 'd': lambda s, h: s.append(s.pop() // s.pop()), 'm': lambda s, h: s.append(s.pop() - s.pop()), 'pr': lambda s, h: s.append(s.pop() * s.pop()), 'dr': lambda s, h: s.pop(), 'dp': lambda s, h: s.append(s[-1]), 'hs': lambda s, h: h.update({s.pop(): s.pop()}), 'hg': lambda s, h: s.append(h[s.pop()]), 's': lambda s, h: s.insert(-1, s.pop())}
def r6(code, stack=[], ptr=0, heap={}):
    if not code.startswith('This is TLOWScript\n'): print('NotTLOWException'); return
    code = ''.join(c for c in code[len('This is TLOWScript\n'):] if c.isalnum() or c == ' ').replace('\n', ' ').split(' ')
    while ptr < len(code):
        if code[ptr] in ops: ops[code[ptr]](stack, heap)
        elif code[ptr].startswith('l') and stack[-1] != 0: ptr = int(code[ptr][1:])-1
        else: stack.append(int(code[ptr]) % 2**64)
        ptr += 1
r6(open(__import__('sys').argv[1]).read())
