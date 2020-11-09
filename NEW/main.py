import fetch as f
import viewPieChart as p
import viewHistogram as h
import viewMap as m

import dash
import dash_core_components as dcc
import dash_html_components as html

if __name__ == "__main__":
    """
        Programme principal :
        - Télécharge le fichier CSV et charge ses données (FETCH)
        - Crée les éléments graphiques (HISTOGRAM, PIE CHART, MAP)
        - Lance le serveur web (HTML)
    """
    
    # FETCH #
    f.fetchFile()
    df = f.readData(
        h.Histogram.getDependencies() +
        p.PieChart.getDependencies() +
        m.Map.getDependencies()
    )
    
    # HISTOGRAM #
    viewHistogram = h.Histogram(df).get()

    # PIE CHART #
    viewPieChart = p.PieChart(df).get()

    # MAP #
    viewMap = m.Map(df).get()  

    # HTML #
    app = dash.Dash(__name__)



    app.layout = html.Div(
        children=[
            html.H1(children='Statistiques bornes électriques',), 
            html.Div(className="maindiv", children=[
            html.Div(    className="leftPart",children=[
            
                html.H2(children='''Graphiques'''),
 dcc.Graph(id='histogram', className="graph", figure=viewHistogram, ),
    dcc.Graph(id='pie-chart',  className="graph", figure=viewPieChart),
            ]),
                 dcc.Graph(   className="rigthPart", id='map', figure=viewMap)  
            
        ]),])
     
    #Run server
    app.run_server(debug=True)