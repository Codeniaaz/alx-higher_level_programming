#!/usr/bin/python3
# script that takes a URL and an email as command-line arguments

import urllib.parse
import urllib.request
import sys


def send_post(url, email):
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        body = response.read().decode('utf-8')

        print("Response body:")
        print(body)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    send_post(url, email)
