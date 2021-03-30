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
from ctypes import Structure, windll, c_uint, sizeof, byref
import windows
import cv2


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

def main():
	windows.createMainWindow()
	
	getFace = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
	inp = cv2.VideoCapture(0)
	storeData = 0
	font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
	
	try:
		work = 0
		while True:
			_, frame = inp.read()
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			facialScan = getFace.detectMultiScale(gray, 1.1, 4)

			for (x, y, w, h) in facialScan:
				if (w*h > 3000):
					if storeData == 0:
						storeData = w * h
					# print(w*h)
					if w * h > 6/5 * storeData:
						cv2.putText(frame, 'Too Close!', (x - 3, y - 3), font, 1, (255, 255, 255), 2)
						cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
						windows.createPostureWin()
					# else:
					# 	cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

			cv2.imshow('ComputerVision', frame)
			key = cv2.waitKey(1)


			# temp = get_idle_duration()
			# if (temp<5):
			# 	work+=1
			# else:
			# 	work=0
			# print(temp)
			# print(work)
			# print()
			# if(work>10):
			# 	windows.createRefreshWin()
			# 	work=0
			# time.sleep(1)
		inp.release()

	except KeyboardInterrupt:
		print('\n')

if __name__=="__main__":
	main()