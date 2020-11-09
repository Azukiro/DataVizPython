import dash
import dash_core_components as dcc
import dash_html_components as html

class View:

    def __init__(self, console, viewMap, viewHistogram, viewPieChart):
        """
            Construit l'objet View
        """
        self.__app = self.__create(console, viewMap, viewHistogram, viewPieChart)

    def __create(self, console, viewMap, viewHistogram, viewPieChart):
        app = dash.Dash(__name__)

        app.layout = html.Div(
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

        return app

    def runServer(self):
        self.__app.run_server(debug=True)