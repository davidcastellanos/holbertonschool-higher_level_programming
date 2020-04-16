#!/usr/bin/python3
"""Requests from URL and returns body response"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    try:
        r = get(argv[1])
        if r.status_code >= 400:
            print('Error code: {}'.format(r.status_code))
        else:
            print(r.text)
    except Exception as e:
        print(e)
