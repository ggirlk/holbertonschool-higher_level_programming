#!/usr/bin/python3
""" Model to fetch web page """

import requests

if __name__ == "__main__":
    req = requests.get("https://intranet.hbtn.io/status")
    the_page = req.content
    the_page = the_page.decode('utf-8')
    the_page = str(the_page)
    print('Body response:')
    print("\t- type: {}".format(type(the_page)))
    print("\t- content: {}".format(the_page))
