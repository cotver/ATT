"""
Arrivals to Thailand
"""

# 3rd-Party modules
import pandas as pd

# modules
import platform
import time


def main():
    """Start program"""
    start_time = time.time()
    

    # list of month
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    # list of continent
    continent = ["East Asia", "Europe", "The Americas", "South Asia", "Oceania", "Middle East", "Africa"]

    
    year_dic = {}
    for year in ["2016", "2017", "2018"]:
        month_dic = {}
        for month in months if year != "2018" else months[0:10]: # 2018 Nov Dec Data not yet available, We'll update later
            dic = {}
            x = pd.ExcelFile("Tourist/%s.xlsx" %year).parse(month) # read excel file
            save = ""
            for j in range(61):
                if x["Country"][j] in continent:
                    dic[x["Country"][j]] = {}
                    save = x["Country"][j]
                else:
                    dic[save].update({x["Country"][j] : x["Number"][j]})
            month_dic[month] = dic
        year_dic[year] = month_dic
    print(year_dic)

        
    print('** Program End At\t:', "%.2f" %(time.time()-start_time), "sec")
  
print('** Python version\t:', platform.python_version())
print('** Staring Program....')
main()
