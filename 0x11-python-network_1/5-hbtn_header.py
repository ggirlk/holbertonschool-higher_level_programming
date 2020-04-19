#!/usr/bin/python3
""" Model to fetch web page """

import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    print(req.headers["X-Request-Id"])
