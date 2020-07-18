import cv2
import pytesseract


def cropImg(x,w,y,h,img):
    crop_img = img[y:y+h,x:x+w]
    return crop_img


def checkImg(img):
    # For Windows
    # pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
    # TESSDATA_PREFIX = 'C:/Program Files (x86)/Tesseract-OCR'

    #img=cv2.imread(img)

    croped_img=cropImg(2822,1259,45,791,img)

    text = pytesseract.image_to_string(croped_img)

    if ("Loughborough" in text) and ("University" in text):
        return 1
    else:
        return -1


#Check 2 pixels color range
'''
from PIL import Image
import ConvertToPng

pink_pages=0
for i in range(0,len(ConvertToPng.pages)):
    im = Image.open('/home/alien/PycharmProjects/untitled/IMG/out%d.png'%(i)) # Can be many different formats.
    pix = im.load()
    print (im.size ) # Get the width and hight of the image for iterating over

    check_left_top_corner =  False
    check_right_bootom_corner = False

    r,g,b=pix[500,2000]
    if r<255 and g<250 and b<250 :
        check_left_top_corner=True

    r,g,b=pix[1000,5700]
    if r<255 and g<250 and b<250 :
        check_right_bootom_corner=True
    if check_left_top_corner==True and check_right_bootom_corner==True:
        pink_pages+=1

print(pink_pages)


'''


