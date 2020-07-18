import ImageToText
import VerifyPinkPages
import FolderAllocation
import ExcelReader
import os
import cv2
from pdf2image import convert_from_path

#PATH TO FOLDER WITH PDF AND EXCEL
pathToFOLDER="/home/alien/PycharmProjects/untitled"

######################################################################################################
files = []

# r=root, d=directories, f = files
for r, d, f in os.walk(pathToFOLDER):
    for file in f:
        if '.pdf' in file:
            files.append(os.path.join(r, file))
pdfPath=files[0]

pages = convert_from_path(pdfPath, 500)

ExcelReader.setLocationOfExcel(pathToFOLDER)
studentIdExcel = ExcelReader.getStudentIds()

def matchStudentNr(predictedNr):
    index_predicted = 0
    index_matches = 0

    for i in range(0, len(studentIdExcel)):
        x = 0
        copy_mpnr = predictedNr
        for j in range(len(studentIdExcel[i])-1,0,-1):
            print(int(studentIdExcel[i][j]),'~',(copy_mpnr % 10))
            if(int(studentIdExcel[i][j])==copy_mpnr%10):
                x += 1
            copy_mpnr =int(copy_mpnr/10)

        if x > index_matches:
            index_predicted = i
            index_matches = x
        print('x:', x)

    return studentIdExcel[index_predicted], index_matches

studentNr = ""
for i in range(len(pages)):
    page = pages[i]
    j = i+1
    page.save(pathToFOLDER+'/out%d.png'%j,'PNG')
    img = cv2.imread(pathToFOLDER+'/out%d.png'%j)

    if VerifyPinkPages.checkImg(img)==1 :
        predictNr = ImageToText.cutDigits(pathToFOLDER, img)
        print(predictNr)
        studentNr, matches = matchStudentNr(predictNr)
        print(studentNr, matches)
        if matches > 4:
            FolderAllocation.createDir(pathToFOLDER+"/%s" % str(studentNr))
            FolderAllocation.move(pathToFOLDER + "/%s" % str(studentNr), pathToFOLDER, j)
            FolderAllocation.remove(pathToFOLDER+'/out%d.png' % j)
        else:
            studentNr = ""
            FolderAllocation.createDir(pathToFOLDER + "/unsure_about_this_ones")
            FolderAllocation.move(pathToFOLDER + "/unsure_about_this_ones", pathToFOLDER, j)
            FolderAllocation.remove(pathToFOLDER + '/out%d.png' % j)

    else:
        if studentNr != "":
            FolderAllocation.move(pathToFOLDER + "/%s" % str(studentNr), pathToFOLDER, j)
            FolderAllocation.remove(pathToFOLDER + '/out%d.png' % j)
        else:
            FolderAllocation.move(pathToFOLDER + "/unsure_about_this_ones", pathToFOLDER, j)
            FolderAllocation.remove(pathToFOLDER + '/out%d.png' % j)
