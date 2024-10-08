import requests
import csv
from pprint import pprint as pp
from config import NSP_api_key


# ------------GETTING FEES AND PASSES FROM ENDPOINT /feespasses
url = 'https://developer.nps.gov/api/v1/parks'

params = {
    'api_key': NSP_api_key,
    'limit': 5000,  # Number of results to retrieve
    'start': 0    # Starting index for the results
}

response = requests.get(url,params=params)
print(f'\nResponse code: {response.status_code}\n') #checking whether we are connected

#storing all data as a dictionary in variable 'data'
data = response.json()
# pp(data['data'])

# Creating dictionary to write into CSV file
field_names = ['park_code','fullName','latitude','longitude','states','id']
result = []

counter = 0
with open('usa_nsp_basic_park_data.csv','w',encoding='utf-8') as csv_file:
    for park in data['data']:
        id = park['id']
        fullName = park['fullName']
        latitude = park['latitude']
        longitude = park['longitude']
        states = park['states']
        parkCode = park['parkCode']
        counter += 1
        #print(counter,park['parkCode'],park['fullName'],park['latitude'],park['longitude'],park['states'])

        dict = {}
        dict['id'] = id
        dict['fullName'] = fullName
        dict['latitude'] = latitude
        dict['longitude'] = longitude
        dict['states'] = states
        dict['park_code'] = parkCode
        result.append(dict)


    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
    spreadsheet.writeheader()
    spreadsheet.writerows(result)



