# VerboseTS Documentation, v0.3.4

## Syntax
All commands start with `This` (which is removed in the reference) and are separated by whitespace. All command arguments are separated by whitespace. General syntax is therefore `This [command] [arguments...]`, where some command arguments are ignored. The *second* argument to some commands is referred to as a **sub-command**.

The program must directly start with `This is TLOWScript`, without any preceding characters.

Example program:
```
This is TLOWScri;pt # The ";" is ignored
This pushes a 1 <- The command "pushes" ignores the second argument, "a"
This pushes 
some 2 // Commands can wrap and some arguments can take any value.
This computes the difference -- Sub-commands are typically found in the second argument.
This does a print an int ; Outputs an integer.
Also, there is no special comment syntax.
```

## Data structure(s)
There is exactly one data structure, a stack, containing integers only. If the stack is empty, it is set to contain one zero. At this stage, attempting to use `computes` will cause an error.

## Command reference

All commands are executed in sequence, except for any conditional and loop blocks. Execution ends when execution reaches the end of the file.

### Control flow commands

#### loops while [zero|...]
If `loops while zero`, repeats the following commands (until the matching `This ends`) while the top of the stack is zero. If `loops while nonzero`, repeats the following commands while the top of the stack is not zero. Loops and conditionals can be nested freely.

*(TODO 0.4.0: Add more conditionals, `loop on stack` and `loop on range` commands.)*

#### runs if [zero|...]
If `runs if zero`, executes the following commands (until the matching `This ends`) while the top of the stack is zero. If `loops if nonzero`, executes the following commands while the top of the stack is not zero. Loops and conditionals can be nested freely.

*(TODO 0.4.0: Add more conditionals.)*

#### ends
Ends the matching `loops` or `runs` command.

### `pushes`: Pushes a value

Does as the headline suggests: pushes an integer value in its second argument (which, due to syntax restrictions, has to be positive *(TODO 0.4.0: Allow `minus` to be used in front of integer literals)*) to the stack.

### `computes`: Arithmetic commands

All commands relating to arithmetic are subcommands of the command `compute`. All of these commands pop two values off the stack (causing an error if there is only one item on the stack) and push the result of the operation applied to the two popped values (popped first *operation* popped second).

The operations are:

* `sum`: Adds the two values together.
* `difference`: Subtracts the second value from the first.
* `product`: Multiplies the two values together.
* `ratio`: Divides the first value by the second, rounding down.
* `remainder`: Gives the first value modulo the second, returning zero if the second value is zero.

### `does`: Various stack operations

This command is used for various operations involving values already on the stack. Usually, this causes an error if not enough values (plus one) are on the stack.

These operations are:

* `print`: Print the top value and print it. If the second argument is `int`, outputs as an integer. If the second argument is `char`, outputs as the corresponding Unicode character.
* `copy <... integer|all>`: Copies either the top value, or if two more arguments are provided, the number of values given by the second argument, unless this argument is `all`, in which case it copies all values excluding the bottommost one.
* `swap`: Swaps the top two values on the stack.
* `drop`: Drops the top value on the stack.