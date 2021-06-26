import os
import cv2
import face_recognition
from time import sleep

path = 'porProcesar/'
i= len(os.listdir(path))
cap=cv2.VideoCapture(0)

while True:
    _,img = cap.read()
    face_locations = face_recognition.face_locations(img)
    if(len(face_locations)==0):
        print("No hay nada")
    else:
        print(face_locations)
        for (top, right, bottom, left) in face_locations:
            imgrecortada=img[top-20:bottom+20,left-20:right+20]
            i=i+1
        cv2.imwrite(os.path.join(path, 'cara' + str(i + 1) + '.jpg'), imgrecortada)
    sleep(5)
