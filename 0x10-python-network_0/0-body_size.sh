#!/bin/bash
# this script takes a URL as input, sends a request to the URL using curl
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
