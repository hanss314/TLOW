import math

def tlow8(n):
	if n >= 0:
		return int(math.sqrt(n))
	else:
		return -n - (n % 2) * 2