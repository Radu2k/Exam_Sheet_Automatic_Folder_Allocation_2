# Reading an excel file using Python
import xlrd
import os

loc=""

def setLocationOfExcel(pathToFOLDER):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(pathToFOLDER):
        for file in f:
            if '.xlsx' in file:
                files.append(os.path.join(r, file))

    excelName = files[0]
    global loc
    loc = str(excelName)
    # Give the location of the file



def getStudentIds():
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    nr=[]
    for i in range(1,sheet.nrows):
        nr.append(sheet.cell_value(i,0))

    return nr

def checkExcel(predictedNr):
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    nr=getStudentIds()

    index_predicted=0
    index_matches=0

    for i in range(0, len(nr)):
        x=0
        copy_mpnr = predictedNr
        for j in range(len(nr[i])-1,1,-1):
            print(int(nr[i][j]),'~',(copy_mpnr % 10))
            if(int(nr[i][j])==copy_mpnr%10):
                x+=1
            copy_mpnr=int(copy_mpnr/10)

        if x>index_matches:
            index_predicted=i+1
            index_matches=x
        print('x:',x)


    return(sheet.cell_value(index_predicted,0))