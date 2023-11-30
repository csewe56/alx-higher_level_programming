#!/usr/bin/python3
import dis
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./4-hidden_discovery.py <hidden_4.pyc>")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename, 'rb') as file:
        magic = file.read(4)
        timestamp = file.read(4)
        code = file.read()

    bytecode = dis.Bytecode(code)
    names = set()

    for instruction in bytecode:
        if 'LOAD_GLOBAL' in instruction.opname and not instruction.argrepr.startswith('__'):
            names.add(instruction.argrepr)

    for name in sorted(names):
        print(name)

