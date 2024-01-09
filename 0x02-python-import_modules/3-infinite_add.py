#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv = argv[1:]
    result = sum(int(arg) for arg in argv)
    print(result)
