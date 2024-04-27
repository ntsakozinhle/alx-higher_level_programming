#!/usr/bin/python3
"""
Module to send a request to a URL and display the value
"""


import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        header = response.getheader('X-Request-ID')
        print(header)
