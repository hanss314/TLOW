This is a bare bones stack-based dialect of TLOWScript, that covers just what is needed.
# How to use
Statements are separated by space and executed from left to right. The memory consists of a 64-bit integer stack which begins with 0 elements and all statements operate on it. 
### Supported statements:
- `add`

    Pops the top 2 values and pushes their sum
- `multiply`

    Pops the top 2 values and pushes their difference
- `subtract`

    Pops the top 2 values and pushes their difference
- `divide`

    Pops the top 2 values and pushes their integer quotient
- `printNum`

    Pops the top value and prints it as a decimal number
- `printChr`

    Pops the top value and prints it the corresponding ASCII character
- `dup`

    Duplicates the top value
- `goto`

    Pops the top value and redirects execution to the statement at that position

- **Anyting else** is interpreted as a 64-bit integer literal that is pushed onto the stack