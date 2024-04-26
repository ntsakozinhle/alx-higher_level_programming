#!/bin/bash
# this script takes a URL as input, sends a request to the URL using curl
# in silent mode, and displays the size of the body of the response in bytes.

# Check is a URL is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# URL to fetch
URL="$1"

curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
