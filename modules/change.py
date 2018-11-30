""" """
def year_change(data, years, months, continents):
    """ """
    dic = {}
    for year in years:
        lis = []
        for month in months:
            if month in data[year]:
                count = 0
                for continent in continents:
                    for country in data[year][month][continent]:
                        count += data[year][month][continent][country]
                lis.append(count)
            else:
                lis.append(None)
        dic[year] = lis

    return dic
