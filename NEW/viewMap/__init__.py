import pandas as pd
import requests, json
import plotly.express as px
import urllib.parse
import math
import re

class Map:

    def __init__(self, df):
        self.df = df

        self.__parsePuissMax(
            self.df,
            'puiss_max'
        )
        
        self.__parseCoordinates(
            self.df,
            "ad_station",
            'Xlongitude',
            'Ylatitude'
        )

        self.__parsePdcNb(
            self.df, 
            'nbre_pdc'
        )

    def __parsePuissMax(self, df, puissMaxName):
        res = []

        for el in df[puissMaxName]: 
            intList = re.findall("[+-]?\d+", el)

            if (len(intList) == 0):
                res.append(0)
            else:
                res.append(intList[0])

        df[puissMaxName] = res
    
    def __parseCoordinates(self, df, adStation, longitudeName, latitudeName):

        df[longitudeName] = pd.to_numeric(df[longitudeName], errors="coerce")
        df[latitudeName] = pd.to_numeric(df[latitudeName], errors="coerce")

        for i in range(len(df)):
            if (math.isnan(df[longitudeName][i]) or math.isnan(df[latitudeName][i])):
                l = json.loads(
                        requests.get(
                            "https://api-adresse.data.gouv.fr/search/?q=" + 
                            urllib.parse.quote(df[adStation][i])
                        ).content.decode('unicode_escape')
                    )["features"]
                    
                if (len(l) == 0):
                    df.drop([i])
                else:
                    df[longitudeName][i], df[latitudeName][i] = l[0]["geometry"]["coordinates"]

    def __parsePdcNb(self, df, pdcNbrName):

        for i in range(len(df)):
            if (math.isnan(df[pdcNbrName][i])):
                df[pdcNbrName][i] = 0

        df['size'] = [nb+1 for nb in df[pdcNbrName]]

    def get(self):
        
        draw = px.scatter_mapbox(
            self.df, 
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
        
        draw.update_layout(mapbox_style = "open-street-map")

        return draw

    def getDependencies(self):

        return [
            "Ylatitude",
            "Xlongitude",
            "ad_station",
            "nbre_pdc",
            "puiss_max"
        ]