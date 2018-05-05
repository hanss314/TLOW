i=1
p=[-0.6,1.6]
while True:
  p=[(x**2+1)/(x*2-1)for(x)in(p)]
  print(int((p[1]**i-p[0]**i)/(p[1]-p[0])))
  i+=1
