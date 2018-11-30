"""
People come in each season
"""

def season(data, years, months):
    
    dic = {}
    summer = ["Mar", "Apr", "May"]
    rainy = ["Jun", "Jul", "Aug", "Sep", "Oct"]
    winter = ["Jan", "Feb", "Nov", "Dec"]

    
    for year in years:
        count_summer = 0
        count_rainy = 0
        count_winter = 0
        for month in data[year]:
            count = 0
            for continent in data[year][month]:
                for country in data[year][month][continent]:
                    count += data[year][month][continent][country]
            if month in summer:
                count_summer += count
            elif month in rainy:
                count_rainy += count
            elif month in winter:
                count_winter += count
                
        dic[year] = [count_summer/3, count_rainy/5, count_winter/4]

    return dic
