#!/bin/bash
# Takes in a URL, sends a request, and displays the size of the body
curl -so /dev/null -w '%{size_download}\n' "$1"
