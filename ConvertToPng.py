from pdf2image import convert_from_path

def getPdfPages(pdfPath):
    pages = convert_from_path(pdfPath, 500)
    return len(pages)

def convertToPng(pdfPath,indexx):
    pages = convert_from_path(pdfPath, 500)
    return



