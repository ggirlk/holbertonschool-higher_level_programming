#!/usr/bin/python3
""" Search API """

import sys
import requests


def searchUser(p=""):
    args = dict(q = p,)
    req = requests.post('http://0.0.0.0:5000/search_user', params=args)
    result = req.json()
    if isinstance(res, dict):
        if len(res) is not 0:
            print("[{}] {}".format(res['id'], res['name']))
        else:
            print('No result')
    else:
        print('Not a valid JSON')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        searchUser(sys.argv[1])
    else:
        searchUser()
