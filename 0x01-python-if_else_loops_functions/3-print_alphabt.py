#!/usr/bin/python3
output = ''.join(chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in {'q', 'e'})
print("{}".format(output), end='')
