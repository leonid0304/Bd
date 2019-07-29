# import openpyxl
import xlsxwriter

A= [i+1 for i in range(5) ]
B= [i+6 for i in range(5) ]
C= [i+11 for i in range(5) ]
print B

A0=["A"+str(i+1) for i in range(5)]
B0=["B"+str(i+1) for i in range(5)]
C0=["C"+str(i+1) for i in range(5)]


# Create an new Excel file and add a worksheet
workbook = xlsxwriter.Workbook('demo1.xlsx')
worksheet = workbook.add_worksheet()

for i in range (5):
    worksheet.write(A0[i], A[i])
    worksheet.write(B0[i], B[i])
    worksheet.write(C0[i], C[i])


workbook.close()



# wb = openpyxl.load_workbook(filename = 'demo.xlsx')
# sheet = wb['test']
# sheet['B1'] = val