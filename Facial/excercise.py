from __future__ import print_function
import cv2
import numpy as np
# import imageio


getFace = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
getEye = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
getleftEye = cv2.CascadeClassifier('haarcascades/haarcascade_lefteye_2splits.xml')
getrghtEye = cv2.CascadeClassifier('haarcascades/haarcascade_righteye_2splits.xml')

inp = cv2.VideoCapture(0)
storeData = 0

font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
fx, fy, fw, fh = 0, 0, 0, 0
leftist=3
rightist=3
exc=3
top=3

xface="./1Face.gif"

# gif = imageio.mimread(xface)
# nums = len(gif)
# print("Total {} frames in the gif!".format(nums))
# imgs = [cv2.cvtColor(img, cv2.COLOR_RGB2BGR) for img in gif]
# i = 0



while True:
    _, frame = inp.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    facialScan = getFace.detectMultiScale(gray, 1.1, 4)
    eyescan = getEye.detectMultiScale(gray, 1.1, 4)
    leftscan = getleftEye.detectMultiScale(gray, 1.1, 4)
    rghtscan = getrghtEye.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in facialScan:
        if (w * h > 3000):
            if storeData == 0:
                storeData = w * h
                fx, fy, fw, fh = x, y, w, h


    iNum = 0
    eyes = []
    for (x, y, w, h) in eyescan:
        if (iNum == 0):

            eyes.append(x)
            eyes.append(y)
            eyes.append(w)
            eyes.append(h)

        if (iNum == 1):

            eyes[0] = int((eyes[0] + x) / 2)
            eyes[1] = int((eyes[1] + y) / 2)
            eyes[2] = int((eyes[2] + w) / 2)
            eyes[3] = int((eyes[3] + h) / 2)
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (20, 12, 124), 2)
            eyes.append(int((eyes[0]+eyes[0]+eyes[2])/2))
            eyes.append(int((eyes[1] + eyes[1] + eyes[3]) / 2))
            cv2.rectangle(frame, (eyes[0], eyes[1]), (eyes[0] + eyes[2], eyes[1] + eyes[3]), (205, 254, 153), 2)
            cv2.circle(frame, (eyes[4], eyes[5]), 0, (205, 254, 153), 3)

        iNum=iNum+1;


    if(exc==3):
        if (fx, fy, fw, fh > 0):
            if (iNum > 1):
                if (fy < eyes[5] < fy + fh):
                    if (fx + 240 < eyes[4] < fx + fw + 240):
                        leftist=-3;
                    if (fx - 240 < eyes[4] < fx + fw - 240):
                        rightist=-3;
            if(leftist>0):
                cv2.rectangle(frame, (fx + 240, fy), (fx + fw + 240, fy + fh), (0, 255, 0), 2)
            if(rightist>0):
                cv2.rectangle(frame, (fx - 240, fy), (fx + fw - 240, fy + fh), (0, 255, 0), 2)

    elif(exc==-3):
        if (fx, fy, fw, fh > 0):
            if (iNum > 1):
                if (fx < eyes[4] < fx + fw):
                    if (fy - 240 < eyes[5] < fy + fh - 240):
                        top=-3;

            if(top>0):
                cv2.rectangle(frame, (fx , fy-240), (fx + fw, fy + fh - 240), (245, 45, 45), 2)

    # i = (i + 1) % nums
    # # if(imgs[i]!=None):
    # 
    # x_offset = y_offset = 100
    # # src = cv2.imread(imgs[i], 1)
    # # tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # # _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
    # # b, g, r = cv2.split(src)
    # # rgba = [b, g, r, alpha]
    # # imgs[i] = cv2.merge(rgba, 4)
    # frame[y_offset:y_offset+imgs[i].shape[0], x_offset:x_offset+imgs[i].shape[1]] = imgs[i]



    cv2.imshow('ComputerVision', frame)
    key = cv2.waitKey(1)
    if(key == 32):
        leftist=3
        rightist=3
        storeData = 0
        top=3;
    elif(key == 99):
        exc=-1*exc
        leftist = 3
        rightist = 3
        storeData = 0
        top = 3;
    elif (key != -1):
        break

cv2.destroyAllWindows()
inp.release()
