
import pandas as pd
from consts import *

# 47 317

def readData():
    return pd.read_csv(CSV_DATA_PATH, sep=';', low_memory=False, encoding="UTF-8", usecols=CSV_DATA_HEADERS)

def createDict(data, keys, values):
    return { 
        tuple(
            df[key][i] 
            for key in keys
        )
            :
        {
            val : df[val][i]
            for val in values
        } 
        for i in range(len(data)) 
    };

if __name__ == "__main__":

    df = readData()

    print( 
        createDict(
            df, 
            ["Xlongitude", "Ylatitude"],
            ["n_operateur", "ad_station", "nbre_pdc", "puiss_max", "type_prise", "acces_recharge"]
        )
    )

    	
