"""Top 10"""

def year(data, months, continents):
    """ find top 10 in that year"""
    dic = {}
    for month in months :
        for continent in continents:
            for country in data[month][continent]:
                dic[country] = data[month][continent][country]+dic[country] \
                if country in dic else data[month][continent][country]
    topten = sorted(dic, key=lambda x: dic[x], reverse =True)
    print(topten[:10])
