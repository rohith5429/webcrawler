#!/usr/bin/env python
import requests

print("* * * * * * * * * * * * * * * * * * * * *")
print("*   ___ _ __ __ ___      _| | ___ _ __  *")
print("*  / __| '__/ _` \ \ /\ / / |/ _ \ '__| *")
print("* | (__| | | (_| |\ V  V /| |  __/ |    *")
print("*  \___|_|  \__,_| \_/\_/ |_|\___|_|    *")
print("*                             -R0h1th   *")
print("* * * * * * * * * * * * * * * * * * * * *")
def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "svcet.ac.in"
with open("/home/marshmellow/pyproject/subdomains.list", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print("[+] Discovered subdomain -->" + test_url)
