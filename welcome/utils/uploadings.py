import numpy as np
import pandas as pd
import logging as log
from pandas.errors import EmptyDataError


def get_list_of_file_headers(requestFiles):
    urgentFile = requestFiles['file']
    try:
        dataFile = pd.read_csv(urgentFile)
        log.info(f'{urgentFile.name} was successfully read via pandas')

        return get_headers(dataFile)
    except EmptyDataError:
        log.warning(f'{urgentFile.name} is empty')

        return []


def get_headers(dataFile):
    listOfHeaders = list()
    for column in dataFile.columns:
        print(column)
        listOfHeaders.append(column)

    return listOfHeaders