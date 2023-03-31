#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
Handles HTTPError exceptions and prints out the HTTP status
code in case of an error.
"""

from urllib import request, error
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            content = response.read()
            print(content.decode('utf-8'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
