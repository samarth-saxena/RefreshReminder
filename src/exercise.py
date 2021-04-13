import cv2
import numpy as np
import imageio
# from skimage.transform import resize
import winsound

# exc 1 -> Head Tilt | 2 -> Neck Elongates | 3 -> Demo Only

def exerciseAnimation():
    getFace = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    getEye = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
    getleftEye = cv2.CascadeClassifier('haarcascades/haarcascade_lefteye_2splits.xml')
    getrghtEye = cv2.CascadeClassifier('haarcascades/haarcascade_righteye_2splits.xml')

    inp = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    storeData = 0
    inpWid  = inp.get(cv2.CAP_PROP_FRAME_WIDTH)
    inpHig = inp.get(cv2.CAP_PROP_FRAME_HEIGHT)

    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    fx, fy, fw, fh = 0, 0, 0, 0
    leftist=3
    rightist=3
    exc=0
    top=3
    exerciseSettings=200

    xface1="../Assets/xr1.gif"
    gif1 = imageio.mimread(xface1)
    nums1 = len(gif1)
    imgs1 = [cv2.cvtColor(img1, cv2.COLOR_RGB2BGR) for img1 in gif1]
    i1 = 0
    FPS1=0

    xface2="../Assets/xr2.gif"
    gif2 = imageio.mimread(xface2)
    nums2 = len(gif2)
    imgs2 = [cv2.cvtColor(img2, cv2.COLOR_RGB2BGR) for img2 in gif2]
    i2 = 0
    FPS2=0

    xface3="../Assets/xr3.gif"
    gif3 = imageio.mimread(xface3)
    nums3 = len(gif3)
    imgs3 = [cv2.cvtColor(img3, cv2.COLOR_RGB2BGR) for img3 in gif3]
    i3 = 0
    FPS3=0

    alpha_blink=[0.1,0.12,0.15,0.2,0.3,0.4,0.45,0.5,0.4,0.3,0.2,0.15,0.12,0.1,0.01]
    alphpnt=0
    while True:
        _, frame = inp.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        facialScan = getFace.detectMultiScale(gray, 1.1, 4)
        eyescan = getEye.detectMultiScale(gray, 1.1, 4)
        leftscan = getleftEye.detectMultiScale(gray, 1.1, 4)
        rghtscan = getrghtEye.detectMultiScale(gray, 1.1, 4)
        # frame=cv2.flip(frame,1)
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

            iNum=iNum+1


        if(exc==0):

            # if ((alphpnt + 1) % alpha_blink.__len__()==0 and (leftist>0 or rightist>0)):
            #     winsound.PlaySound('../Assets/radar.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
            alphpnt = (alphpnt + 1) % alpha_blink.__len__()

            FPS1 = FPS1 + 1
            if (FPS1 > 6):
                FPS1 = 0
                i1 = (i1 + 1) % nums1
            imgs1[i1] = cv2.resize(imgs1[i1], (120, 120))

            x_offset = int((inpWid - imgs1[i1].shape[0]) / 2)
            y_offset = int(inpHig - imgs1[i1].shape[1])
            frame[y_offset:y_offset + imgs1[i1].shape[0], x_offset:x_offset + imgs1[i1].shape[1]] = imgs1[i1]

            if (fx, fy, fw, fh > 0 ):
                if (iNum > 1 and (leftist>0 or rightist>0)):
                    if (fy < eyes[5] < fy + fh):
                        if (fx + exerciseSettings < eyes[4] < fx + fw + exerciseSettings):
                            leftist=-3
                        if (fx - exerciseSettings < eyes[4] < fx + fw - exerciseSettings):
                            rightist=-3
                if(leftist>0):
                    overlay = frame.copy()
                    cv2.rectangle(overlay, (fx + exerciseSettings, fy), (fx + fw + exerciseSettings, fy + fh), (10,255,10), -1)
                    # cv2.rectangle(overlay, (420, 205), (595, 385), (0, 0, 255), -1)
                    cv2.addWeighted(overlay, alpha_blink[alphpnt], frame, 1 - alpha_blink[alphpnt], 0, frame)

                if(rightist>0):
                    overlay = frame.copy()
                    cv2.rectangle(overlay, (fx - exerciseSettings, fy), (fx + fw - exerciseSettings, fy + fh), (10,255,10), -1)
                    # cv2.rectangle(overlay, (420, 205), (595, 385), (0, 0, 255), -1)
                    cv2.addWeighted(overlay, alpha_blink[alphpnt], frame, 1 - alpha_blink[alphpnt], 0, frame)

                if (rightist<0 and leftist<0):
                    leftist,rightist=0,0
                    winsound.PlaySound('../Assets/succ1.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)


        elif(exc==1):
            FPS2 = FPS2 + 1
            if (FPS2 > 2):
                FPS2 = 0
                i2 = (i2 + 1) % nums2
            imgs2[i2] = cv2.resize(imgs2[i2], (120, 120))
            x_offset = int((inpWid - imgs2[i2].shape[0]) / 2)
            y_offset = int(inpHig - imgs2[i2].shape[1])
            frame[y_offset:y_offset + imgs2[i2].shape[0], x_offset:x_offset + imgs2[i2].shape[1]] = imgs2[i2]

            if (fx, fy, fw, fh > 0):
                if (iNum > 1 and top>0):
                    if (fx < eyes[4] < fx + fw):
                        if (fy - exerciseSettings < eyes[5] < fy + fh - exerciseSettings):
                            top=-3

                if(top>0):
                    overlay=frame.copy()
                    cv2.rectangle(overlay, (fx , fy-exerciseSettings), (fx + fw, fy + fh - exerciseSettings), (10,255,10), -1)
                    # cv2.rectangle(overlay, (420, 205), (595, 385), (0, 0, 255), -1)
                    alphpnt=(alphpnt + 1) % alpha_blink.__len__()
                    cv2.addWeighted(overlay, alpha_blink[alphpnt], frame, 1 - alpha_blink[alphpnt],0, frame)

                if(top<0):
                    top=0
                    winsound.PlaySound('../Assets/succ1.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)


        elif(exc==2):
            FPS3 = FPS3 + 1
            if (FPS3 > 3):
                FPS3 = 0
                i3 = (i3 + 1) % nums3
            imgs3[i3] = cv2.resize(imgs3[i3], (120, 120))

            x_offset = int((inpWid - imgs3[i3].shape[0]) / 2)
            y_offset = int(inpHig - imgs3[i3].shape[1])
            frame[y_offset:y_offset + imgs3[i3].shape[0], x_offset:x_offset + imgs3[i3].shape[1]] = imgs3[i3]


        cv2.imshow('ComputerVision', frame)
        key = cv2.waitKey(1)
        if(key == 32): # key (SPACE_BAR) -> Exercise Reset
            leftist=3
            rightist=3
            storeData = 0
            top=3
        elif(key == 99): # key (c) -> Exercise Change (rotate)
            exc=exc+1
            exc=exc%3
            leftist = 3
            rightist = 3
            storeData = 0
            top = 3
        elif (key == 100): # key (d) -> Exercise Complete
            leftist=-3
            rightist=-3
            top=-3
        elif (key != -1):
            break

    cv2.destroyAllWindows()
    inp.release()
