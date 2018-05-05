import binascii # Modified NoahTLS with
import re       # hopefully no line wraps
def tlow8(input):
    code = """This is TLOWScript
7b2d3530303a3530302c323a312c31303a337d5b515d""".split('\n')
    if code[0] != "This is TLOWScript": return "NotTLOWException"
    trueCode = str(binascii.unhexlify(code[1]), 'ascii').replace("Q", f"{input}")
    regCheck = re.compile('[\{,]Q:'.replace('Q', f"{input}"))
    if regCheck.search(trueCode): return eval(trueCode)
    return input