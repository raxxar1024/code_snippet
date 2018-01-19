# -*- coding: utf-8 -*-
import xlrd


def get_data_from_file(file_name, key_column_num, value_column_num):
    dict_data = {}
    data = xlrd.open_workbook(file_name)
    table = data.sheets()[0]  # 通过索引顺序获取
    for i in xrange(1, table.nrows):
        dict_data[table.row_values(i)[key_column_num]] = table.row_values(i)[value_column_num]
    return dict_data


def match(file_name, key_column_num, dict_account):
    data = xlrd.open_workbook(file_name)
    table = data.sheets()[0]  # 通过索引顺序获取
    for i in xrange(3, table.nrows):
        if table.row_values(i)[key_column_num] in dict_account:
            print dict_account[table.row_values(i)[key_column_num]]
        else:
            print "XXX"


if __name__ == "__main__":
    dict_account = get_data_from_file("2.xlsx", 1, 3)
    match("1.xls", 2, dict_account)
