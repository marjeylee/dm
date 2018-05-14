# -*- coding: utf-8 -*-
"""
用于数据读取
"""
from framework.utility.number_utility import get_random_number_list_from_range
from national_medicine.data_manage import get_clean_data
from national_medicine.machine_learning_model.classification.multi_classification.neural_network import __get_mapping
import numpy as np

__author__ = 'l'
__date__ = '2018/5/11'
clean_data = get_clean_data()

type_size = 1300


def get_batch_train_data():
    """
    批量获取数据
    :return:
    """
    max_size = len(clean_data)
    random_int_list = get_random_number_list_from_range(num_size=5, num_range=(0, max_size - 1))
    batch = []
    for i in random_int_list:
        batch.append(clean_data[i])
    return batch


def get_batch(batch_data, data_type, mapping):
    """
    输入数据集
    :param batch_data:
    :param data_type:
    :param mapping:
    :return:
    """
    vector_batch = []
    for data in batch_data:
        materials = data[data_type]
        vector = np.zeros((1, type_size), dtype=np.float32)
        for key in materials:
            vector[0][mapping[key]] = 1
        vector_batch.append(vector)
    return np.concatenate(tuple(vector_batch))


def change_to_batch_vector(batch_data, data_vector_mapping):
    """
    更改数据成为向量
    :param batch_data:
    :param data_vector_mapping:
    :return:
    """
    input_batch = get_batch(batch_data, 'materials', data_vector_mapping[0])
    output_batch = get_batch(batch_data, 'usage', data_vector_mapping[1])
    return input_batch, output_batch


def get_train_vector_batch():
    """
    获得可训练的batch
    :return:
    """
    batch_data = get_batch_train_data()
    data_vector_mapping = __get_mapping()
    return change_to_batch_vector(batch_data, data_vector_mapping)


if __name__ == '__main__':
    pass
