#!/usr/bin/python3
""" Model to fetch web page """

import urllib.request
import sys

if __name__ == "__main__":
    data = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(data)
    data = data.encode("ascii")
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
