#!/usr/bin/python3
""" Model to fetch web page """

import urllib.request


req = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
   the_page = response.read()
print("Body response:")
print("\t- type: {}".format(type(the_page)))
print("\t- content: {}".format(the_page))
s = str(the_page).encode('utf-8')
print("\t- utf8 content: {}".format(s))
