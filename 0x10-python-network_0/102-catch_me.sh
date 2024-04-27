#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me
curl -s -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" -w "\n%{http_code}"  0.0.0.0:5000/catch_me -o /dev/null | grep -q "200" && echo "You got me!"
