import pandas as pd
import urllib.request
import requests, json

# CONSTS #

CSV_DATA_URL = "https://www.data.gouv.fr/fr/datasets/r/50625621-18bd-43cb-8fde-6b8c24bdabb3"
                
CSV_DATA_PATH = "fetch/assets/data.csv"

COORDS_DATA_URL = "https://api-adresse.data.gouv.fr/search/"

# FUNCTIONS #

### LOAD DATA CSV ###

def fetchFile():
    """
        Télécharge le fichier de données le plus  
        récent sur le site officiel www.data.gouv.fr
    """
    urllib.request.urlretrieve(
        CSV_DATA_URL, 
        CSV_DATA_PATH
    )

def readData(cols):
    """
        Charger les colonnes du  fichier csv 
        récupéré dynamiquement via fetchFile()
    """
    return pd.read_csv(
        CSV_DATA_PATH, 
        sep=';', 
        low_memory=False, 
        encoding="UTF-8", 
        usecols=cols
    )

### LOAD COORDINATES ###

def getCoordsFromName(name): # df[adStation][i]
    """
        Charger le fichier csv récupéré 
        dynamiquement via fetchFile()
    """
    url = COORDS_DATA_URL + "?q=" + urllib.parse.quote(name)

    try:
    
        data = json.loads(
            requests.get(url).content.decode('unicode_escape')
        )["features"]
    
    except Exception:
        print(url + " can't be reached!")
        return None

    if (len(data) == 0):
        return None
    
    return data[0]["geometry"]["coordinates"]