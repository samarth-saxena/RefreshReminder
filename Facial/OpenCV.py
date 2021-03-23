import cv2
import numpy

inp= cv2.VideoCapture(0)


while True:
    _, frame = inp.read()
    cv2.imshow('Test Screen!', frame)
    key=cv2.waitKey(1)
    if key!=-1:
        break
