# import openpyxl
import xlsxwriter

# Create an new Excel file and add a worksheet
workbook = xlsxwriter.Workbook('dem.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hello')
worksheet.write('A2', 'Hello')
worksheet.write('A3', 'Hello')
worksheet.write('A4', 'Hello')
worksheet.write('A5', 'Hello')
worksheet.write('B1', 'Hello')
worksheet.write('B2', 'Hello')
worksheet.write('B3', 'Hello')
worksheet.write('B4', 'Hello')
worksheet.write('B5', 'Hello')
worksheet.write('C1', 'Hello')
worksheet.write('C2', 'Hello')
worksheet.write('C3', 'Hello')
worksheet.write('C4', 'Hello')
worksheet.write('C5', 'Hello')

workbook.close()



# wb = openpyxl.load_workbook(filename = 'demo.xlsx')
# sheet = wb['test']
# sheet['B1'] = val