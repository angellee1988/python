#!/usr/bin/python3

import xlrd


def test_xlrd_on_demand_false():
    # f = xlrd.open_workbook('test_cases\\read_xls.xls', on_demand=False)
    f = xlrd.open_workbook('test_cases\\read_xlsx.xlsx', on_demand=False)


def test_xlrd_on_demand_true():
    # f = xlrd.open_workbook('test_cases\\read_xls.xls', on_demand=True)
    f = xlrd.open_workbook('test_cases\\read_xlsx.xlsx', on_demand=True)
    f.sheet_by_index(0)
