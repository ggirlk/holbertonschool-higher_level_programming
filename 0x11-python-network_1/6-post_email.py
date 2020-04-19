#!/usr/bin/python3
""" Model to fetch web page """

import requests
import sys

if __name__ == "__main__":
    data = {"email": sys.argv[2]}
    req = requests.post(sys.argv[1], data)
    print("Your email is: {}".format(req.json()["email"]))
