#!/bin/bash
# This script takes a URL as inout, sends DELETE request to the URL
curl -sX DELETE "$1"
