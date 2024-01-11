#!/usr/bin/python3
""" a Python script that takes in a URL and an email address"""

import requests as reqs
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    resp = reqs.post(url, data={'email': email})
    print(resp.text)
