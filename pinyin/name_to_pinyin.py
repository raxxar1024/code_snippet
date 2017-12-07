#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pypinyin import lazy_pinyin


def read_data():
    import xlrd
    data = xlrd.open_workbook('excelFile.xls')
    table = data.sheets()[0]
    names = table.col_values(0)
    for i in xrange(len(names)):
        # name_pinyin = "".join(lazy_pinyin(names[i])) + "_1"
        name_pinyin = "".join(map(lambda x: x[0], lazy_pinyin(names[i]))) + "_1"
        print "['%s', '%s_1', '%s']," % (name_pinyin, names[i], names[i])


if __name__ == "__main__":
    read_data()
