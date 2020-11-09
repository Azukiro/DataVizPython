import fetch as f
import viewPieChart as p
import viewHistogram as h
import viewMap as m
import console as c
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
    # CONSOLE #

    console = c.Console.instance()

    # FETCH #
    
    console.startBlock("FETCH")
    
    f.fetchFile()
    df = f.readData(
        h.Histogram.getDependencies() +
        p.PieChart.getDependencies() +
        m.Map.getDependencies()
    )

    console.endBlock()
    
    # HISTOGRAM #
    
    console.startBlock("HISTOGRAM")

    viewHistogram = h.Histogram(console, df).get()

    console.endBlock()

    # PIE CHART #
    
    console.startBlock("PIE CHART")

    viewPieChart = p.PieChart(console, df).get()

    console.endBlock()

    # MAP #
    
    console.startBlock("MAP")

    viewMap = m.Map(console, df).get()  

    console.endBlock()

    # HTML #
    
    console.startBlock("HTML")

    app = dash.Dash(__name__, external_stylesheets=['/style/style.css'])

    app.layout = html.Div(
        children=[
            html.H1(children='Statistiques bornes électriques',), 
            html.Div(children='''Graphiques'''),
            dcc.Graph(id='histogram', figure=viewHistogram),
            dcc.Graph(id='pie-chart', figure=viewPieChart),
            dcc.Graph(id='map', figure=viewMap)
        ])

    console.endBlock()

    #Run server
    app.run_server(debug=True)