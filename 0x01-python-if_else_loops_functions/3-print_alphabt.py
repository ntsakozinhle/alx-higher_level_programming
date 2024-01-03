#!/usr/bin/python3
output = ''.join(chr(i) for i in range(ord('a'), ord('z') + 1))
if 'q' not in output and 'e' not in output:
    print("{}".format(output), end='')
