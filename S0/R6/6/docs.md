# TLOW R6 Documentation

## Program Description

This is a TLOWScript interpreter, where the code is just Python scripts converted from ascii into hexadecimal.

## Generating TLOWScript

Generating TLOWScript code is simple. All you have to do is call the `toHex` function with a `b"binary string"`, then print the output. Here's an example showing many of the TLOWScript features:

```py
hex = toHex(b"""import math
x=1
y=2
z=math.floor(x/y)
print(z)
z=x
while z<3:
    print('a')
    z+=1""")
print(hex)
```

## Running TLOWScript

Once you've got some TLOWScript generated, you'll probably want to run it. This is as simple as calling the `tlow6` function with your code. Here's an example using the code from earlier:

```py
tlow6("""This is TLOWScript
696d706f7274206d6174680a783d310a793d320a7a3d6d6174682e666c6f6f7228782f79290a7072696e74287a290a7a3d780a7768696c65207a3c333a0a097072696e7428276127290a097a2b3d31""")
```

Try adding some ⓃⓞⓝⒶⓛⓟⓗⓐⓝⓤⓜⓔⓡⓘⓒ characters to make sure the code ignores them properly!