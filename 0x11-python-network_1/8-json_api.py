#!/usr/bin/python3
""" Search API """

import sys
import requests


def searchUser(p=""):
    args = {'q': p}
    req = requests.post('http://0.0.0.0:5000/search_user', data=args)
    try:
        res = req.json()
        if len(res) is not 0:
            print("[{}] {}".format(res['id'], res['name']))
        else:
            print('No result')
    except:
        print('Not a valid JSON')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        searchUser(sys.argv[1])
    else:
        searchUser()
