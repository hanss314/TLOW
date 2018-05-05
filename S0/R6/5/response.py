stack = []; localvars = {}; opcodes = {'a': lambda: stack.append(stack.pop() + stack.pop()), 'd': lambda: stack.append(stack.pop() // stack.pop()), 'm': lambda: stack.append(stack.pop() * stack.pop()), 'p': lambda: print(stack.pop()), 'q': lambda: print(chr(stack.pop()), end=""), 's': lambda: stack.append(stack.pop() - stack.pop()), 'x': lambda: localvars.update({stack.pop(): stack.pop()}), 'y': lambda: stack.append(localvars.get(stack.pop()))}
def tlow(text : str):
    if not text.startswith("This is TLOWScript"): print("NotTLOWException") # This is TLOWScript
    else:
        code = "".join(filter(lambda t: t.isalnum(), text[18:])); ptr = 0
        while ptr < len(code):
            if code[ptr].isdigit(): stack.append(int(code[ptr]))
            elif code[ptr] == 'k': ptr -= (1, stack.pop() + 1)[stack.pop() > 0]
            elif code[ptr] in opcodes: opcodes[code[ptr]]()
            ptr += 1
