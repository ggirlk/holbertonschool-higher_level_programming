#!/usr/bin/python3
""" Model to fetch web page """

import requests

if __name__ == "__main__":
    req = requests.get("https://intranet.hbtn.io/status")
    the_page = req.content
    print("\t- type: {}".format(type(the_page)))
    print("\t- content: {}".format(the_page.decode('utf-8')))
