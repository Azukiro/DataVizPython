import sys
import plotly
import plotly.express as px
import pandas as pd
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
    
    # df[['Xlongitude', 'Ylatitude']].apply(pd.to_numeric)

    for i in range(len(df)):
        try:
            #print(i)
            #df.loc[:, ('Xlongitude', i)] = float(df.loc[:, ('Xlongitude', i)])
            #df.loc[:, ('Ylatitude', i)] = float(df.loc[:, ('Ylatitude', i)])
            df["Xlongitude"][i] = float(df["Xlongitude"][i])
            df["Ylatitude"][i] = float(df["Ylatitude"][i])
        except ValueError:
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

    """
    fig = px.scatter_mapbox(
        df, 
        lat = "Ylatitude", 
        lon = "Xlongitude", 
        hover_name = "ad_station", 
        hover_data = [
            "acces_recharge", 
            "type_prise"
        ],
        color_discrete_sequence = [
            "fuchsia"
        ], 
        zoom = 10
    )
    fig.update_layout(mapbox_style = "open-street-map")

    fig.update_layout(margin = {
        "r": 0,
        "t": 0,
        "l": 0,
        "b": 0
    })

    fig.show()
    """
    