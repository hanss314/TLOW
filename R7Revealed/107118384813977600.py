#This is TLOWScript
#6b3d503d310a7768696c6520313a50256b20616e64207072696e74286b293b502a3d6b2a6b3b6b2b3d31
n = 1
f = 1   # (n-1)!^2
while True:
    if f % n == 1:
        print(n)
    f *= n * n
    n += 1
# Uses modified version of https://en.wikipedia.org/wiki/Wilson%27s_theorem
