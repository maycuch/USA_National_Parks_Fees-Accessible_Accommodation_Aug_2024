import requests
import csv
from pprint import pprint as pp
from config import NSP_api_key


# ------------GETTING FEES AND PASSES FROM ENDPOINT /feespasses
url = 'https://developer.nps.gov/api/v1/feespasses'

params = {
    'api_key': NSP_api_key,
    'limit': 1600,  # Number of results to retrieve
    'start': 0    # Starting index for the results
}

response = requests.get(url,params=params)
print(f'\nResponse code: {response.status_code}\n') #checking whether we are connected

#storing all data as a dictionary in variable 'data'
data = response.json()
# pp(data['data'])

#flatten data
flat_data = []

for xs in data['data']:
    flat_data.append(xs)
# pp(flat_data)

# Use Chat GPT to flatten the data variable data (ensure park_code is at the same level as passes/fees data):===========================
# List to store the flattened data
flattened_data = []

# Iterate over each park dictionary in the list
for park_data in flat_data:
    park_code = park_data.get('parkCode')
    isFeeFreePark = park_data.get('isFeeFreePark')

    # Flatten the fees data
    for fee in park_data.get('fees', []):
        flat_entry = {'parkCode': park_code,'isFeeFreePark': isFeeFreePark, 'type': 'fee'}
        flat_entry.update(fee)
        flattened_data.append(flat_entry)

    # Flatten the passes data
    for pass_ in park_data.get('passes', []):
        flat_entry = {'parkCode': park_code, 'type': 'pass'}
        flat_entry.update(pass_)
        flattened_data.append(flat_entry)

# # Print the flattened data
# pp(flattened_data)

# for i in flattened_data:
#     print(i)
#============================================================================================

# Creating dictionary to write into CSV file
field_names = ['park_code','price_type','cost','fee_type','pass_category','description','id']
result = []

with open('usa_nsp_fees_passes.csv','w',encoding='utf-8') as csv_file:
    for x in flattened_data:
        id = x['id']
        park_code = x['parkCode']
        price_type = x['type']
        cost = x['cost']
        pass_category = x['category'] if 'category' in x else None
        description = x['description']
        fee_type = x['entranceFeeType'] if 'entranceFeeType' in x else None

        dict = {}
        dict['id'] = id
        dict['cost'] = cost
        dict['pass_category'] = pass_category
        dict['description'] = description
        dict['park_code'] = park_code
        dict['price_type'] = price_type
        dict['fee_type'] = fee_type
        result.append(dict)


    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
    spreadsheet.writeheader()
    spreadsheet.writerows(result)



