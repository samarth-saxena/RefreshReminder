import cv2
import numpy as np
import dlib
from math import hypot
		
def startOCVTest():		
	getFace = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

	inp = cv2.VideoCapture(0,cv2.CAP_DSHOW)
	storeData = 0

	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

	def midpoint(p1 ,p2):
		return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

	font = cv2.FONT_HERSHEY_DUPLEX

	def get_BlinkRatio(eye_points, facial_landmarks):
		left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
		right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
		center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
		center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))

		hor_line_lenght = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
		ver_line_lenght = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

		ratio = hor_line_lenght / ver_line_lenght
		return ratio

	while (True):
		_, frame = inp.read()

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		facialScan = getFace.detectMultiScale(gray, 1.1, 4)

		frame = cv2.flip(frame,1)
		faces = detector(gray)

		for (x, y, w, h) in facialScan:
			if (w*h > 3000):
				if storeData == 0:
					storeData = w * h

				if w * h > 2 * storeData: #6/5
					# if(winNotif):
					# 	windowsNotification("You are sitting too close!!", 10)
					# else:						
					# 	MainWindow.launchPostureFrame()
						# c.createPostureFrame.emit()

					cv2.putText(frame, 'Too Close!', (x - 3, y - 3), font, 1, (255, 255, 255), 2)
					cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
				else:
					# if(winNotif == False):
					# 	MainWindow.hidePostureFrame()
					cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

		for face in faces:
			landmarks = predictor(gray, face)

			LeftEye_ratio = get_BlinkRatio([36, 37, 38, 39, 40, 41], landmarks)
			RightEye_ratio = get_BlinkRatio([42, 43, 44, 45, 46, 47], landmarks)

			# use BlinkRatio for Results
			BlinkRatio = (LeftEye_ratio + RightEye_ratio) / 2

			if BlinkRatio > 3.7:
				# means Eye is closed
				cv2.putText(frame, "BLINKING", (75, 150), font, 6, (0, 0, 255)) #remove after integration with UI


		cv2.imshow('ComputerVision', frame)
		key = cv2.waitKey(1)
		if (key != -1):
			# c.exitApp.emit()
			break

	inp.release()
	cv2.destroyAllWindows()