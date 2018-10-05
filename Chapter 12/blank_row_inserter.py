#! python3
# blank_row_inserter.py - Takes two integers n and m and a filename string as
# command line arguments. The program will insert m blank rows starting at row n
# and save the spreadsheet as a new file

import sys, openpyxl, os

n = int(sys.argv[1])
m = int(sys.argv[2])
filename = sys.argv[3]

wb = openpyxl.load_workbook(filename)
sheet = wb.active
new_wb = openpyxl.Workbook()
new_sheet = new_wb.active

for r in range(1, sheet.max_row + 1):
    for c in range(1, sheet.max_column + 1):
        if r < n:
            new_sheet.cell(row=r, column=c).value = sheet.cell(row=r, column=c).value
        else:
            new_sheet.cell(row=r+m, column=c).value = sheet.cell(row=r, column=c).value
            
new_wb.save(f'{os.path.splitext(filename)[0]}_blank.xlsx')
print(f'{os.path.splitext(filename)[0]}_blank.xlsx saved')
