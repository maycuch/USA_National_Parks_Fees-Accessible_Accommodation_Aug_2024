# USA_National_Parks_Fees_Accessible_Accommodation_Aug_2024

In this project, I have focused on obtaining data regarding ***USA National Parks entrance fees & passes*** and ***wheelchair accessible accommodation*** in the USA. 

In this repository you can find: 
- `config.py` you will need to sign up for National Service Park API in order to obtain your API Key and it can be easily done [here](https://www.nps.gov/subjects/developer/get-started.htm) and add it into this congif.py into row 1
  
- ***`data-sourcing`*** folder including:
  -  `usa_nsp_fees_passes.py` - python code extracting data from [National Park Servicec API](https://www.nps.gov/subjects/developer/api-documentation.htm) and saving them into `usa_nsp_fees_passes.csv`
  -  `usa_overpass_turboaccommodation.geojson` which is a dataset downloaded from __OpenStreetMap (OSM)__ using [Overpass Turbo tool](https://overpass-turbo.eu/) covering accommodation (hotel hostel,guest_house, apartment, alipne_hut, camp_site, caravan_site) where the `wheelchair tag` is set as "yes" or "limited"
  -  `usa_accommodation_overpass_turbo.py` - pyhton code extracting and formatting data into desireable format from the above geojson file and saving it into `usa_accommodation.csv` file
  -  `usa_nsp_basic_park_data.csv` which extracts basic data about each park included in this API into `usa_nsp_basic_park_data.csv`. This file is not used in further project but it was crated with the plan to use it to identify park names and geolocation when merging with other datasets

- ***`jupyter.ipynb`*** - where you can see how I cleaned, explored and visualised data. In the last section of the notebook I focus on question *"Is there any correlation between level of entrance fees and average temperature?"*. My original assumption was that parks with warmer climate would have a higher entrance cost, as I thought, there would be more activities for people to enjoy. Unlike my original assumption, by analysing provided data, I discovered slightly negative correlation between level of entrance fees and average temperature. This can be seen especially for parks with highest annual entrance pass that tend to be in colder range of average annual temperature. One possible explanation could be the fact that parks with colder average temperature tend to have harsh weather conditions which then translates into higher maintainance costs.

- `cleaned_usa_accommodation.csv` and `cleaned_usa_nsp_fees_passes.csv`  - these are files from data-sourcing folder but cleaned in order to be used in Jupyter file
  
- `requirements.txt` highlighting what packages you need in order to run these files
  

