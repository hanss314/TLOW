# TLOWScript
This language is centered around a single (limited) bank of registers and then
a few single-character commands which somehow manages to form a turing-complete
language that matches hanss' spec. ¯\\\_(ツ)\_/¯

The registers is an array of integers with no limit to size meaning that you
can make any integer you want if you try hard enough. The currently used
register is stored in a "pointer" that can be incremented or decremented at
will.

## Syntax
Well, every file must start with `This is TLOWScript`, but after that each
command is as follows:

|Command|What it actually does                                       |
|-------|------------------------------------------------------------|
|i      |Increment the current register by 1                         |
|s      |Decrement the current registrt by 1                         |
|f      |Increment the pointer by 1                                  |
|b      |Decrement the pointer by 1                                  |
|p      |Print the ASCII representation of the current register      |
|o      |Print the current register as an integer string             |
|m      |Set a marker to jump to                                     |
|j      |Jump to the most recent marker if the current register is >0|

## Examples
What documentation would be complete without examples? The following outputs
`Hello World!\n` to the console.

```
This is TLOWScriptiiiiiiiimfiiiimfiifiiifiiifibbbbsjfififsffimbjbsjffpfssspiiiiiiippiiipffpbspbpiiipsssssspsssssssspffipfiip
```

Right. You though that was bad? Due to the magical nature of only parsing
alphanum characters, that is functionally equivilant to the following:

```
This is TLOWScriptii$%iii"iiimfiiii^$Wmfiifiiifii£"ifibb^$£bbsj'fifi'#fsff.imb,jb.sjf.f,p.fsss"pii\\iiii£$ipp%i£iip"£ffp$£bs$pbpi$%iips£$"sssssp$%£sss^%ss[]sssp[[[ffipfiip
```

But to top it all off, that can be written as the following and still be
functionally equivilant:

```
This is TLOWScriptii$%iii"iiigamfkxgiiii^$Wmfiiafduicxzkiifii£"zifgibb^$£bkbsj'fifi'#fsfgf.imb,jb.sjgf.fxz,p.fsss"kpii\\xzgiiizi£$ipzaup%i£igip"£ffp$£kbsg$pbpi$%iuipgs£$"sssxxssap$%£sszs^%ss[]sssp[[[ffxipafiipgkkk
```

And, of course, you can just keep going. Thank me later.
