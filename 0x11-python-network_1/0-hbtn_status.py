#!/usr/bin/python3

import urllib.request

url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    data = response.read()

decoded_data =  data.decode("utf-8")

print("Body response:")
print("\t- type:", type(data))
print("\t- content:", data)
print("\t- utf8 content:", decoded_data)
