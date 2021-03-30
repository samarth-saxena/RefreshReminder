# # Move mouse pointer to given coordinates -------------------------------------
# import pyautogui
# print(pyautogui.position())
# pyautogui.moveTo(100, 100, duration = 1)

# #Print mouse coordinates -----------------------------------------------------
# import pyautogui, sys
# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')

# #If pc idle, same no. gets printed, else different----------------------------
# import time
# import win32api
# for i in range(10):
#    print(win32api.GetLastInputInfo())
#    time.sleep(1)


# Print idle time ---------------------------------------------------------------
import time
import threading
from ctypes import Structure, windll, c_uint, sizeof, byref
import windows
import cv2

import numpy as np
import dlib
from math import hypot


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

		inp = cv2.VideoCapture(0)
		storeData = 0

		font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

		while True:
			_, frame = inp.read()

			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			facialScan = getFace.detectMultiScale(gray, 1.1, 4)

			for (x, y, w, h) in facialScan:
				if (w*h > 3000):
					if storeData == 0:
						storeData = w * h

					# print(w*h)

					if w * h > 2 * storeData:
						cv2.putText(frame, 'Too Close!', (x - 3, y - 3), font, 1, (255, 255, 255), 2)
						cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
					# else:
					# 	cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

			cv2.imshow('ComputerVision', frame)
			key = cv2.waitKey(1)
			if (key != -1):
				break

		inp.release()

class eyeBlink (threading.Thread):

	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter

	def run(self):
		cap = cv2.VideoCapture(0)

		#finding approx eye points, see "landmarks_points.png" for ref.
		detector = dlib.get_frontal_face_detector()
		predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

		def midpoint(p1 ,p2):
			return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

		font = cv2.FONT_HERSHEY_TRIPLEX

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
					cv2.putText(eyeFrame, "BLINKING", (75, 150), font, 6, (0, 0, 255)) #remove after integration with UI


			cv2.imshow("eyeFrame", eyeFrame)

			# Esc key for Exit
			key = cv2.waitKey(1)
			if key == 27: 
				break

		cap.release()
		cv2.destroyAllWindows()


def main():
	windows.createMainWindow()
	
	# thread1 = faceDistance(1, "Thread-1", 1)
	thread2 = eyeBlink(2, "Thread-2", 2)

	# Start new Threads
	# thread1.start()
	thread2.start()

	try:
		work = 0
		while True:
			temp = get_idle_duration()
			if (temp<5):
				work+=1
			else:
				work=0
			print(temp)
			print(work)
			print()
			if(work>10):
				windows.createRefreshWin()
				work=0
			time.sleep(1)

	except KeyboardInterrupt:
		print('\n')

if __name__=="__main__":
	main()