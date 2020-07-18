import numpy as np
from PIL import Image,ImageFilter
from matplotlib import pyplot as plt
from keras.models import load_model
import cv2

def predictDigit(pathToFOLDER,im):
    model = load_model(pathToFOLDER + "/MobileNet.h5")

    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(im)

    #for i in range(1,7):
    #img = Image.open('/home/alien/PycharmProjects/untitled/%d.png' % (i), 'r')

    img = img.filter(ImageFilter.GaussianBlur(radius=0))
    img = img.resize((28, 28), Image.LANCZOS)

    img = img.filter(ImageFilter.SHARPEN);
    img = img.convert('L')

    plt.imshow(img)
    plt.show()

    # convert rgb to grayscale
    img = img.convert('L')
    img = np.array(img)

    # reshaping to support our model input and normalizing
    img = img.reshape(1, 28, 28, 1)
    img = img / 255.0

    # predicting the class
    res = model.predict([img])[0]

    digit, acc = np.argmax(res), max(res)
    print('*-' + str(digit) + '-* , ' + str(int(acc * 100)) + '%')

    return digit