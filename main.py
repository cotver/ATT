"""
Arrivals to Thailand
"""

# 3rd-Party modules
import pandas as pd

# modules
import platform
import time

# Our modules
from modules import top10, season, change, graph


years = ["2016", "2017", "2018"]

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"] # list of month

continents = ["East Asia", "Europe", "The Americas", "South Asia", "Oceania", "Middle East", "Africa"] # list of continent



def change_picker(year_dic, years, months, continents):
    """Pick People Arrive changes each year"""

    print('** People Arrive changes each year analyzing :', end=" ")
    changes = change.year_change(year_dic, years, months, continents)
    print("success")
    return changes



def season_picker(year_dic, years, months):
    """Pick People Arrive in each season"""
    
    print('** People Arrive in each season analyzing    :', end=" ")
    seasons = season.season(year_dic, years, months)
    print("success")
    return seasons



def top10_picker(year_dic):
    """Pick top10 continent and country"""

    print('** Top 10 countries analyzing\t\t     :', end=" ")
    
    topcountry = []
    topcontinent = []
    
    for year in years:
        topcountry.append(top10.year_country(year_dic["%s" %year], months, continents))
        topcontinent.append(top10.year_continent(year_dic["%s" %year], months, continents))
    topcountry.append(top10.total_country(year_dic, years, months, continents))
    topcontinent.append(top10.total_continent(year_dic, years, months, continents))

    alltop = {"country":topcountry, "continent":topcontinent}


    print("success")
    return alltop



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


    all_top_10 = top10_picker(year_dic)
    
    people_arrive_season = season_picker(year_dic, years, months)

    people_change = change_picker(year_dic, years, months, continents)

    print('** Creating graph\t\t\t     :', graph.create_graph(years, months, all_top_10, people_arrive_season, people_change))
    print('** Program ended\t\t\t     :', "%.2f" %(time.time()-start_time), "sec")

print('** Python version\t\t\t     :', platform.python_version())
print('** Staring Program....')
main()
