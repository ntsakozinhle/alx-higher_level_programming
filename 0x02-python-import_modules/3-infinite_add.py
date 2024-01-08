import sys

argv = sys.argv[1:]
result = sum(int(arg) for arg in argv)

print(result)
