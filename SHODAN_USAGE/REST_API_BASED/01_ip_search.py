#!/usr/bin/python
"""
Purpose:

https://developer.shodan.io/api
"""
import os
import requests
from pprint import pprint
import time


class Shodan:
    def __init__(self):
        self.base_url = 'https://api.shodan.io'
        self.YOUR_API_KEY = os.getenv('SHODAN')
        self.vulnerable_ips = ''

    def get_host_info_by_ip(self, ip, minify=True, history=False):
        """
        Returns all services that have been found on the given host IP.
        """
        URL = self.base_url + f'/shodan/host/{ip}?key={self.YOUR_API_KEY}&minify={minify}&history={history}'
        try:
            response = requests.get(URL).json()
            if (not response.get('error')) and response.get('vulns'):
                self.vulnerable_ips += ip + '\n'
                # pprint(response)
                print(response['ip_str'])#, response['ports'], response.get('vulns'), '\n\n')
        except requests.exceptions.SSLError:
            time.sleep(10)

    def filter_vulnerable_ips(self, file_name):
        with open('ip_addresses.txt', 'r') as f:
            for ech_ip in set(f.readlines()):
                s.get_host_info_by_ip(ech_ip.strip())

        if self.vulnerable_ips:
            print(self.vulnerable_ips)
            with open('vulnerable_ips.txt', 'w') as g:
                g.write(self.vulnerable_ips)
                g.close()

s = Shodan()
s.filter_vulnerable_ips('ip_addresses.txt')
