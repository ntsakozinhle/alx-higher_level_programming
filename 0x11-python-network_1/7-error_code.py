#!/usr/bin/python3
"""
Module to send a request to a URL and display the body of the response
"""


import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
