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
import firstWin

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

try:
	while True:
		temp = get_idle_duration()
		print(temp)
		if(temp>2):
			firstWin.createWindow()
		time.sleep(1)
except KeyboardInterrupt:
	print('\n')
