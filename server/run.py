import os
from csv import reader
import numpy as np
from train import train_data
import torch
from pandas import read_csv


os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

TRAIN_DATA = True


def data_load(filepath):
    with open(filepath, 'rt', encoding='UTF-8') as raw_data:
        readers = reader(raw_data, delimiter=',')
        x = list(readers)
        data = np.array(x)
    data = np.delete(data, 0, 0)
    list_all = []
    for i in data:
        list_each = []
        for j in i:
            list_each.append(int(j))
        list_each[-1] -= 1
        list_all.append(list_each)
    data = np.array(list_all)
    return data


def data_process(data):
    trains = data[:, : -1]
    labels = data[:, -1]
    data = (trains, labels)
    return data


if __name__ == '__main__':
    if TRAIN_DATA:
        train = data_load('./data/train.csv')
        test = data_load('./data/test.csv')
        train = data_process(train)
        test = data_process(test)
        train_data(train, test)
    else:
        pass
