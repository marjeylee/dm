# -*- coding: utf-8 -*-
"""
离散数据描述
"""
import math

__author__ = 'l'
__date__ = '2018/5/10'

from collections import defaultdict
import numpy as np


def list_quantity_statistics(lis):
    """
    list中数量统计，生成dict类型数据｛key:num｝
    :param lis: list
    :return:
    """
    if (lis is None) or len(lis) < 1:
        raise Exception('输入list异常', 1)
    dic = defaultdict(int)
    for l in lis:  # l 一般为可hash object
        dic[l] = dic[l] + 1
    sort_list = sorted(dic.items(), key=lambda d: d[1], reverse=True)
    di = {}
    for s in sort_list:
        di[s[0]] = s[1]
    return di


def get_range(value_list):
    """
    获取极差—list中的最大值和最小值之间的差
    :param value_list:
    :return:
    """
    value_list.sort(reverse=True)
    r = value_list[0] - value_list[len(value_list) - 1]
    max_value = value_list[0]
    min_value = value_list[len(value_list) - 1]
    return {'range': r, 'max_value': max_value, 'min_value': min_value}


def get_standard_deviation(value_list):
    """
    获取方差
    :param value_list:
    :return:
    """
    arr = np.array(value_list)
    return np.std(arr)


def get_variance(value_list):
    """
    标准差
    :param value_list:
    :return:
    """
    value = get_standard_deviation(value_list)
    return math.pow(value, 2)


if __name__ == '__main__':
    ll = [1, 2, 4, 5, 6, 3, 2, 2, 1, 2, 2, 2, 2, 2]
    a = list_quantity_statistics([1, 2, 34, 4, 5, 6, 3, 2, 2, 1, 2, 2, 2, 2, 2, 1])
    rang = get_range(ll)
    std = get_standard_deviation(ll)
    variance = get_variance(ll)
    print(std)
