#!/usr/bin/python3
"""Send a POST request to a url with the payload being an email address"""
from urllib.request import urlopen
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    data = urlencode({'email': argv[2]}).encode('utf-8')
    with urlopen(argv[1], data) as response:
        print(response.read().decode('utf-8'))
