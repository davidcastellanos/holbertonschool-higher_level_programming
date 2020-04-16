#!/usr/bin/python3
'''Sends a request to a URL and displays body'''


if __name__ == "__main__":
    import urllib.error
    import urllib.request
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as r:
            print(r.read().decode('utf8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
