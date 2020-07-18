import pytesseract
from PIL import Image
import cv2
import numpy as np
from matplotlib import pyplot as plt
import PredictDigit

def printImgDimensions(img):
    dimensions = img.shape

    height = img.shape[0]
    width = img.shape[1]
    channels = img.shape[2]

    print('Image Dimension    : ', dimensions)
    print('Image Height       : ', height)
    print('Image Width        : ', width)
    print('Number of Channels : ', channels)

def cropImg(x,w,y,h,img):
    crop_img = img[y:y+h,x:x+w]
    return crop_img

def cutDigits(pathToFOLDER,img):
    #img = cv2.imread(img)#'/home/alien/PycharmProjects/untitled/IMG/out%d.png'%i)

    croped_img=cropImg(1244,927,1258,160,img)
    #cv2.imwrite('RegistrationNR.png', croped_img )

    median = cv2.medianBlur(croped_img,5)
    plt.imshow(median)
    plt.show()#1

    gray = cv2.cvtColor(croped_img, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    blur = cv2.GaussianBlur(blackAndWhiteImage,(5,5),0)

    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    ret4,th4 = cv2.threshold(th3,0,255,cv2.THRESH_BINARY_INV)

    #print ("Threshold selected : ", ret3)
    #print ("Threshold selected : ", ret4)

    #output = pytesseract.image_to_string(th3, lang='eng')
    #print (output)

    #cv2.imwrite('out_gauss_otsu.png',th3)
    #cv2.imwrite('out_gauss_otsu_INVERTED.png',th4)
    ###################################################################################################################################
    img = th3 #cv2.imread('/home/alien/PycharmProjects/untitled/out_gauss_otsu.png',0)

    img = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)

    ###########################Text Line Extraction############################################

    plt.imshow(img)
    #plt.show()#1

    plt.imshow(img,cmap = 'gray')
    #plt.show()#2

    bimg=cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
    #print(bimg.shape)

    #print(bimg[:,:,0]==bimg[:,:,1])

    (bimg[:,:,0]==bimg[:,:,1]).all()


    ###########################Remove dotted line##############################################
    NoColumns=bimg.shape[1]
    #print(NoColumns)

    NoRows=bimg.shape[0]
    #print(NoRows)

    hsum=np.sum(((255-bimg)/255)[:,:,0],axis=1)

    hsum.astype(float)
    maxi=hsum.max();
    #print( maxi)
    for i in range(len(hsum)):
       if maxi==hsum[i]:
           index=i
    #print(index,"index")

    for i in range(131,NoRows):
       for j in range(NoColumns):
        cv2.circle(bimg,(j,i),1,(255,255,255),-1)


    ###########################CHECK IF ARE MORE WRITTEN LINES IN IMAGE#########################
    bimgo = bimg.copy()
    #print(bimg[:,:,0])

    nbimg=255-bimg
    #print(nbimg[:,:,0])

    plt.imshow(nbimg)
    #plt.show()#3

    np.unique(nbimg)
    nbimg=nbimg/255

    np.unique(nbimg)

    NoRows=nbimg.shape[0]
    #print(NoRows)

    #SEE WHERE ARE LINES WITH WORDS (NO USE IN OUR CASE, BECAUSE WE GIVE IT ONLY ONE LINE, WITH STUDENT NUMBER)
    for i in range(NoRows):
        summ=np.sum(nbimg[i,:,0])
        cv2.circle(bimg,(int(summ),i),2,255,-1)

    plt.imshow(bimg)
    #plt.show()#4

    #MAKE PLOTS BASED ON WHERE ARE WRITTEN LINES IN IMAGE
    hsum=np.sum(nbimg[:,:,0],axis=1)
    #print('hsum shape:', hsum.shape)


    plt.plot(hsum)
    #plt.show()#5


    plt.plot(np.diff(hsum))
    #plt.show()#6


    dif= np.diff(hsum.astype(float))
    plt.plot(dif)
    #plt.show()#7


    #print(hsum)
    #print('hsum:',hsum>0)

    hsum[hsum>0]=1
    #print(hsum)
    #MAKE PLOT BASED ON WHERE WRITTEN LINES START AND END  (USES N'TH DISCRETE DIFF)
    hdif=np.diff(hsum.astype(float))
    #print('hdif:',hdif)

    plt.plot(hdif)
    #plt.show()#8

    #SEPARATE LINES | FRAMING THE LINES
    UL=np.where(hdif>0)
    LL=np.where(hdif<0)

    #print(UL)
    #print(LL)

    UL=np.where(hdif>0)[0]
    LL=np.where(hdif<0)[0]

    #print('UL:',UL)
    #print('LL:',LL)

    images=[]
    nbimages=[]
    for ix in range (len(UL)):
        plt.figure()
        #images.append(bimgo[:,:])
        #nbimages.append(nbimg[:,:])

        #FOR CUTTING HEIGHT OF IMAGE
        #images.append(bimgo[UL[ix]-50:LL[ix]+50,:])
        #nbimages.append(nbimg[UL[ix]-50:LL[ix]+50:,:])

        images.append(bimgo[UL[ix]:LL[ix]+20,:])
        nbimages.append(nbimg[UL[ix]:LL[ix]+20,:])

        plt.imshow(images[ix])
        #plt.show()


    vsum = np.sum(nbimages[0],axis=0)
    #print("vsum",vsum)
    ###################CALCULATE WHERE THE DIGITS AND CHARACTERS ARE IN IMAGES###################
    #######
    # CHOOSE WHERE THE DIGITS/CHARACTERS ARE BASED ON WHERE ARE SPACES IN THE FIRST
    # HALF OF THE IMAGE(BECAUSE AS AN EXAMPLE THE LINE FROM BELOW 2 CAN NOT GET SEPARATE BY
    # THE FIRST PART OF THE 9 AND CAN BE CONFUSED AND CUT AS ONE DIGIT)
    #######
    vsum=np.sum(nbimages[0][:,:,0],axis=0)
    vsum[vsum>0]=1
    vdif=np.diff(vsum.astype(float))

    #print(vdif)

    plt.plot(vdif)
    #plt.show()

    RL=np.where(vdif>0)[0]
    LL=np.where(vdif<0)[0]

    #print('RL',RL)
    #print('LL',LL)

    vsum1=np.sum(nbimages[0][:int(NoRows/2),:,0],axis=0)
    vsum1[vsum1>0]=1
    vdif1=np.diff(vsum1.astype(float))

    #print(vdif1)

    plt.plot(vdif1)
    #plt.show()

    RL1=np.where(vdif1>0)[0]
    LL1=np.where(vdif1<0)[0]

    #print('RL1',RL1)
    #print('LL1',LL1)

    if len(RL1)==7 and len(RL)!=7:
        RL=RL1
        LL=LL1

    results=[]

    nr=0
    for ix in range(len(RL)):
        plt.figure()
        i=int(ix)
        #print ('ix: '+str(ix))

        if i>0 and i<(len(RL)-1):
            cimgI= images[0][:,RL[ix]-int((RL[ix]-LL[ix-1])):LL[ix]+int((RL[ix+1]-LL[ix]))]
            NoRows=cimgI.shape[0]
            NoColumns=cimgI.shape[1]
            for k in range(int(4/5*(RL[ix]-LL[ix-1]))):
                for l in range(NoRows):
                    cv2.circle(cimgI, (k, l), 1, (255,255,255), -1)
            for k in range(NoColumns-int(4/5*(RL[ix+1]-LL[ix])),NoColumns):
                for l in range(NoRows):
                    cv2.circle(cimgI, (k, l), 1, (255,255,255), -1)
        elif i==0:
            cimgI= images[0][:,:LL[ix]+int(1*(RL[ix+1]-LL[ix])/2)]
        elif i==(len(RL)-1):
            cimgI= images[0][:,RL[ix]-int(1*(RL[ix]-LL[ix-1])/2):LL[ix]+50]


        results.append(cimgI)

        #print('Original Dimensions : ', cimgI.shape)

        gray2 = cv2.cvtColor(cimgI, cv2.COLOR_BGR2GRAY)
        (thresh, blackAndWhiteImage2) = cv2.threshold(gray2, 127, 255, cv2.THRESH_BINARY)
        # blur2 = cv2.GaussianBlur(blackAndWhiteImage2, (5, 5), 0)

        ret4, th4 = cv2.threshold(cv2.threshold(blackAndWhiteImage2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1], 0, 255,
                              cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        ret4, th4 = cv2.threshold(th4, 0, 255, cv2.THRESH_BINARY_INV)

        plt.imshow(th4)
        #plt.show()
        if ix>0:
            nr=(nr*10)+PredictDigit.predictDigit(pathToFOLDER,th4)
        #cv2.imwrite('/home/alien/PycharmProjects/untitled/%d.png'%(i), th4)
    return nr

