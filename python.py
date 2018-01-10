# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:37:14 2018

@author: Sebastiaan
"""

import json
with open ("precipitation.json") as my_file:
    percip = json.load(my_file)
    
    
#daily_Seattle = list()
#n=0
#for line in percip:
#    Stations = percip[n]['station']
#    Date = percip[n]['date']
#    Values = percip[n]['value']
#    if Stations == 'GHCND:US1WAKG0038': 
#      daily_Seattle.append(Values)
#    n = n + 1
#Seattle_total_percipitation = sum(Seattle)
#print(Seattle_total_percipitation)    


"""
line 8-24 calculate all of the rain fall

""" 


total_year = []
 
        




monthsinyear = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

import json
with open ("precipitation.json") as my_file:
    percip = json.load(my_file)
    for months in monthsinyear:
        monthly_Seattle = []
        for line in percip:
            Stations = line['station']
            if Stations == 'GHCND:US1WAKG0038': 
                Date = line['date'][5:7]
                if Date == monthsinyear:
                    Values = line['value']
                    monthly_Seattle.append(Values)
print (monthly_Seattle)
        
                    

    
    




#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
##Seattle_total_percipitation = sum(Seattle)
##print(Seattle_total_percipitation)    
#
# 
#        
#    
#    
##    
##    
##    
##    stationslist = []
##    stationslist = [percip_dict [2]]
##    print (stationslist)    
##with open ("stations.csv") as file:
##    reader = csv.reader(file)
##    for row in reader:
##        print (row)
##        
