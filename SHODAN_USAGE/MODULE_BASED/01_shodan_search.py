#!/usr/bin/python
"""
Purpose: 
pip install shodan
"""
import shodan
import os
SHODAN_API_KEY = os.getenv('SHODAN')

api = shodan.Shodan(SHODAN_API_KEY)

try:
    # Search Shodan
    results = api.search('apache')
    # Show the results
    print('Results found: %s' % results['total'])
    for result in results['matches']:
        print('IP: %s' % result['ip_str'])
        print(result['data'])
        print('')
except shodan.APIError as e:
    print('Error: %s' % e)