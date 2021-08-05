import os
from datetime import datetime

import cv2
import face_recognition
import numpy as np

#variables and list needed
path = 'train_images'
images = []
Names = []
myList = os.listdir(path)
#print(myList)

#Function to read the images from local drive
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    Names.append(os.path.splitext(cl)[0])
#print(Names)

#function to find the Image Encoding
def findEncodings(images):
    encodeList = []
    for im in images:
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(im)[0]
        encodeList.append(encode)
    return encodeList

#Once face recognised save name and time of entry to a csv file
def savelist(name):
    with open('recognition_list.csv','r+') as f:
        myDataList = f.readlines()
        nameList =[]
        for line in myDataList:
            entry = line.strip().split(',')
            nameList.append(entry[0])
        print(nameList)
        if name not in nameList:
            now = datetime.now()
            dt_string = now.strftime('%I:%M:%S')
            f.writelines(f'\n{name},{dt_string}')


encodeListKnow = findEncodings(images)
print("Encoding Completed")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#image reading and encoding and recognition
while True:
    success, img = cap.read()
    ims = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    ims = cv2.cvtColor(ims, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(ims)
    encodesCurFrame = face_recognition.face_encodings(ims, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnow, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnow, encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = Names[matchIndex].upper()
            #print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            savelist(name)


#open the camera and capture images
    cv2.imshow('camera', img)
    cv2.waitKey(1)