n=0
def f(n)n<3?n-1:f(n-1)+f(n-2)end
loop{n+=1
puts f n}


