#!/bin/bash
# script that makes a request to catch_me
curl -H 'Origin: HolbertonSchool' -sLX PUT -d user_id=98 "$1"
