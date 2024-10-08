# import geopandas as gpd
import csv
from pprint import pprint as pp
import json
import sys

# Set the encoding of the standard output(console window) to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

with open('./usa_overpass_turbo_accommodation.geojson','r',encoding="utf-8") as f:
  contents = f.read()

# Parse the JSON string into a dictionary
geojson_data = json.loads(contents)
#pp(geojson_data)

#Checking number of results
counter_ = 0
for j in geojson_data['features']:
  counter_ +=1
print(f'Number of accommodations: {counter_}')


# Creating dictionary to append into csv file
field_names = ['wheelchair','latitude','longitude','accomm_type','state','name','street','house_number','city','website','phone']
results = []


with open('usa_accommodation.csv','w',encoding='utf-8') as csv_file:
  counter = 0
  for i in geojson_data['features']:
    counter += 1
    latitude = ((i['geometry'])['coordinates'])[0]
    longitude = ((i['geometry'])['coordinates'])[1]
    city = i.get('properties',{}).get('addr:city',None)
    state = i.get('properties',{}).get('addr:state',None)
    street = i.get('properties',{}).get('addr:street',None)
    house_number = i.get('properties',{}).get('addr:housenumber',None)
    name = i.get('properties',{}).get('name',None)
    phone = i.get('properties',{}).get('phone') or i.get('properties',{}).get('contact:phone') or None
    accomm_type = (i['properties'])['tourism']
    url = i.get('properties',{}).get('website',None)
    wheelchair = (i['properties'])['wheelchair']

    dict = {}
    dict['wheelchair'] = wheelchair
    dict['latitude'] = latitude
    dict['longitude'] = longitude
    dict['accomm_type'] = accomm_type
    dict['state'] = state
    dict['name'] = name
    dict['street'] = street
    dict['house_number'] = house_number
    dict['city'] = city
    dict['website'] = url
    dict['phone'] = phone
    results.append(dict)

  spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
  spreadsheet.writeheader()
  spreadsheet.writerows(results)




