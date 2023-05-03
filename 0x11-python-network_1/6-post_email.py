#!/usr/bin/python3
"""
Sends a POST request to a given URL using the requests package
with an email as a parameter and displays the body of the response.
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)