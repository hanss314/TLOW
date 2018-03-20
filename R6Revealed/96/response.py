def tlowscript(code):
    if code[0:18] != 'This is TLOWScript': code = "This is TLOWScript printTLOWopenTLOWquoteNotTLOWExceptionTLOWquoteTLOWclose"
    code = ''.join(c for c in code[19:] if c.isalnum() or c.isspace())
    code = code.replace('TLOWplus', '+').replace('TLOWminus', '-')
    code = code.replace('TLOWtimes', '*').replace('TLOWdivide', '/')
    code = code.replace('TLOWequals', '=').replace('TLOWcolon', ':')
    code = code.replace('TLOWopen', '(').replace('TLOWclose', ')')
    code = code.replace('TLOWcomma', ',').replace('TLOWperiod', '.')
    code = code.replace('TLOWquote', '\'')
    exec(code)
