import numpy as np
import pandas as pd
import logging as log
import copy
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
        listOfHeaders.append(column)

    return listOfHeaders


def save_file_to_media(f):
    filecopy = copy.deepcopy(f)
    clear_csv_storage_file()
    dest = open('welcome/media/data.csv', 'wb+')
    for chunk in filecopy.chunks():
        dest.write(chunk)
    dest.close()


def clear_csv_storage_file():
    dest_clear = open('welcome/media/data.csv', 'a')
    dest_clear.truncate()
    dest_clear.close()