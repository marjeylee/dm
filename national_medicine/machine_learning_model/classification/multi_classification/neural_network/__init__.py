# -*- coding: utf-8 -*-
"""
神经网络多分类
"""
import json

from framework.utility.file_path_utility import combine_file_path, get_all_files_under_directory
from national_medicine.data_manage import get_clean_data

__author__ = 'l'
__date__ = '2018/5/10'


def __get_set(clean_data, key_name):
    """
    :param clean_data:
    :param key_name:
    :return:
    """
    s = set()
    for dct in clean_data:
        for item in dct[key_name]:
            s.add(item)
    return s


def __get_item_mapping(usage_set):
    """
    获取每一项对应输入输出为的位置关系
    :param usage_set:
    :return:
    """
    mapping = {}
    i = 0
    for u in usage_set:
        mapping[u] = i
        i = i + 1
    return mapping


def __save_mapping():
    """
    保存mapping
    :return:
    """
    input_to_vector_mapping = __get_item_mapping(materials_set)
    output_to_vector_mapping = __get_item_mapping(usage_set)
    input_path = combine_file_path(
        'national_medicine/machine_learning_model/classification/multi_classification/neural_network/data'
        '/input_mapping.txt')
    with open(input_path, mode='w', encoding='utf8') as file:
        json_str = json.dumps(input_to_vector_mapping)
        file.write(json_str)
    output_path = combine_file_path(
        'national_medicine/machine_learning_model/classification/multi_classification/neural_network/data'
        '/out_mapping.txt')
    with open(output_path, mode='w', encoding='utf8') as file:
        json_str = json.dumps(output_to_vector_mapping)
        file.write(json_str)


def __get_mapping():
    """
    获取输入输出映射
    :return:
    """
    input_path = combine_file_path(
        'national_medicine/machine_learning_model/classification/multi_classification/neural_network/data'
        '/input_mapping.txt')
    with open(input_path, mode='r', encoding='utf8') as file:
        json_str = file.readlines()[0]
        in_mapping = json.loads(json_str, encoding='utf8')
    output_path = combine_file_path(
        'national_medicine/machine_learning_model/classification/multi_classification/neural_network/data'
        '/out_mapping.txt')
    with open(output_path, mode='r', encoding='utf8') as file:
        json_str = file.readlines()[0]
        out_mapping = json.loads(json_str, encoding='utf8')
    return in_mapping, out_mapping


if __name__ == '__main__':
    c_data = get_clean_data()
    materials_set = __get_set(c_data, 'materials')  # 1029
    usage_set = __get_set(c_data, 'usage')  # 1022
    treatment = __get_set(c_data, 'treatment')  # 3731
    # __save_mapping()
    input_mapping, output_mapping = __get_mapping()
    print(len(materials_set))
