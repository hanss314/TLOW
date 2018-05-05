r3 = lambda x: [[x[i]+x[i-1]*k for k in range(x[i])] for i in range(len(x)-1,-1,-1)]
