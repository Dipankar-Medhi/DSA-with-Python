Bitwise operations are operations that manipulate the individual bits of binary numbers. In Python, there are six bitwise operators:

Bitwise AND (&): Performs a bitwise AND operation on two binary numbers, returning a new binary number where each bit is set to 1 only if both corresponding bits in the original numbers are set to 1. For example:

```
a = 0b1101
b = 0b1010
c = a & b
print(bin(c))  # Output: 0b1000
```

Bitwise OR (|): Performs a bitwise OR operation on two binary numbers, returning a new binary number where each bit is set to 1 if either corresponding bit in the original numbers is set to 1. For example:

```
a = 0b1101
b = 0b1010
c = a | b
print(bin(c))  # Output: 0b1111
```

Bitwise XOR (^): Performs a bitwise XOR (exclusive OR) operation on two binary numbers, returning a new binary number where each bit is set to 1 if only one of the corresponding bits in the original numbers is set to 1. For example:

```
a = 0b1101
b = 0b1010
c = a ^ b
print(bin(c))  # Output: 0b0111
```

Bitwise NOT (~): Performs a bitwise NOT operation on a binary number, returning a new binary number where each bit is inverted (i.e., 0s become 1s and 1s become 0s). Note that this operator is unary (i.e., it only takes one operand). For example:

```
a = 0b1101
b = ~a
print(bin(b))  # Output: -0b1110 (Note: the output is negative because the sign bit is 1.)
```

Left shift (<<): Shifts the bits of a binary number to the left by a specified number of positions, filling in the empty spaces with 0s. For example:

```
a = 0b1101
b = a << 2
print(bin(b))  # Output: 0b110100
```

Right shift (>>): Shifts the bits of a binary number to the right by a specified number of positions, discarding the bits that are shifted off and filling in the empty spaces with 0s (if the number is unsigned) or with the sign bit (if the number is signed). For example:

```
a = 0b1101
b = a >> 2
print(bin(b))  # Output: 0b0011
```