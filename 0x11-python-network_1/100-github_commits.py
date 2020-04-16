#!/usr/bin/python3
"""function that searches for a value"""
from sys import argv
from requests import get

if __name__ == "__main__":
    usr = 'https://api.github.com/repos/' + argv[2] + '/' + argv[1] + '/commits'
    res = get(usr)
    try:
        out = res.json()
    except:
        print("Not a valid JSON")
    else:
        lst = []
        for entry in out:
            sha = entry['sha']
            author = entry['commit']['author']['name']
            date = entry['commit']['author']['date']
            lst.append((sha, author, date))
    lst.sort(key=lambda x: x[2], reverse=True)
    for entry in lst[:10]:
        print("{}: {}".format(entry[0], entry[1]))