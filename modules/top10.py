"""Top 10"""
def year_country(data, months, continents):
    """ find top 10 in that year"""
    dic = {}
    for month in months :
        for continent in continents:
            for country in data[month][continent]:
                dic[country] = data[month][continent][country]+dic[country] \
                if country in dic else data[month][continent][country]
    topten = sorted(dic, key=lambda x: dic[x], reverse =True)
    

def year_continent(data, months, continents):
    """ find top 10 in that year"""
    dic = {}
    for month in months :
        for continent in continents:
            for country in data[month][continent]:
                dic[continent] = data[month][continent][country]+dic[continent] \
                if continent in dic else data[month][continent][country]
    topten = sorted(dic, key=lambda x: dic[x], reverse =True)


def total_country(data, years, months, continents):
    """ find top 10 in that year"""
    dic = {}
    for year in years:
        for month in months if year != "2018" else months[0:10]:
            for continent in continents:
                for country in data[year][month][continent]:
                    dic[country] = data[year][month][continent][country]+dic[country] \
                    if country in dic else data[year][month][continent][country]
    topten = sorted(dic, key=lambda x: dic[x], reverse =True)


def total_continent(data, years, months, continents):
    """ find top 10 in that year"""
    dic = {}
    for year in years:
        for month in months if year != "2018" else months[0:10]:
            for continent in continents:
                for country in data[year][month][continent]:
                    dic[continent] = data[year][month][continent][country]+dic[continent] \
                    if continent in dic else data[year][month][continent][country]
    topten = sorted(dic, key=lambda x: dic[x], reverse =True)
