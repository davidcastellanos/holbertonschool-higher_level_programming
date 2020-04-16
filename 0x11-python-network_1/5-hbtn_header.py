#!/usr/bin/python3
"""Requests from URL and returns X-R from https://intranet.hbtn.io/status"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    try:
        r = get(argv[1])
        print(r.headers.get('X-Request-Id'))
    except Exception as e:
        print(e)
