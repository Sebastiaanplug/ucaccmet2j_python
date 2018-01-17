# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:37:14 2018

@author: Sebastiaan
"""

import json
with open ("precipitation.json") as my_file:
    percip = json.load(my_file)
   
daily_Seattle = list()
for line in percip:
    Stations = line['station']
    Date = line['date']
    Values = line['value']
    if Stations == 'GHCND:US1WAKG0038': 
      daily_Seattle.append(Values)

Seattle_total_percipitation = sum(daily_Seattle)  #total yearly rainfall
print(Seattle_total_percipitation)

monthsinyear = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

Seattle_monthly_percipitation = list()
for month in monthsinyear:
    monthly_Seattle = list()
    for line in percip:
        Stations = line['station']
        Date = line['date'][5:7]
        Values = line['value']
        if Stations == 'GHCND:US1WAKG0038': 
            if Date == month:
                monthly_Seattle.append(Values)
    Seattle_monthly_percipitation.append(sum(monthly_Seattle))

Seattle_relative_month_percipitation = [x / Seattle_total_percipitation for x in Seattle_monthly_percipitation]   
    
with open('Seattle.json','w') as file:
    json.dump({"Seattle": {
            "totalYearlyPrecipitation" : Seattle_total_percipitation,
            "totalMonthlyPrecipitation" : Seattle_monthly_percipitation,
            "state" : "WA",
            "relativeMonthlyPrecipitation": Seattle_relative_month_percipitation,
            "Station" : "GHCND:US1WAKG0038"
        }
},file)
      
