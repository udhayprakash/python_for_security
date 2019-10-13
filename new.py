#!/usr/bin/python
"""
Purpose: 
Go to https://nmap.org/download.html and download  nmap & npcap
pip install python-nmap

"""
import nmap
from pprint import pprint 

nm = nmap.PortScanner()
nm.scan('1.22.229.36', '22-443')
print(f'nm.nmap_version:{nm.nmap_version()}')
# help(nm)

for host in nm.all_hosts():
     print('----------------------------------------------------')
     print('Host : %s (%s)' % (host, nm[host].hostname()))
    #  pprint(nm[host])
     print('State : %s' % nm[host].state())
     for proto in nm[host].all_protocols():
         print('----------')
         print('Protocol : %s' % proto)
         lport = sorted(nm[host][proto].keys())
         for port in lport:
             print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
# ----------------------------------------------------
# Host : 127.0.0.1 (localhost)
# State : up
# ----------
# Protocol : tcp
# port : 22   state : open
# port : 25   state : open
# port : 80   state : open
# port : 111  state : open
# port : 443  state : open