#!/usr/bin/python
"""
Purpose:

https://developer.shodan.io/api
"""
import os
import requests
from pprint import pprint

class Shodan:
    def __init__(self):
        self.base_url = 'https://api.shodan.io'
        self.YOUR_API_KEY = os.getenv('SHODAN')

    def ip_search(self, ip):
        response = requests.get(self.base_url + f'/shodan/host/{ip}?key={self.YOUR_API_KEY}').json()
        if not response.get('error'):
            print(ip)

s = Shodan()

with open('ip_addresses.txt', 'r') as f:
    for ech_ip in f.readlines():
        s.ip_search(ech_ip.strip())