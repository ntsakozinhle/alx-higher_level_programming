#!/usr/bon/python3
"""
Module to authenticate with GitHub API and display user ID.
"""


import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_id = response.json().get('id')
        print(user_id)
    else:
        print(None)
