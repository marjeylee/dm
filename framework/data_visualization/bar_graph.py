# -*- coding: utf-8 -*-
"""
柱状图
"""
__author__ = 'l'
__date__ = '2018/5/10'
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def dict_visualization(dic):
    """
    字典类型数据梯形图显示
    :param dic: ｛key,num｝
    :return:
    """
    color = '#9966CC'
    x = list(dic.keys())
    y = []
    show_num = 20
    for k in x:
        y.append(dic[k])
    if len(x) > show_num:
        x = x[:show_num]
        y = y[:show_num]
    # config = plt.gcf()
    # plt.figure(figsize=(60, 20))
    plt.bar(x, y, 0.4, color=color)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("bar chart")

    plt.show()
