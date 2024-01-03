#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            print("{}\n".format(chr(ord(char) - ord('a') + ord('A'))), end="")
        else:
            print("{}\n".format(char), end="")
