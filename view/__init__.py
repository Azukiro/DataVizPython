import dash
import dash_core_components as dcc
import dash_html_components as html

class View:

    def __init__(self, console, viewMap, viewHistogram, viewPieChart):
        """
            Construit l'objet View et notamment la structure HTML de la page web
        """
        self.__app = dash.Dash(__name__)
        self.__app.layout = html.Div(
            children=[
                html.H1(children='Statistiques bornes électriques',),

                html.Div(
                    className="maindiv",
                    children=[
                        html.Div(className="leftPart", children=[

                            html.H2(children='''Carte'''),
                            dcc.Graph(id='map', className="rigthPart",
                                    figure=viewMap)
                        ]),

                        html.Div(
                            className="rigthPart",
                            children=[
                                html.H2(children='''Graphiques'''),
                                dcc.Graph(id='histogram', className="graph",
                                        figure=viewHistogram, ),
                                dcc.Graph(id='pie-chart',  className="graph",
                                        figure=viewPieChart),
                            ]
                        ),
                    ]
                ),
            ]
        )

    def runServer(self):
        """
            Lance le serveur en local. Le site sera accessible via le lien : http://127.0.0.1:8050/
        """
        self.__app.run_server(debug=True)
