import requests
import pandas as pd
import csv

# trackcorona.live/api/countries => response: location,latitude,longitude,confirmed,dead,recovered,updated 
def get_and_save_countries():
    url = 'https://www.trackcorona.live/api/countries'
    r = requests.get(url)
    data = r.json()
    data = data["data"]
  
    with open("corona/dash_apps/finished_apps/apicountries.csv","w",newline="",encoding ='utf-8') as f:  
        title = "location,country_code,latitude,longitude,confirmed,dead,recovered,updated".split(",") 
        cw = csv.DictWriter(f,title,delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        cw.writeheader()
        cw.writerows(data)





   

 

