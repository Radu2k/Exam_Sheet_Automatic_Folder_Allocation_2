import os
import shutil
from pdf2image import convert_from_path

# Move a file by renaming it's path
#os.rename('/Users/billy/d1/xfile.txt', '/Users/billy/d2/xfile.txt')

# Move a file from the directory d1 to d2
#shutil.move('/Users/billy/d1/xfile.txt', '/Users/billy/d2/xfile.txt')

def createDir(path):
    # define the access rights
    access_rights = 0o755
    # Check if dst path exists
    if os.path.isdir(path) == False:
        try:
            os.makedirs(path,access_rights)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)
    else:
        print("Directory %s already exists" % path)

def save( dstDir, page,index):
    try:
           page.save(dstDir+'page%d.png'%index,'PNG');
    except OSError:
            print("Creation of the file out%d.png failed" % index)
    else:
            print("Successfully created the file page%d.png" % index)

def move( dstDir,path,index):
    i=index
    #for i in range(startImgIndex,endImgIndex):
        # Move the file to 1path11
    print("path:",path)
    if os.path.isfile(dstDir+'/out%d.png'%i) == False:
        try:
            shutil.move(path+'/out%d.png'%i, dstDir)
        except OSError:
            print("Moving the file out%d.png failed, check if it already exists in the folder",dstDir % i)
        else:
            print("Successfully moved the file out%d.png" % i)
    else:
        print("File out%d.png already exists" % i)

def remove(path):
    if os.path.isfile(path) == True:
        try:
            os.remove(path)
        except OSError:
            print("Removing the", path,"failed")

