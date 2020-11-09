import sys
import plotly
import plotly.express as px
import pandas as pd
import math
import re
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
    
    # df["price"] = [ (1 if ("payant" in str(stringPrice).lower()) else 0) for stringPrice in df['acces_recharge']]

    l = []
    for stringPuiss in df['puiss_max']: 
        intList = re.findall("[+-]?\d+", stringPuiss)
        if (len(intList) == 0):
            l.append(0)
        else:
            l.append(intList[0])
    df["formatted_puiss"] = l
    

    df['Xlongitude'] = pd.to_numeric(df["Xlongitude"], errors="coerce")
    df['Ylatitude'] = pd.to_numeric(df["Ylatitude"], errors="coerce")

    for i in range(len(df)):
        if (math.isnan(df['Xlongitude'][i]) or math.isnan(df['Ylatitude'][i])):
            print(i)
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

    df['size'] = [nb+1 for nb in df['nbre_pdc']]
    
    fig = px.scatter_mapbox(
        df, 
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
            "formatted_puiss" : "Puissance",
            "nbre_pdc" : "Nombre de prises",
        },
        color="formatted_puiss",
        color_continuous_scale=px.colors.qualitative.Plotly,
        #color_continuous_scale=["blue", "green"],
        #range_color=[0, 1],
        size="size",
        zoom = 7
    )
    
    fig.update_layout(mapbox_style = "open-street-map")

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
    