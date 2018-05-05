import binascii
import re
def toHex(code): return str(binascii.hexlify(code), 'ascii') # Call function with b"python\n code" to get TLOWScript code
def toString(hexString): return str(binascii.unhexlify(hexString), 'ascii') # De-hexlify
def anFilter(string): return re.sub('[^0-9a-zA-Z \t\n\r]+', '', string) # Alphanumeric Filter
def tlow6(code): # Actual TLOWScript Interpreter
    codeSplit = code.split('\n') # Split code
    if anFilter(codeSplit[0]) != "This is TLOWScript": print("NotTLOWException") # Check if TLOWScript
    else: exec(toString(anFilter(codeSplit[1]))) # Run Code

