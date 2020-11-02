import pandas as pd
import plotly.express as px
from collections import Counter

class PieChart:

    def __init__(self, df):
        """
            Construit l'objet PieChart:
            - Calcule l'implantation des différents opérateurs
        """
        self.__df = pd.Series(Counter(df["n_operateur"])).to_frame('new_col').reset_index()
        self.__df.columns = ['Opérateur', 'Nombre de bornes']

    def get(self):
        """
            Retourne le pie chart, prêt à être affiché
        """
        
        draw = px.pie(self.__df, values='Nombre de bornes', names='Opérateur')
    
        draw.update_layout(
            title="Pourcentage de présence des opérateurs",
            legend_title="Nom des opérateurs",
            font = dict(
                family="Courier New, monospace",
                size=11,
                color="RebeccaPurple"
            )
        )

        return draw

    @staticmethod
    def getDependencies():
        """
            Retourne les dépendances au df, c'est à dire les
            noms de colonnes utilisées du CSV chargé
        """

        return [
            "n_operateur"
        ]
