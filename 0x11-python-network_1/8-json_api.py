#!/usr/bin/python3
"""
Takes a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys

if __name__ == '__main__':
    try:
        letter = sys.argv[1]
    except IndexError:
        letter = ""
    response = requests.post('http://0.0.0.0:5000/search_user',
                             data={'q': letter})
    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
