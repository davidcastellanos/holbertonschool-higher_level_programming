#!/usr/bin/python3
"""Takes my github credentials and uses gh api to display my id"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    try:
        r = get('https://api.github.com/user', auth=(argv[1], argv[2]))
        j = r.json()
        print(j.get('id'))
    except ValueError as e:
        print(e)
