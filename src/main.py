import time
import threading
from ctypes import Structure, windll, c_uint, sizeof, byref
import gui
import cv2

from win10toast import ToastNotifier

import numpy as np
import dlib
from math import hypot
from PyQt5.QtWidgets import QApplication
import sys


class LASTINPUTINFO(Structure):
	_fields_ = [
		('cbSize', c_uint),
		('dwTime', c_uint),
	]

def get_idle_duration():
	lastInputInfo = LASTINPUTINFO()
	lastInputInfo.cbSize = sizeof(lastInputInfo)
	windll.user32.GetLastInputInfo(byref(lastInputInfo))
	millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
	return millis / 1000.0

class faceDistance (threading.Thread):

	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter

	def run(self):
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
			
		while (gui.flag[0]):
			_, frame = inp.read()

			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			facialScan = getFace.detectMultiScale(gray, 1.1, 4)

			frame = cv2.flip(frame,1)
			faces = detector(gray)

			for (x, y, w, h) in facialScan:
				if (w*h > 3000):
					if storeData == 0:
						storeData = w * h

					# print(w*h)
						# win = windows.createPostureWin()

					if w * h > 2 * storeData: #6/5
						# win.showWin()
						# windows.createPostureWin()
						cv2.putText(frame, 'Too Close!', (x - 3, y - 3), font, 1, (255, 255, 255), 2)
						cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
					# else:
					# 	win.closeWin()
					# 	cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

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
				break

		inp.release()
		cv2.destroyAllWindows()


class screenUsage(threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter

	def run(self):
		try:
			# gui.launchBreakPopup()
			# print("Point 1")
			# popup = gui.breakPopup()
			# print("Point 2")
			# popup.show()
			# print("Point 3")
			# app.exec_()
			# print("Point 4")
			# global temp
			# temp = True

			# work = 0
			# while gui.flag[3]:
			# 	temp = get_idle_duration()
			# 	if (temp<5):
			# 		work+=1
			# 	else:
			# 		work=0
			# 	print(temp)
			# 	print(work)
			# 	print()
			# 	if(work>10):
			# 		# windows.createRefreshWin()
			# 		work=0
			# 	time.sleep(1)
			# 	if (gui.readytogo == False):
			# 		break

		except KeyboardInterrupt:
			sys.exit()

temp = False

# class guiThread(threading.Thread):
# 	def __init__(self, threadID, name, counter):
# 		threading.Thread.__init__(self)
# 		self.threadID = threadID
# 		self.name = name
# 		self.counter = counter
	
# 	def run(self):


if __name__=="__main__":
	app = QApplication(sys.argv)

	gui.launchMainWindow()
	# popup = gui.breakPopup()
	# gui.launchBreakPopup()

	# toaster = ToastNotifier()
	# toaster.show_toast("Refresh reminder","Take a break to refresh!",duration=10, threaded=True)

	app.exec_()

	TFaceDistance = faceDistance(1, "Thread-1", 1)
	TScreenUsage = screenUsage(2, "Thread-2", 2)


	if(gui.readytogo):
		if(gui.flag[0]):
			TFaceDistance.start()
		if(gui.flag[3]):
			TScreenUsage.start()
	try:
		while(True):
			if(temp):
				temp=False
				# popup.show()
			if(gui.readytogo == False):
				if(TFaceDistance.is_alive()):
					TFaceDistance.join()
				if(TScreenUsage.is_alive()):
					TScreenUsage.join()
				break
	except KeyboardInterrupt:
		sys.exit()

