#!/usr/bin/python3
for ascii_val in range(122, 96, -1):
    print("{}".format(chr(ascii_val if ascii_val % 2 == 0 else ascii_val - 32)), end="")  # noqa
