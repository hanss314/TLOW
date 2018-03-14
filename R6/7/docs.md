# TLOWScript
Well, this is essentially a dummed-down version of assembly.

Each instruction is on a new line and is formed by a command character
and then space seperated arguments to be passed to that command.

Following are the commands and their arguments:

|Command|Name |Argument 1  |Argument 2 (Optional)|
|-------|-----|------------|---------------------|
|s      |Store|Register    |Integral data        |
|c      |Copy |Source reg  |Location reg         |
|a      |Add  |Location reg|Source reg           |
|t      |Sub  |Location reg|Source reg           |
|d      |Div  |Location reg|Source reg           |
|m      |Mult |Location reg|Source reg           |
|p      |Print|Register    |                     |
|o      |Outp |Verbatim    |                     |
|j      |Jmp  |Line #      |                     |
|j      |JmpIf|Register    |Line #               |

## Example
The following code will print `Hello world` 5 times:
```
This is TLOWScript
s foo 5
s bar 1
o Hello world
t foo bar
j foo 3
```

The following code will print the fibonachi sequence:
```
This is TLOWScript
s foo 0
s bar 1
a foo bar
p bar
a bar foo
p foo
j 4
```

