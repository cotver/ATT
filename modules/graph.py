"""graph create"""

import pygal


def graph_topten(topten):
    """createing"""
    names = ["2016", "2017", "2018", "TOTAL"]
    for year in topten:
        line_chart = pygal.HorizontalBar()
        line_chart.title = '%s TOP 10' %(names[topten.index(year)])
        for country in year:
            line_chart.add(country[0], country[1])
        line_chart.render_to_file('%s_Top_10.svg' %(names[topten.index(year)]))

