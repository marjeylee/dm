# -*- coding: utf-8 -*-
"""
统计数据可视化
"""
from framework.data_visualization.bar_graph import dict_visualization
from national_medicine.data_description import quantity_statistics
from national_medicine.data_manage import get_format_data

__author__ = 'l'
__date__ = '2018/5/10'

if __name__ == '__main__':
    f_data = get_format_data()
    medicinal_materials_dict = quantity_statistics(f_data, '处方+')
    dict_visualization(medicinal_materials_dict)
