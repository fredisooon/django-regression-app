from welcome.utils.file_utils import *
import pandas as pd
import logging

def set_of_var_is_numeric(depVars, indepVars):
    df = pd.read_csv('welcome/media/data.csv', nrows=2)

    if (var_is_numeric(depVars) and var_is_numeric(indepVars)):
        logging.info('Variables for simple regression is numerics')
        return True
    else:
        return False


def var_is_numeric(listOfVar):
    dataFile = pd.read_csv('welcome/media/data.csv', nrows=2)
    for var in listOfVar:
        if (dataFile.dtypes[var] == 'float64' or dataFile.dtypes[var] == 'int64'):
            print('Is Numeric')
            logging.info(var)
        else:
            print("Is String")
            return False
    return True


def is_logistic_dataset(depVar, indepVar):
    if (dep_data_is_probability(depVar) and var_is_numeric(indepVar)):
        return True
    return False


def dep_data_is_probability(depVar):
    df = pd.read_csv('welcome/media/data.csv')
    depended_unique_list = df[depVar[0]].unique()
    log_unique_list = [0, 1]

    if (len(depended_unique_list) == 2 and
        set(depended_unique_list) >= set(log_unique_list)):

        return True
    else:
        return False


def is_linear_dataset(depVar, indepVar):
    if (set_of_var_is_numeric(depVar, indepVar) and
        not dep_data_is_probability(depVar) and
        not is_ordinal_dataset(depVar, indepVar)):
        print('Dataset in linear')
        return True
    return False


def is_multiple_linear_dataset(depVar, indepVar):
    if (set_of_var_is_numeric(depVar, indepVar) and
        not dep_data_is_probability(depVar) and
        not is_ordinal_dataset(depVar, indepVar)):
        return True
    return False


def is_pair_regression_dataset(depVar, indepVar):
    if (len(depVar) == 1 and len(indepVar) == 1):
        return True
    return False

def is_multiple_regression_dataset(depVar, indepVar):
    if (len(depVar) == 1 and len(indepVar) > 1):
        return True
    return False


def is_ordinal_dataset(depVar, indepVar):
    df = pd.read_csv('welcome/media/data.csv')
    depended_unique_list = df[depVar[0]].unique()
    if (len(depended_unique_list) in range(3,6) and var_is_numeric(indepVar)):
        return True
    return False


def is_multiple_logistic_dataset(depVar, indepVar):
    if (is_logistic_dataset(depVar, indepVar)):
        return True
    return False

def is_multiple_ordinal_dataset(depVar, indepVar):
    if (is_ordinal_dataset(depVar, indepVar)):
        return True
    return False