#!/usr/bin/python3
"""
Module to send a POST request to a URL with an email as parameter
"""


import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = 'http://localhost:5000/post_email'
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
        print(body)
