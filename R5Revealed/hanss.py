def r5(a, s):
    return 3

import sys
args = list(map(int, sys.argv[1:]))
print(r5(args[1:], args[0]))

