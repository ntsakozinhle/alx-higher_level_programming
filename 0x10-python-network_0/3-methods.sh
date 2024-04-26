#!/bin/bash
# This script takes a URL as input, sends an OPTIONS request to the URL
curl -sI -X OPTIONS "$1" | grep -i Allow | cut -d ' ' -f 2-
