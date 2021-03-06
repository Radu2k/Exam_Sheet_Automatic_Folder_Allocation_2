# Exam_Sheet_Automatic_Folder_Allocation_2

Automatization of grading written exam papers, using Machine Learning, OpenCV and Matplotlib.
Developed a system that transform scanned exam papers from PDF to folders with images for each student, based on handwritten student number and grading.

First it will look for the pdf. Then using machine learning it will try and understand the student number in each pdf page (If there is one). After it will check and match the result with one from an excel file with all student numbers. Then it will create a folder with student ID for those that match more than 70% of digits, it will use the one that had the biggest match with what found in excel.
  
## Getting Started

Download the zip and extract it.

### Installing
I recommand to use linux and pip command.

Extract the MobileNet.zip and place scripts and .h5 file in the same folder.

Open the project in PyCharm and you will need to import the following:

* [Numpy](https://numpy.org/install/)
* [PIL](https://pillow.readthedocs.io/en/stable/installation.html)
* [Matplotlib](https://matplotlib.org/3.3.2/users/installing.html)
* [Keras](https://pypi.org/project/Keras/)
* [CV2](https://pypi.org/project/opencv-python/)
* [Pytesseract](https://pypi.org/project/pytesseract/)
* [OS]()
* [xlrd](https://pypi.org/project/xlrd/) - version 1.2.0
* [pdf2image](https://pypi.org/project/pdf2image/)
* [shutil](https://pypi.org/project/pytest-shutil/)

## Built With

* [Curt-Park handwritten_digit_recognition github](https://github.com/Curt-Park/handwritten_digit_recognition) - Used Curt-Park's pre-trained model.

## Authors

* **Radu-Constantin Salavat** - *Initial work* - [Radu2k](https://github.com/Radu2k)
* **Dr Firat Batmaz** - *Ideea, Inspiration and Documentation* - [Dr Firat Batmaz](https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/firat-batmaz/)

## Acknowledgments

* Hat tip to anyone whose code was used

