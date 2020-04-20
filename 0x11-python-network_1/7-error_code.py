#!/usr/bin/python3
""" Model to fetch web page """

import requests
import sys

if __name__ == "__main__":
    try:
        req = requests.get(sys.argv[1])
        print(req.content.decode("utf-8"))
    except requests.exceptions.HTTPError as ex:
        e = ex.decode('utf-8')
        e = ''.join(x for x in e if x.isdigit())
        print("Error code: {}".format(e))
