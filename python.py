# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:37:14 2018

@author: Sebastiaan
"""

import json
with open ("precipitation.json") as my_file:
    percip = json.load(my_file)
    Seattle = [item for item in percip
                     if item['station'] == 'GHCND:US1WAKG0038']
    
    Seattle_total_percipitation = sum(item['value'] for item in seattle_dict)
    
    

    
    Date = [item['date'][5:7] for item in Seattle]
    Values = [item['value'] for item in Seattle]
    monthvalue = zip(Date,Values)
    
    for k,v in monthvalue:
        monthy_Seattle[(int(k) - 1)] += v
 
        
                    
    Relative_month =  [x / Seattle_total_percipitation for x in monthy_Seattle]
    
    
    with open('Seattle.json','w') as file:
        json.dump({"Seattle": {
                "totalYearlyPrecipitation" : Seattle_total_percipitation,
                "totalMonthlyPrecipitation" : monthly_Seattle,
                "state" : "WA",
                "relativeMonthlyPrecipitation": Relative_month,
                "Station" : "GHCND:US1WAKG0038"
            }
    },file)
      
