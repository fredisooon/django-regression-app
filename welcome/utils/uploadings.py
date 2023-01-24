import numpy as np
import pandas as pd
from scipy import stats
import csv


def handle_uploaded_file(f):
    if f.name.endswith(".csv"):
        print("We have access to the file")
    else:
        print("ERROR")
    df = pd.read_csv(f)
    print(df.columns[0], df.columns[5]) #выводим названия столбцов в файлы 
                                        #чтобы убедится что мы имеем доступ к файлу