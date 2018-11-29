"""graph create"""

import pygal


def graph_topten(alltop):
    """createing topten graph"""
    
    names = ["2016", "2017", "2018", "TOTAL"]
    for topten in alltop:
        for year in alltop[topten]:
            line_chart = pygal.HorizontalBar()
            line_chart.title = '%s %s TOP %s' \
            %(topten, names[alltop[topten].index(year)], "10" if topten == "country" else "")
            for country in year:
                line_chart.add(country[0], country[1])
            line_chart.render_to_file('%s_%s_Top%s.svg' \
            %(topten, names[alltop[topten].index(year)], "_10" if topten == "country" else ""))


def graph_season(data, years):
    """createing People come in each season graph"""
    
    line_chart = pygal.Bar()
    line_chart.title = 'Season'
    line_chart.x_labels = map(str, ["Summer", "Rainy", "Winter"])
    for year in years:
        line_chart.add(year,  data[year])
    line_chart.render_to_file('season.svg')
