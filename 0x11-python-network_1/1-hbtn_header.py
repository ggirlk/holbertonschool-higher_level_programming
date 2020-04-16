#!/usr/bin/python3
""" Model to fetch web page """

import urllib.request
import sys


req = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(req) as response:
    the_page = response
print(the_page.getheader("X-Request-Id"))
