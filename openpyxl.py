# coding=utf-8

from openpyxl import workbook
wb = load_workbook(filename = 'abc.xlsx')
sheet_ranges = wb['range names']
print(sheet_ranges['A1'].value)