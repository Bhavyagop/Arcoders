from openpyxl import load_workbook, workbook

wb = load_workbook(filename = 'hackathon.xlsx')

sheet_ranges = wb['range names']

sheet  = wb.active()