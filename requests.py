"""
Filename: requests.py
Purpose: To obtain data from USDA api endpoint and put it into a file
Authors: Kymberlee Hill , Swarnim Bhandari
"""
from urllib.request import urlopen
from urllib.parse import urlencode

params = {
    'api_key': '0D98036D-C6D4-390F-A3E4-C7169A050F15',
    'short_description': "TURKEYS, YOUNG, SLAUGHTER, FI - SLAUGHTERED, MEASURED IN HEAD",
    'year__GE' : '1989',
    'year__LE' : '2018',
    'state_alpha' : 'VA',
    'frequency_description' : 'MONTHLY',
    }

url = "http://quickstats.nass.usda.gov/api/api_GET/?" + urlencode(params)

with urlopen(url) as x:
        data = x.read()
        with open("outputdata.json", 'wb') as outf:
            outf.write(data)
