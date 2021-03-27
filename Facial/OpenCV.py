import cv2

getFace = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

inp = cv2.VideoCapture(0)
storeData = 0;

font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

while True:
    _, frame = inp.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    facialScan = getFace.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in facialScan:
        if storeData == 0:
            storeData = w * h

        if w * h > 2 * storeData:
            cv2.putText(frame, 'Too Close!', (x - 3, y - 3), font, 1, (255, 255, 255), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        else:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('bruh', frame)
    key = cv2.waitKey(1)
    if (key != -1):
        break

inp.release()