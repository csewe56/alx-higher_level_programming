#!/usr/bin/python3
"""
This is a magic calculation function.
"""

import dis

def magic_calculation(a, b):
    """Magic calculation function"""
    add = __import__('magic_calculation_102').add
    sub = __import__('magic_calculation_102').sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)

# Display the bytecode for verification
dis.dis(magic_calculation)

