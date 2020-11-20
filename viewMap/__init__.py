import pandas as pd
import plotly.express as px
import urllib.parse
import math
import re
import fetch as f

class Map:

    def __init__(self, console, df):
        """
            Construit l'objet PieChart:
            - Récupère la puissance maximale sous forme d'entiers
            - Récupère au mieux la lattitude et la longitude des bornes
            - Traite le nombre de prises afin de faire figurer les bornes 
                qui n'ont pas de prises sur la carte
        """
        self.__console = console
        self.__df = df

        self.__parsePuissMax(
            self.__df,
            'puiss_max'
        )
        
        self.__parseCoordinates(
            self.__df,
            "ad_station",
            'Xlongitude',
            'Ylatitude'
        )

        self.__parsePdcNb(
            self.__df, 
            'nbre_pdc'
        )

    def __parsePuissMax(self, df, puissMaxName):
        """
            Récupère la puissance maximale sous forme d'entiers
            - Valeur entière si possible
            - Sinon, 0
        """
        res = []
        length = len(df[puissMaxName])

        for i in range(length): 

            self.__console.printIteration(i, length)

            intList = re.findall("[+-]?\d+", df[puissMaxName][i])

            if (len(intList) == 0):
                res.append(0)
            else:
                res.append(intList[0])

        df[puissMaxName] = res
    
    def __parseCoordinates(self, df, adStationName, longitudeName, latitudeName):
        """
            Récupère au mieux la lattitude et la longitude des bornes
            - Directement via le CSV, si les champs sont bien formatés,
            - Sinon, récupère le tuple (lattitude, longitude) via
                une API à partir du nom du lieu (adStationName)
        """

        df[longitudeName] = pd.to_numeric(df[longitudeName], errors="coerce")
        df[latitudeName] = pd.to_numeric(df[latitudeName], errors="coerce")
        length = len(df)

        for i in range(length):
            
            self.__console.printIteration(i, length)

            if (math.isnan(df[longitudeName][i]) or math.isnan(df[latitudeName][i])):
                
                coords = f.getCoordsFromName(df[adStationName][i])
                    
                if (coords != None):
                    df[longitudeName][i], df[latitudeName][i] = coords
                    

    def __parsePdcNb(self, df, pdcNbrName):
        """
            Traite le nombre de prises afin de faire figurer les bornes 
            qui n'ont pas de prises sur la carte :
            - On crée une colonne 'size' qui contient pdcNbrName + 1,
                qui sera utilisée pour former la carte, la colonne 
                pdcNbrName étant donc uniquement utilisée en temps
                que référentiel d'affichage textuel
        """
        length = len(df)

        for i in range(length):

            self.__console.printIteration(i, length)

            if (math.isnan(df[pdcNbrName][i])):
                df[pdcNbrName][i] = 0

        df['size'] = [nb+1 for nb in df[pdcNbrName]]

    def get(self):
        """
            Retourne la carte, prêt à être affichée
        """
        
        draw = px.scatter_mapbox(
            self.__df, 
            lat = "Ylatitude", 
            lon = "Xlongitude", 
            hover_name="ad_station",
            hover_data={
                "nbre_pdc" : True,
                "size" : False,
                "Ylatitude" : False,
                "Xlongitude" : False
            },
            labels={
                "puiss_max" : "Puissance",
                "nbre_pdc" : "Nombre de prises",
            },
            color="puiss_max",
            color_continuous_scale=px.colors.qualitative.Plotly,
            #color_continuous_scale=["blue", "green"],
            #range_color=[0, 1],
            size="size",
            zoom = 7
        )
        
        draw.update_layout(mapbox_style = "open-street-map", title="Carte représentant la puissance des bornes éléctriques",
             paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',font = dict(
                family="Courier New, monospace",
                size=13,
             color='#ffffff'
             
            ),)

        return draw

    @staticmethod
    def getDependencies():
        """
            Retourne les dépendances au df, c'est à dire les
            noms de colonnes utilisées du CSV chargé
        """

        return [
            "Ylatitude",
            "Xlongitude",
            "ad_station",
            "nbre_pdc",
            "puiss_max"
        ]
