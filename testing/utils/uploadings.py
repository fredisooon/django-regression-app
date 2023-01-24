import numpy as np
import pandas as pd
from scipy import stats
import csv


def handle_uploaded_file(f):
    if f.name.endswith(".csv"):
        print("OK")
    else:
        print("ERROR")
    df = pd.read_csv(f)
    print(type(df.columns))
    print(df.columns[0], df.columns[5])
    """X = np.array(df['hs_grad'])
    Y = np.array(df['poverty'])
    res = stats.linregress(df['hs_grad'], df['white'])
    print(res)"""
