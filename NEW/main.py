import fetch as f
import viewPieChart as p
import viewHistogram as h
import viewMap as m

import dash
import dash_core_components as dcc
import dash_html_components as html

if __name__ == "__main__":
    
    # FETCH #
    f.fetchFile()
    df = f.readData()
    
    # HISTOGRAM #
    viewHistogram = h.Histogram(df).get()

    # PIE CHART #
    viewPieChart = p.PieChart(df).get()

    # MAP #
    viewMap = m.Map(df).get()

    # HTML #
    app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

    app.layout = html.Div(
        children=[
            html.H1(children='Statistiques bornes électriques'), 
            html.Div(children='''Graphiques'''),
            dcc.Graph(id='histogram', figure=viewHistogram),
            dcc.Graph(id='pie-chart', figure=viewPieChart),
            dcc.Graph(id='map', figure=viewMap)
        ])
     
    #Run server
    app.run_server(debug=True)