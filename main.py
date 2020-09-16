
import pandas as pd
from consts import *

# 47 317

if __name__ == "__main__":

    df = pd.read_csv(CSV_DATA_PATH, sep=';', low_memory=False, encoding="UTF-8", usecols=CSV_DATA_HEADERS)
    print(df)