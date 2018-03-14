def tlowscript(code):
  mem,ptr,instruction,prog = [0 for i in range(9999)],0,-1,code.replace("This is TLOWScript","")
  if not code.startswith("This is TLOWScript"): return print("NotTLOWException")
  while instruction < len(prog)-1:
    instruction += 1
    char = prog[instruction]
    if char in "RL": ptr = (ptr+{"R":1,"L":-1}[char])%9999
    elif char in "PN": print({"P":chr(mem[ptr]),"N":mem[ptr]}[char])
    elif char in "ASMQCID": mem[ptr] = {"A":lambda m,p: m[(p-1)%9999]+m[m[p]],"S":lambda m,p: m[(p-1)%9999]-m[m[p]],"M":lambda m,p: m[(p-1)%9999]*m[m[p]],"Q":lambda m,p: m[(p-1)%9999]//m[m[p]],"C":lambda m,p: m[m[p]],"I":lambda m,p: m[p]+1,"D":lambda m,p: m[p]-1}[char](mem,ptr)
    elif char == "J": instruction += mem[ptr]
