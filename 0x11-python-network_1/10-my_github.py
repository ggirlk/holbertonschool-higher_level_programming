#!/usr/bin/python3
""" Search API """

import sys
import requests


def gitApi(p="", t=""):
    token = "token "+t
    args = {'Authorization': token, 'username': p}
    req = requests.get('https://api.github.com/user', headers=args)
    try:
        res = req.json()
        if len(res) is not 0:
            print(res['id'])
        else:
            print('None')
    except:
        print('None')

if __name__ == "__main__":
    if len(sys.argv) > 2:
        gitApi(sys.argv[1], sys.argv[2])
