#!/bin/bash
#this script sends a JSON POST request to a URL passed as first argument
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
