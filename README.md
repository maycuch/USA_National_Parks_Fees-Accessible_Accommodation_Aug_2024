# USA_National_Parks_Fees_Accessible_Accommodation_Aug_2024

In this project, I have focused on obtaining data regarding ***USA National Parks entrance fees & passes*** and ***wheelchair accessible accommodation*** in the USA. 

To review my work look at :
- `data-sourcing` folder including python code to extract data from [National Park Servicec API](https://www.nps.gov/subjects/developer/api-documentation.htm) and another code tackling data extracted from OpenStreetMap (OSM) using [Overpass Turbo tool](https://overpass-turbo.eu/).
  - You will need Python editor such as Pycharm and some basic libraries such as requests, json, sys, csv.
  
- `maria-jupyter.ipynb` where you can see how I cleaned, explored and visualised data. In the last section of the notebook I focus on question *"Is there any correlation between level of entrance fees and average temperature?"*. My original assumption was that parks with warmer climate would have a higher entrance cost, as I thought, there would be more activities for people to enjoy. Unlike my original assumption, by analysing provided data, I discovered slightly negative correlation between level of entrance fees and average temperature. This can be seen especially for parks with highest annual entrance pass that tend to be in colder range of average annual temperature. One possible explanation could be the fact that parks with colder average temperature tend to have harsh weather conditions which then translates into higher maintainance costs.
  -  you will need to install libraries such as pandas, matplotlib.pyplot and seaborn in order to see charts.
