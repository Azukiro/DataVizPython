import sys
import plotly
import plotly.express as px
import pandas as pd
import math
from consts import *
import requests, json
import urllib.parse

def readData():
    return pd.read_csv(
        CSV_DATA_PATH, 
        sep=';', 
        low_memory=False, 
        encoding="UTF-8", 
        usecols=CSV_DATA_HEADERS
    )

if __name__ == "__main__":
    df = readData()
    
    """
    df[['Xlongitude', 'Ylatitude']].apply(
        pd.to_numeric, errors='coerce'
    )
    """

    df['Xlongitude'] = pd.to_numeric(df["Xlongitude"], errors="coerce")
    df['Ylatitude'] = pd.to_numeric(df["Ylatitude"], errors="coerce")

    for i in range(len(df)):
        
        
        if (math.isnan(df['Xlongitude'][i]) or math.isnan(df['Ylatitude'][i])):
            l = json.loads(
                    requests.get(
                        "https://api-adresse.data.gouv.fr/search/?q=" + 
                        urllib.parse.quote(df["ad_station"][i])
                    ).content.decode('unicode_escape')
                )["features"]
                
            if (len(l) == 0):
                df.drop([i])
            else:
                df["Xlongitude"][i], df["Ylatitude"][i] = l[0]["geometry"]["coordinates"]


        if (math.isnan(df['nbre_pdc'][i])):
            df['nbre_pdc'][i] = 0

    fig = px.scatter_mapbox(
        df, 
        lat = "Ylatitude", 
        lon = "Xlongitude", 
        hover_name = "ad_station", 
        hover_data = [
            "acces_recharge", 
            "type_prise"
        ],
        color="Xlongitude",
        color_continuous_scale=px.colors.cyclical.IceFire,
        size="nbre_pdc",
        zoom = 7
    )
    
    fig.update_layout(mapbox_style = "open-street-map")

    fig.update_layout(margin = {
        "r": 0,
        "t": 0,
        "l": 0,
        "b": 0
    })

    """
    for i in range(len(STATIONS)):
        folium.CircleMarker(
            location = (LATS[i], LONGS[i]),
            radius = TEMPS[i]*2,
            color = 'crimson',
            fill = True,
            fill_color = 'crimson'
        ).add_to(fig)
    """

    fig.show()
    