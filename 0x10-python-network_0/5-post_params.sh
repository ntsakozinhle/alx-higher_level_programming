#!/bin/bash
# This script takes a URL as input, sends POST request to the URL
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be there for PLD" "$1"
