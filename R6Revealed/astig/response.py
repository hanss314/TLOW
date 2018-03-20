def parser(precode, var = {"*": 16}):
  code, stack, keywords = ''.join(c for c in precode if c.isalnum()), [], {"a": ("arith:Add",lambda: (lambda x,y: stack.append(x+y))(stack.pop(),stack.pop())),"s": ("arith:Subtract",lambda: (lambda x,y: stack.append(x-y))(stack.pop(),stack.pop())),"m": ("arith:Muliply",lambda: (lambda x,y: stack.append(x*y))(stack.pop(),stack.pop())),"d": ("arith:Divide",lambda: (lambda x,y: stack.append(x//y))(stack.pop(),stack.pop())),"r": ("arith:Remainder",lambda: (lambda x,y: stack.append(x%y))(stack.pop(),stack.pop())),"p": ("arith:Power",lambda: (lambda x,y: stack.append(x**y))(stack.pop(),stack.pop())),"n": ("arith:Negate",lambda: (lambda x: stack.append(-x))(stack.pop())),"c": ("logic:Complement",lambda: (lambda x: stack.append(~x))(stack.pop())),"0": ("arith:0",lambda: (lambda x: stack.append(10*x))(stack.pop())),"1": ("arith:1",lambda: (lambda x: stack.append(10*x+1))(stack.pop())),"2": ("arith:2",lambda: (lambda x: stack.append(10*x+2))(stack.pop())),"3": ("arith:3",lambda: (lambda x: stack.append(10*x+3))(stack.pop())),"4": ("arith:4",lambda: (lambda x: stack.append(10*x+4))(stack.pop())),"5": ("arith:5",lambda: (lambda x: stack.append(10*x+5))(stack.pop())),"6": ("arith:6",lambda: (lambda x: stack.append(10*x+6))(stack.pop())),"7": ("arith:7",lambda: (lambda x: stack.append(10*x+7))(stack.pop())),"8": ("arith:8",lambda: (lambda x: stack.append(10*x+8))(stack.pop())),"9": ("arith:9",lambda: (lambda x: stack.append(10*x+9))(stack.pop())),"O": ("str:Ord",lambda: (lambda x: stack.append(ord(x)))(stack.pop())),"u": ("str:Unicode",lambda: (lambda x: stack.append(chr(x)))(stack.pop())),"B": ("io:stringBuilder",lambda: ((lambda x,y: stack.append(x+y))(stack.pop(),code[var["*"]+1]),var.update({"*":var["*"]+1}))),"L": ("var:Load",lambda: (lambda x,y: var.update({x:y}))(stack.pop(),stack.pop())),"Y": ("var:copY",lambda: (lambda x,y: var.update({x:var[y]}))(stack.pop(),stack.pop())),"j": ("ctrl:Jump-a",lambda: (lambda x: var.update({"*":x}))(stack.pop())),"C": ("stack:Copy",lambda: (lambda x: (stack.append(x),stack.append(x)))(stack.pop())),"W": ("stack:sWap",lambda: (lambda x,y: (stack.append(x),stack.append(y)))(stack.pop(),stack.pop())),"D": ("stack:Delete",lambda: stack.pop()),"J": ("ctrl:Jump-r",lambda: (lambda x: var.update({"*":var["*"]+x}))(stack.pop())),"T": ("str:Take",lambda: (lambda x,y: stack.append(y[x]))(stack.pop(),stack.pop())),"F": ("ctrl:iF jump-r",lambda: (lambda x,y: var.update({"*":var["*"]+x*(y!=0)}))(stack.pop(),stack.pop())),"G": ("ctrl:if Goto",lambda: (lambda x,y: var.update({"*":x*(y!=0)+var["*"]*(y==0)}))(stack.pop(),stack.pop())),"U": ("var:Unload",lambda: (lambda x: stack.append(var[x]))(stack.pop())),"A": ("var:Add-to",lambda: (lambda x,y: var.update({x:var[x]+y}))(stack.pop(),stack.pop())),"e": ("arith:Equal",lambda: (lambda x,y: stack.append((x==y)+0))(stack.pop(),stack.pop())),"l": ("arith:unequaL",lambda: (lambda x,y: stack.append((x!=y)+0))(stack.pop(),stack.pop())),"x": ("logic:bitwise Xor",lambda: (lambda x,y: stack.append(x^y))(stack.pop(),stack.pop())),"b": ("logic:Bitwise and",lambda: (lambda x,y: stack.append(x&y))(stack.pop(),stack.pop())),"w": ("logic:bitWise or",lambda: (lambda x,y: stack.append(x|y))(stack.pop(),stack.pop())),"t": ("logic:noT",lambda: (lambda x: stack.append((not x)+0))(stack.pop())),"g": ("arith:Greater",lambda: stack.append((stack.pop()>stack.pop())+0)),"f": ("arith:Fewer",lambda: stack.append((stack.pop()<stack.pop())+0)),"I": ("io:Integer",lambda: (stack.append(int(code[var["*"]+1])),var.update({"*":var["*"]+1}))),"S": ("io:String",lambda: (stack.append(str(code[var["*"]+1])),var.update({"*":var["*"]+1}))),"i": ("io:Input",lambda: (stack.append(input()))),"Q": ("magic:Quine1",lambda: (stack.append(code))),"q": ("magic:Quine2",lambda: (stack.append(precode))),"z": ("const:Zero",lambda: (stack.append(0))),"y": ("const:Yes",lambda: (stack.append(1))),"E": ("const:Empty",lambda: (stack.append(""))),"M": ("const:Maxnum",lambda: (stack.append(2**64-1))),"H": ("magic:Helloworld",lambda: (stack.append("Hello world!"))),"K": ("debug:stacK",lambda: (stack.append(str(stack)))),"k": ("debug:Kill",lambda: var.update({"*":-2})),"N": ("debug:No-op",lambda: "do nothing"),"V": ("debug:Vardump",lambda: (stack.append(str(var)))),"o": ("io:Output",lambda: print(stack.pop())),"h": ("debug:Help",lambda: (lambda x: print(x,"=",keywords[x][0]))(stack.pop())),"X": ("prog:eXec",lambda: parser(stack.pop(), var)),"R": ("prog:Run",lambda: parser(var[stack.pop()], var)),"Z": ("stack:Zero",lambda: stack.clear()),"P": ("prog:Polymorph",lambda: (lambda x,y: locals().update({'code':code[:x]+y+code[x+1:]}))(stack.pop(),stack.pop())),"v": ("prog:View",lambda: (lambda x: stack.append(code[x]))(stack.pop())),}
  if code[:len("ThisisTWOWscript")] != "ThisisTWOWscript":
    print("NotTLOWException")
    return
  while 0 <= var["*"] < len(code):
    if code[var["*"]] in keywords: 
      keywords[code[var["*"]]][1]()
    var["*"] = var["*"]+1