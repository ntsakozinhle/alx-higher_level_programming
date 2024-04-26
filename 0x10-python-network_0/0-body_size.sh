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

content_length=$(curl -sI "$URL" | grep -i Content-Length | awk '{print $2}')

if [ -z "$content_length" ]; then
	echo "Content-Length header not found. Size could not be determined."
else
	echo "$content_length"
fi
