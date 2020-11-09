import pandas as pd
import plotly.express as px

class Histogram:

    def __init__(self, df):
        """
            Construit l'objet Histogram
        """
        self.__df = df

    def get(self):
        """
            Retourne l'histogramme', prêt à être affiché
        """
        
        draw = px.histogram(self.__df, x="nbre_pdc", log_y=True)

        draw.update_traces(
            marker=dict(
                line=dict(
                    color='rgb(9, 30, 66)', 
                    width=2
                )
            ),
            marker_color='rgb(0, 199, 229)',
        )

        draw.update_layout(
            title="Nombre de prise par borne",
            xaxis_title="Nombre de prises",
            yaxis_title="Nombre de bornes",
            legend_title="Nombre de prises par bornes",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color='#ffffff'
            ),
              paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
        )

        return draw

    @staticmethod
    def getDependencies():
        """
            Retourne les dépendances au df, c'est à dire les
            noms de colonnes utilisées du CSV chargé
        """

        return [
            "nbre_pdc"
        ]
