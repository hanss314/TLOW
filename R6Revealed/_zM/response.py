from string import ascii_letters, digits, whitespace # Verbose TLOWScript by -Unknown-, version 0.3.4
def tokenizer(code):code,jumps=[i.split()for i in code.split("This ")][1:]if code.split("This ")[0]==""else[],[];[jumps.append([i,inst[0]=="loops"])if inst[0]in["loops","runs"]else[jump for jump in jumps if len(jump)==2][-1].append(i)if inst[0] == "ends" else None for i,inst in enumerate(code)];return code,jumps
def maths(stk,inst,ip,jumps):stk[0:2]=[{"sum":stk[0]+stk[1],"difference":stk[0]-stk[1],"product":stk[0]*stk[1],"ratio":stk[0]//stk[1],"remainder":stk[0]%stk[1]if stk[1]else 0}[inst[2]]];return stk,ip+1
def various(stk,inst,ip,jumps):return{"print":lambda stk,ip:(print({"char":chr,"int":int}[inst[4]](stk[0]),end=""if"c"in inst[4]else"\n")or((stk[1:]or[0]),ip+1)),"copy":lambda stk,ip:(stk[0:(len(stk)-1 if inst[4]=="all"else int(inst[4]))if len(inst)>3 else 1]+stk,ip+1),"swap":lambda stk,ip:(stk[1:2]+stk[0:1]+stk[2:],ip+1),"drop":lambda stk,ip:(stk[1:]or[0],ip+1)}[inst[2]](stk,ip)
def push(stk,inst,ip,jumps):stk.insert(0,int(inst[2]));return stk,ip+1
def cond(stk,inst,ip,jumps):return stk,(jumps[[i[0]for i in jumps].index(ip)][2])+1 if(stk[0]!=0 if inst[2]=="zero"else stk[0]==0)else ip+1
def blend(stk,inst,ip,jumps):return stk,(jumps[[i[2]for i in jumps].index(ip)][0])if(jumps[[i[2]for i in jumps].index(ip)][1])else ip+1  
def tlowScript(code): 
  code,jumps=tokenizer("".join([i for i in code if i in(ascii_letters+digits+whitespace)]));stk,pointer=([0],1)if(code and code[0][:2]==["is","TLOWScript"])else(print("NotTLOWException")and[],len(code))
  while pointer<len(code):stk,pointer={"computes":maths,"does":various,"pushes":push,"loops":cond,"runs":cond,"ends":blend}[code[pointer][0]](stk,code[pointer],pointer,jumps)