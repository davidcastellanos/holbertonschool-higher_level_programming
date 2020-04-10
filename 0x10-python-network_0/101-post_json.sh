#!/bin/bash
# POST a JSON file to web server
curl -s -X POST -H "Accept: application/json" -H "Content-Type: application/json" -d "@$2" $1
