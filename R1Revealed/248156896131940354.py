a, b, c = 1, 1, 0
fib = lambda a, b, c: ((not ((c + 1) % 10) or print(b)) and (b, a + b, c + 1)) or fib(b, a + b, c + 1)
while True:
	while print(a) or ((c + 1) % 10):
		a, b, c = b, a + b, c + 1
	a, b, c = fib(a, b, c + 1)