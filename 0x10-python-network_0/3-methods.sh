#!/bin/bash
# Get allowed HTTP verbs
curl -sI "$1" | grep Allow: | cut -d' ' -f2-
