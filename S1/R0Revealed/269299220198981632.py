def s1r0(s,k):
	n,l,u = "","abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i, x in enumerate(s):
		if l.find(x) > -1:
			n += l[(l.find(x) + l.find((k.lower())[i%len(k)])) % 26]
		elif u.find(x) > -1:
			n += u[(u.find(x) + l.find((k.lower())[i%len(k)])) % 26]
		else:
			n += x
	return n
