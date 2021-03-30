from cv2 import cv2
import numpy as np
import dlib
from math import hypot

cap = cv2.VideoCapture(0)

#finding approx eye points, see "landmarks_points.png" for ref.
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def midpoint(p1 ,p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

font = cv2.FONT_HERSHEY_COMPLEX

#returns blink ratio for specific eye
def get_BlinkRatio(eye_points, facial_landmarks):
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))

    hor_line_lenght = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    ver_line_lenght = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

    ratio = hor_line_lenght / ver_line_lenght
    return ratio

while True:
    _, eyeFrame = cap.read()
    eyeFrame = cv2.flip(eyeFrame,1)
    gray = cv2.cvtColor(eyeFrame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:
        landmarks = predictor(gray, face)

        LeftEye_ratio = get_BlinkRatio([36, 37, 38, 39, 40, 41], landmarks)
        RightEye_ratio = get_BlinkRatio([42, 43, 44, 45, 46, 47], landmarks)

        # use BlinkRatio for Results
        BlinkRatio = (LeftEye_ratio + RightEye_ratio) / 2 

        if BlinkRatio > 3.7:
            # means Eye is closed
            cv2.putText(eyeFrame, "BLINKING", (75, 150), font, 6, (0, 255, 255)) #remove after integration with UI


    cv2.imshow("eyeFrame", eyeFrame)

    # Esc key for Exit
    key = cv2.waitKey(1)
    if key == 27: 
        break

cap.release()
cv2.destroyAllWindows()