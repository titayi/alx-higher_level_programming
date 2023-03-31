#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using the requests package
and displays the response body.
"""

import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    response.raise_for_status()
    content = response.content.decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
