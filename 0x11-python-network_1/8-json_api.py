#!/usr/bin/python3
"""
Module to send a POST request to http://0.0.0.0:5000/search_user
"""


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    data = {'q': q}
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
