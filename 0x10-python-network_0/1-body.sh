#!/bin/bash
# This script takes a URL as input, sends a GET request to the URL using curl
curl -s -X GET -w "\n%{http_code}" "$1" | awk 'END {if ($NF == 200) {print}}'
