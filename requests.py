"""
Filename: extract.py
Authors: Kymberlee Hill , Swarnim Bhandari
"""
import requests
import json

api_key = "0D98036D-C6D4-390F-A3E4-C7169A050F15"
response = requests.get("http://quickstats.nass.usda.gov/api/api_GET/?key="+ api_key +"&year__GE=1989&year__LE=2018&program=SURVEY&sector=\'ANIMALS & PRODUCTS\'&group=POULTRY&commodity_desc=TURKEYS&category=SLAUGHTERED&data_item__LIKE='F1 - SLAUGHTERED, MEASURED IN HEAD'&format=csv&state_alpha=VA")

bad_error = response.raise_for_status()
status = response.status_code
print(bad_error)
print(status)

with open('outputfile.json', 'w') as outf:
  outf.write(response.text)
