#!/bin/bash
# Bash script that takes in a URL as an argument
curl -s -X GET --header "X-HolbertonSchool-User-Id: 98" "$1"
