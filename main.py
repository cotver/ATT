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
    
    tourist2016 = pd.ExcelFile("Tourist/2559.xlsx")
    tourist2017 = pd.ExcelFile("Tourist/2560.xlsx")
    tourist2018 = pd.ExcelFile("Tourist/2561.xlsx")

    # list of month
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    # list of continent
    continent = ["East Asia", "Europe", "The Americas", "South Asia", "Oceania", "Middle East", "Africa"]

    
    for month in months:
        dic = {}
        dic2 = {}
        x = tourist2016.parse(month)
        for j in range(61):
            dic[x["Country"][j]] = x["Number"][j]
        print(dic)

        
    print('** Program End At\t:', time.time()-start_time, "sec")
  
print('** Python version\t:', platform.python_version())
print('** Staring Program....')
main()
