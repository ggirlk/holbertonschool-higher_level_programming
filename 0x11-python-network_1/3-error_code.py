#!/usr/bin/python3
""" Model to fetch web page """

import urllib.request
import sys
from urllib.error import HTTPError

if __name__ == "__main__":
    try:
        req = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as ex:
        print("Error code: {}".format(ex))
