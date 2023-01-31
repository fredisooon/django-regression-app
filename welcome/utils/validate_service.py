from welcome.utils.file_utils import *
import pandas as pd
import logging

def set_of_var_is_numeric(depVars, indepVars):
    df = pd.read_csv('welcome/media/data.csv', nrows=2)

    if (var_is_numeric(df, depVars) and var_is_numeric(df, indepVars)):
        print("OK")
        logging.info('Variables for simple regression is numerics')
        return True
    else:
        return False


def var_is_numeric(dataFile, listOfVar):
    for var in listOfVar:
        if (dataFile.dtypes[var] == 'float64' or dataFile.dtypes[var] == 'int64'):
            print('Is Numeric')
            logging.info(var)
        else:
            print("Is String")
            return False
    return True

