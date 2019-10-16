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

    def get_host_info_by_ip(self, ip, minify=True, history=False):
        """
        Returns all services that have been found on the given host IP.
        """
        URL = self.base_url + f'/shodan/host/{ip}?key={self.YOUR_API_KEY}&minify={minify}&history={history}'
        try:
            response = requests.get(URL).json()
            if (not response.get('error')) and response.get('vulns'):
                return response['ip_str']
                # pprint(response)
                # print(response['ip_str'], response['ports'], response.get('vulns'), '\n\n')
        except requests.exceptions.SSLError:
            time.sleep(10)

    def filter_vulnerable_ips(self, file_name):
        g = open('vulnerable_ips.txt', 'a')
        with open('ip_addresses.txt', 'r') as f:
            for ech_ip in set(f.readlines()):
                vul_ip = s.get_host_info_by_ip(ech_ip.strip())
                if vul_ip:
                    g.write(vul_ip + '\n')
        g.close()

s = Shodan()
s.filter_vulnerable_ips('ip_addresses.txt')
