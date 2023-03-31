#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter and displays
the body of the response (decoded in utf-8).
"""

from urllib import request, parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = parse.urlencode({'email': email}).encode()
    with request.urlopen(url, data) as response:
        content = response.read()
        print(content.decode('utf-8'))
