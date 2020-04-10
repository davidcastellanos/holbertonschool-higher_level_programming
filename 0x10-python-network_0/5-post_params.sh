#!/bin/bash
# Sends a POST request and displays response
curl -sd 'email=hr@holbertonschool.com&subject=I will always be here for PLD' "$1"
