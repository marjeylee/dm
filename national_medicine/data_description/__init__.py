# -*- coding: utf-8 -*-
"""
数据描述
"""
from framework.data_description.descrete_data import list_quantity_statistics, get_range, get_standard_deviation
from national_medicine.data_manage import get_format_data

__author__ = 'l'
__date__ = '2018/5/10'


def quantity_statistics(format_data, type):
    """
    药材数量统计
    :param format_data:
    :param type:
    :return:
    """
    lst = []
    for data in format_data:
        content = data['content']
        lst.extend(content[type])
    return list_quantity_statistics(lst)


if __name__ == '__main__':
    f_data = get_format_data()
    medicinal_materials_dict = quantity_statistics(f_data, '处方+')
    usage_dict = quantity_statistics(f_data, '主治')
    treatment_dict = quantity_statistics(f_data, '功能')
    medicinal_value = list(medicinal_materials_dict.values())
    range_info = get_range(medicinal_value)  # 极差信息
    std = get_standard_deviation(medicinal_value)  # 标准差
    print(medicinal_materials_dict)
