# -*- coding: utf-8 -*-
import json

from framework.utility.file_path_utility import combine_file_path, get_all_files_under_directory

__author__ = 'l'
__date__ = '2018/5/10'


def get_format_file_path():
    """
    获取所有format_data下的文件路径
    :return:
    """
    data_path = combine_file_path('./national_medicine/data')  # 以项目根目录文相对路径
    return get_all_files_under_directory(data_path)


def loads_file_to_object(json_files_path):
    """
    加载文件成为对象集合
    :param json_files_path:
    :return:
    """
    obj_list = []
    for p in json_files_path:
        with open(p, mode='r', encoding='utf8') as file:
            json_str = file.readlines()[0]
            obj = json.loads(json_str)
            obj_list.append(obj)
    return obj_list


def get_format_data():
    """
    获取数据对象
    :return:
    """
    json_files = get_format_file_path()
    return loads_file_to_object(json_files)


if __name__ == '__main__':
    pass
