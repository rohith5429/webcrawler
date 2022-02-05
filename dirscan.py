#!/usr/bin/env python
import requests

print("  * * * * * * * * * * * * * * * * * * *  ")
print("*  ____  _      ____                   *")
print("* |  _ \(_)_ __/ ___|  ___ __ _ _ __   *")
print("* | | | | | '__\___ \ / __/ _` | '_ \  *")
print("* | |_| | | |   ___) | (_| (_| | | | | *")
print("* |____/|_|_|  |____/ \___\__,_|_| |_| *")
print("*                            -R0h1th   * ")
print("  * * * * * * * * * * * * * * * * * * * ")





def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "svcet.ac.in"
with open("//home/marshmellow/pyproject/subdir.list", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print("[+] Discovered subdomain -->" + test_url)
            
