"""
Arrivals to Thailand
"""

# 3rd-Party modules
import pandas as pd

# modules
import platform
import time

# Our modules
from modules import top10


years = ["2016", "2017", "2018"]

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"] # list of month

continents = ["East Asia", "Europe", "The Americas", "South Asia", "Oceania", "Middle East", "Africa"] # list of continent



def top10_picker(year_dic):
    """ top10"""
    for year in years:
        top10.year_country(year_dic["%s" %year], months if year != "2018" else months[0:10], continents)
        top10.year_continent(year_dic["%s" %year], months if year != "2018" else months[0:10], continents)
    top10.total_country(year_dic, years, months, continents)  
    top10.total_continent(year_dic, years, months, continents)    
    return "success"



def main():
    """Start program"""
    start_time = time.time()
    
    
    year_dic = {}
    for year in years:
        month_dic = {}
        for month in months if year != "2018" else months[0:10]: # 2018 Nov Dec Data not yet available, We'll update when it's available
            dic = {}
            x = pd.ExcelFile("Tourist/%s.xlsx" %year).parse(month) # read excel file
            save = ""
            for j in range(60):
                if x["Country"][j] in continents:
                    dic[x["Country"][j]] = {}
                    save = x["Country"][j]
                else:
                    dic[save].update({x["Country"][j] : x["Number"][j]})
            month_dic[month] = dic
        year_dic[year] = month_dic


    print('** Top 10 countries analyzing\t:', top10_picker(year_dic))
    
    
    print('** Program end at\t:', "%.2f" %(time.time()-start_time), "sec")
  
print('** Python version\t:', platform.python_version())
print('** Staring Program....')
main()

