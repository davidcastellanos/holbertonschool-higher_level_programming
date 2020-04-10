#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me
curl -H 'Origin: HolbertonSchool' -sLX PUT -d user_id=98 "$1"
