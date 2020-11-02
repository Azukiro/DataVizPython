import pandas as pd
import urllib.request

# CONSTS #

CSV_DATA_URL = "https://www.data.gouv.fr/fr/datasets/r/50625621-18bd-43cb-8fde-6b8c24bdabb3"

CSV_DATA_PATH = "fetch/assets/data.csv"

CSV_DATA_HEADERS = [
    "n_amenageur",
    "n_operateur",
    "n_enseigne",
    "id_station",
    "n_station",
    "ad_station",
    "code_insee",
    "Xlongitude",
    "Ylatitude",
    "nbre_pdc",
    "id_pdc",
    "puiss_max",
    "type_prise",
    "acces_recharge",
    "accessibilité",
    "observations",
    "date_maj",
    "source"
]

# FUNCTIONS #


def fetchFile():
    """
        Télécharge le fichier de données le plus  
        récent sur le site officiel www.data.gouv.fr
    """
    urllib.request.urlretrieve(
        CSV_DATA_URL, 
        CSV_DATA_PATH
    )

def readData():
    """
        Charger le fichier csv récupéré 
        dynamiquement via fetchFile()
    """
    return pd.read_csv(
        CSV_DATA_PATH, 
        sep=';', 
        low_memory=False, 
        encoding="UTF-8", 
        usecols=CSV_DATA_HEADERS
    )
