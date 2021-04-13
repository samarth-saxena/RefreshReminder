import time
import threading
from ctypes import Structure, windll, c_uint, sizeof, byref
import gui
import cv2
from win10toast import ToastNotifier
import numpy as np
import dlib
from math import hypot

import threading
# import main
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFile, Qt, pyqtSignal, QObject
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QDialog, QDialogButtonBox, QFormLayout, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QStackedLayout, QSystemTrayIcon, QVBoxLayout, QWidget
import sys

readytogo = False
flag = [False, False, False, False]
app = QApplication(sys.argv)
screen = app.primaryScreen()
size = screen.size()

class Communicate(QObject):
	startApp = pyqtSignal()
	exitApp = pyqtSignal()
	createBreakPopup = pyqtSignal()

c = Communicate()

class postureWindow(QWidget):
	def __init__(self, height, width):
		super().__init__()

		self.setWindowTitle("postureWindow")
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setWindowFlag(Qt.WindowStaysOnTopHint)
		# ui.setWindowOpacity(0)
		# ui.setAttribute(Qt.WA_NoSystemBackground, True)
		self.setAttribute(Qt.WA_TranslucentBackground, True)
		self.setStyleSheet("border : 10px solid red;")
		self.setFixedSize(width, height)
		self.setupUi()

	def setupUi(self):
		self.setObjectName("postureWindow")
		self.framelayout = QHBoxLayout()
		# self.okButton = QPushButton(self.centralwidget)
		# self.okButton.setGeometry(QtCore.QRect(380, 330, 231, 111))
		# self.okButton.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
		# self.okButton.setFlat(False)
		# self.okButton.setObjectName("okButton")
		# self.okButton.setStyleSheet("border: 5px solid black")

		self.exitButton = QPushButton("  X  ", self)
		self.exitButton.setObjectName("exitButton")
		self.exitButton.setStyleSheet(
			"border: 5px solid red; background-color: red;")
		self.exitButton.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
		self.exitButton.clicked.connect(self.closeWin)

		# self.titleLabel = QLabel(self.centralwidget)
		# self.titleLabel.setGeometry(QtCore.QRect(170, 120, 371, 141))
		# self.titleLabel.setObjectName("titleLabel")

		font = QtGui.QFont()
		font.setFamily("Quicksand")
		font.setBold(True)
		font.setWeight(80)
		font.setPointSize(48)
		# self.titleLabel.setFont(font)

		# font.setPointSize(20)
		# self.okButton.setFont(font)

		font.setPointSize(14)
		self.exitButton.setFont(font)

		# self.okButton.setText("Okay")
		# self.exitButton.setText()
		# self.titleLabel.setText("Sitting too close!!")


	def closeWin(self):
		self.hide()
		c.exitApp.emit() #TODO Remove this line



# def createPostureWin():
# 	app = QtWidgets.QApplication(sys.argv)
# 	screen = app.primaryScreen()
# 	print('Screen: %s' % screen.name())
# 	size = screen.size()
# 	print('Size: %d x %d' % (size.width(), size.height()))
# 	rect = screen.availableGeometry()
# 	print('Available: %d x %d' % (rect.width(), rect.height()))

# 	ui = postureWindow(size.height(), size.width())

# 	ui.show()
# 	app.exec_()


class breakPopup(QWidget):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Refresh Reminder - Break Popup")
		self.setMinimumSize(800, 400)
		self.setWindowFlag(Qt.FramelessWindowHint)

		popupCSS = ""

		self.mainLayout = QGridLayout()

		self.okButton = QPushButton("Okay", self)
		self.okButton.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
		self.okButton.setObjectName("okButton")
		self.okButton.clicked.connect(self.launchExercise)

		self.settingsButton = QPushButton("Go to settings", self)
		self.settingsButton.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
		self.settingsButton.setObjectName("settingsButton")
		self.settingsButton.clicked.connect(self.showMainWin)

		self.skipButton = QPushButton("Skip", self)
		self.skipButton.setObjectName("skipButton")
		self.skipButton.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
		self.skipButton.clicked.connect(self.hide)

		self.titleLabel = QLabel("Its time for a break!", self)
		self.titleLabel.setObjectName("titleLabel")

		self.mainLayout.addWidget(self.titleLabel, 0, 0, 1, 3)
		self.mainLayout.addWidget(self.settingsButton, 1, 0)
		self.mainLayout.addWidget(self.skipButton, 1, 1)
		self.mainLayout.addWidget(self.okButton, 1, 2)

		self.setLayout(self.mainLayout)

	def launchExercise(self):
		self.hide()
		print("Exercise")

	def showMainWin(self):
		self.hide()
		launchMainWindow()


class MainWindow(QWidget):
	popup = breakPopup()
	frame = postureWindow(size.height(), size.width())

	def __init__(self):
		super().__init__()

		#Window Setup
		self.setWindowTitle("Refresh Reminder - Main Window")
		self.setMinimumSize(800, 400)
		self.setWindowFlag(Qt.FramelessWindowHint)

		self.setupUI()


	def setupUI(self):
		#Main Stylesheet
		mainCSS = ("""
			QWidget#mainWidget {
				margin: 0px;
				padding: 0px;
				text-align: center;
				background-color: #6fb98f;
				border: 1 px;
			}


			QWidget#sidePane {
				margin: 0px;
				padding: 0px;
				background-color: #2c7873;
				border:0px;

			}

			QWidget#quitPane {
				margin: 0px;
				padding: 0px;
				border:0px;
				background-color: #2c7873;
			}

			QWidget#titlePane {
				margin: 0px;
				border:0px;
			}

			QLabel#titleLabel {
				font-family: Quicksand;
				font-size: 60px;
				font-weight: bold;
				padding: 20px 10px;

			}

			QPushButton {
				margin: 0px;
				padding: 20px 50px;
				background-color: #2c7873;
				color: white;
				border: none;
				font-family: "Open Sans";
				font-size: 20px;
			}

			QPushButton#switch1, #switch2, #switch3, #switch4 {
				padding: 10px 20px;
				background-color:red;
				max-width: 50px;
				height: 30px;
				font-weight: bold;
				font-size:15px;
			}

			QLabel#option1, #option2, #option3, #option4 {
				font-size:16px;
			}

			QPushButton::hover {
				background-color: #004445;
			}

		""")


		#Layouts
		self.mainLayout = QGridLayout()
		self.sidePaneLayout = QVBoxLayout()
		self.titlePaneLayout = QHBoxLayout()
		self.stackedLayout = QStackedLayout()
		# self.quitPaneLayout = QVBoxLayout()
		self.VSpacer = QVBoxLayout()
		self.VSpacer.addStretch(1)
		self.HSpacer = QHBoxLayout()
		self.HSpacer.addStretch(1)

		#Widgets
		self.setObjectName("mainWidget")
		self.sidePane = QWidget(self)
		self.sidePane.setObjectName("sidePane")
		self.titlePane = QWidget(self)
		self.titlePane.setObjectName("titlePane")
		# self.quitPane = QWidget(self)
		# self.quitPane.setObjectName("quitPane")

		self.titleLabel = QLabel("Refresh Reminder", self)
		# self.titleLabel.setGeometry(QtCore.QRect(100, 100, 371, 141))
		self.titleLabel.setObjectName("titleLabel")

		self.homePage()
		self.settingsPage()
		self.helpPage()
		self.aboutPage()

		self.exitButton = QPushButton("Exit", self)
		self.exitButton.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
		self.exitButton.setObjectName("exitButton")
		self.exitButton.clicked.connect(self.initiateExitApp)

		self.hideButton = QPushButton("Hide", self)
		self.hideButton.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
		self.hideButton.setObjectName("hideButton")
		self.hideButton.clicked.connect(self.hideApp)

		self.homeButton = QPushButton("Home", self)
		self.homeButton.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
		self.homeButton.setObjectName("homeButton")
		# self.homeButton.setIcon(QIcon('home.png'))
		# self.homeButton.setIconSize(QtCore.QSize(130,130))
		self.homeButton.clicked.connect(lambda: self.switchPage(0))

		self.settingsButton = QPushButton("Settings", self)
		self.settingsButton.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
		self.settingsButton.setObjectName("settingsButton")
		self.settingsButton.clicked.connect(lambda: self.switchPage(1))

		self.helpButton = QPushButton("Help", self)
		self.helpButton.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
		self.helpButton.setObjectName("helpButton")
		self.helpButton.clicked.connect(lambda: self.switchPage(2))

		self.aboutButton = QPushButton("About", self)
		self.aboutButton.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
		self.aboutButton.setObjectName("aboutButton")
		self.aboutButton.clicked.connect(lambda: self.switchPage(3))
		# self.aboutButton.clicked.connect(hideWindow)

		self.sidePaneLayout.addWidget(self.exitButton, 0, Qt.AlignTop)
		self.sidePaneLayout.addWidget(self.hideButton, 0, Qt.AlignTop)
		self.sidePaneLayout.addStretch(1)
		self.sidePaneLayout.addWidget(self.homeButton, 0, Qt.AlignTop)
		self.sidePaneLayout.addWidget(self.settingsButton, 0, Qt.AlignTop)
		self.sidePaneLayout.addWidget(self.helpButton, 0, Qt.AlignTop)
		self.sidePaneLayout.addWidget(self.aboutButton, 0, Qt.AlignTop)
		self.sidePaneLayout.addStretch(1)
		self.sidePaneLayout.setContentsMargins(0,0,0,0)
		# self.sidePaneLayout.setAlignment()

		# self.quitPaneLayout.addWidget(self.exitButton, 0, Qt.AlignCenter)
		# self.quitPaneLayout.addWidget(self.hideButton, 0, Qt.AlignCenter)
		# self.quitPaneLayout.setContentsMargins(0,0,0,0)


		self.setStyleSheet(mainCSS)

		# self.titlePaneLayout.addStretch()
		self.titlePaneLayout.addWidget(self.titleLabel, 0, Qt.AlignCenter)
		self.titlePaneLayout.setContentsMargins(0,0,0,0)
		# self.titlePaneLayout.addStretch(40)
		# self.titlePaneLayout.setAlignment(self.titleLabel, Qt.AlignCenter)


		# self.mainLayout.addWidget(self.quitPane, 0, 0)
		self.mainLayout.addWidget(self.titlePane, 0, 1)
		self.mainLayout.addWidget(self.sidePane, 0, 0, 2, 1)
		self.mainLayout.addLayout(self.stackedLayout, 1, 1)
		self.mainLayout.setContentsMargins(0,0,0,0)
		self.mainLayout.setSpacing(0)
		# self.mainLayout.setSpacing(50)

		# Setting layouts
		# self.quitPane.setLayout(self.quitPaneLayout)
		self.titlePane.setLayout(self.titlePaneLayout)
		self.sidePane.setLayout(self.sidePaneLayout)
		self.setLayout(self.mainLayout)

	def switchPage(self, num):
		self.stackedLayout.setCurrentIndex(num)

	def homePage(self):
		self.page1 = QWidget()
		self.page1Layout = QGridLayout()


		spacingBox1 = QWidget(self.page1)
		spacingBox1.setLayout(self.VSpacer)

		option1 = QLabel("Face-to-screen distance", self.page1)
		option1.setObjectName('option1')

		switch1 = QPushButton("Off", self.page1)
		switch1.setCheckable(True)
		switch1.clicked.connect(lambda: self.changeColor(switch1, 1))
		switch1.setObjectName('switch1')
		switch1.setCursor(QtGui.QCursor(Qt.PointingHandCursor))

		option2 = QLabel("Blink detection", self.page1)
		option2.setObjectName('option2')

		switch2 = QPushButton("Off", self.page1)
		switch2.setCheckable(True)
		switch2.clicked.connect(lambda: self.changeColor(switch2, 2))
		switch2.setObjectName('switch2')
		switch2.setCursor(QtGui.QCursor(Qt.PointingHandCursor))

		option3 = QLabel("Excercise animation", self.page1)
		option3.setObjectName('option3')

		switch3 = QPushButton("Off", self.page1)
		switch3.setCheckable(True)
		switch3.clicked.connect(lambda: self.changeColor(switch3, 3))
		switch3.setObjectName('switch2')
		switch3.setCursor(QtGui.QCursor(Qt.PointingHandCursor))

		option4 = QLabel("Work time detection", self.page1)
		option4.setObjectName('option4')

		switch4 = QPushButton("Off", self)
		switch4.setCheckable(True)
		switch4.clicked.connect(lambda: self.changeColor(switch4, 4))
		switch4.setObjectName('switch2')
		switch4.setCursor(QtGui.QCursor(Qt.PointingHandCursor))


		spacingBox2 = QWidget(self.page1)
		spacingBox2.setLayout(self.VSpacer)

		self.page1Layout.addWidget(spacingBox1, 0, 0, 5, 1)

		self.page1Layout.addWidget(option1, 1, 1)
		self.page1Layout.addWidget(option2, 2, 1)
		self.page1Layout.addWidget(option3, 3, 1)
		self.page1Layout.addWidget(option4, 4, 1)

		self.page1Layout.addWidget(switch1, 1, 2)
		self.page1Layout.addWidget(switch2, 2, 2)
		self.page1Layout.addWidget(switch3, 3, 2)
		self.page1Layout.addWidget(switch4, 4, 2)

		self.page1Layout.addWidget(spacingBox2, 0, 3, 5, 1)

		self.page1Layout.setAlignment(Qt.AlignTop)

		self.page1.setLayout(self.page1Layout)
		self.stackedLayout.addWidget(self.page1)

	def settingsPage(self):
		# Create the second page
		self.page2 = QWidget()
		self.page2Layout = QVBoxLayout()

		# option1 = QLabel("Notification mode:", self.page1)
		# option1.setObjectName('option1')

		# switch1 = QPushButton("On", self.page1)
		# switch1.setCheckable(True)
		# switch1.clicked.connect(lambda: self.changeColor(switch1))
		# switch1.setObjectName('switch1')
		# switch1.setCursor(QtGui.QCursor(Qt.PointingHandCursor))

		# self.page2Layout.addWidget(title1)
		# self.page2Layout.addWidget(text1)
		# self.page2Layout.setAlignment(Qt.AlignTop)

		self.page2.setLayout(self.page2Layout)
		self.stackedLayout.addWidget(self.page2)

	def helpPage(self):
		# Create the second page
		self.page3 = QWidget()
		self.page3Layout = QVBoxLayout()

		title1 = QLabel("<h1>Face-to-screen distance</h1>", self)
		title1.setObjectName('title1')

		text1 = QLabel("<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", self)
		text1.setObjectName('text1')
		text1.setWordWrap(True)

		self.page3Layout.addWidget(title1)
		self.page3Layout.addWidget(text1)
		self.page3Layout.setAlignment(Qt.AlignTop)

		self.page3.setLayout(self.page3Layout)
		self.stackedLayout.addWidget(self.page3)

	def aboutPage(self):
		self.page4 = QWidget()
		self.page4Layout = QVBoxLayout()

		title1 = QLabel("<h1>About the application</h1>", self)
		title1.setObjectName('title1')

		text1 = QLabel("<p><b>Refresh reminder</b> is a desktop application aimed towards digital well-being of heavy desktop users like students, teachers, programmers, designers etc. <br> This application has been written in Python. It uses PyQt5 for GUI and OpenCV2 for computer vision. <br><br> Created by <b> Paradigm Shifters </b>, a team of undergraduates at IIIT Delhi. Created as a project in the course <b> Design of Interactice Systems [DES205] </b> , Winter 2020.", self)
		text1.setObjectName('text1')
		text1.setWordWrap(True)

		self.page4Layout.addWidget(title1)
		self.page4Layout.addWidget(text1)
		self.page4Layout.setAlignment(Qt.AlignTop)

		self.page4.setLayout(self.page4Layout)
		self.stackedLayout.addWidget(self.page4)

	def changeColor(self, button, n):
		if button.isChecked():
			button.setStyleSheet("background-color : green")
			button.setText("On")
			flag[n-1] = True
			print(n, "True")
		else:
			button.setStyleSheet("background-color : red")
			button.setText("Off")
			flag[n-1] = False
			print(n, "False")

	def hideApp(self):
		# global readytogo
		# readytogo = True
		# self.close()
		c.startApp.emit()
		# c.createBreakPopup.emit()
		self.hide()
		# self.close()

	@classmethod
	def launchBreakPopup(cls):
		MainWindow.popup.show()

	@classmethod
	def launchPostureFrame(cls):
		MainWindow.frame.show()

	def initiateExitApp(self):
		c.exitApp.emit()

	def showApp(self):
		self.show(self)

def launchMainWindow():
	window.show()


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
		print("Face thread started")

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

		while (flag[0]):
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
				c.exitApp.emit()
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
			print("Screen thread started")
			# MainWindow.launchBreakPopup()
			# popup = gui.breakPopup()
			# print("Point 2")
			# popup.show()
			# print("Point 3")
			# app.exec_()
			# print("Point 4")
			# global temp
			# temp = True


			work = 0
			while flag[3]:
				temp = get_idle_duration()
				if (temp<5):
					work+=1
				else:
					work=0
				print(temp)
				print(work)
				print()
				if(work>10):
					# windows.createRefreshWin()
					c.createBreakPopup.emit()
					work=0
				time.sleep(1)


		except KeyboardInterrupt:
			c.exitApp.emit()




def startupServices():
	if(flag[0] & (TFaceDistance.is_alive()==False) ):
		TFaceDistance.start()
	if(flag[3] & (TScreenUsage.is_alive()==False) ):
		TScreenUsage.start()

def shutdownApp():
	global flag
	flag[0] = False
	flag[1] = False
	flag[2] = False
	flag[3] = False
	if(TFaceDistance.is_alive()):
		TFaceDistance.join()
	if(TScreenUsage.is_alive()):
		TScreenUsage.join()

	sys.exit(0)

if __name__=="__main__":

	c.exitApp.connect(shutdownApp)
	c.startApp.connect(startupServices)
	c.createBreakPopup.connect(MainWindow.launchBreakPopup)

	window = MainWindow()

	# window.show()
	MainWindow.launchPostureFrame()
	TFaceDistance = faceDistance(1, "Thread-1", 1)
	TScreenUsage = screenUsage(2, "Thread-2", 2)

	app.exec_()









# class mainWindow(QMainWindow):
#     def __init__(self):
#         super(mainWindow, self).__init__()
#         self.setGeometry(200, 200, 1000, 800)
#         self.setupUi()

#     def setupUi(self):
#         self.setStyleSheet("background-color: #00bfff;")
#         self.setObjectName("mainWindow")
#         self.setEnabled(True)
#         self.setCursor(QtGui.QCursor(Qt.ArrowCursor))
#         self.setWindowOpacity(1)
#         self.centralwidget = QWidget(self)
#         self.centralwidget.setObjectName("centralwidget")

#         self.titleLabel = QLabel(self.centralwidget)
#         self.titleLabel.setGeometry(QtCore.QRect(100, 100, 371, 141))
#         self.titleLabel.setObjectName("titleLabel")

#         self.exitButton = QPushButton(self.centralwidget)
#         self.exitButton.setObjectName("exitButton")
#         self.exitButton.setStyleSheet("border: 5px solid black")
#         self.exitButton.setCursor(QtGui.QCursor(Qt.PointingHandCursor))

#         self.option1 = QLabel(self.centralwidget)
#         self.option1.setGeometry(QtCore.QRect(200, 250, 371, 141))
#         self.option1.setObjectName("option1")

#         self.onSlider = QtWidgets.QSlider(self.centralwidget)
#         self.onSlider.setObjectName("onSlider")
#         self.onSlider.setGeometry(QtCore.QRect(550, 300, 91, 31))
#         self.onSlider.setMaximum(1)
#         self.onSlider.setPageStep(1)
#         self.onSlider.setOrientation(Qt.Horizontal)
#         self.onSlider.setTickPosition(QtWidgets.QSlider.NoTicks)

#         self.option2 = QLabel(self.centralwidget)
#         self.option2.setGeometry(QtCore.QRect(200, 350, 371, 141))
#         self.option2.setObjectName("option2")

#         self.onSlider2 = QtWidgets.QSlider(self.centralwidget)
#         self.onSlider2.setObjectName("onSlider2")
#         self.onSlider2.setGeometry(QtCore.QRect(550, 400, 91, 31))
#         self.onSlider2.setMaximum(1)
#         self.onSlider2.setPageStep(1)
#         self.onSlider2.setOrientation(Qt.Horizontal)
#         self.onSlider2.setTickPosition(QtWidgets.QSlider.NoTicks)

#         self.aboutButton = QPushButton(self.centralwidget)
#         self.aboutButton.setGeometry(QtCore.QRect(10, 100, 100, 80))
#         self.aboutButton.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
#         self.aboutButton.setFlat(False)
#         self.aboutButton.setObjectName("aboutButton")
#         self.aboutButton.setStyleSheet("border: 5px solid black")

#         self.helpButton = QPushButton(self.centralwidget)
#         self.helpButton.setGeometry(QtCore.QRect(10, 200, 100, 80))
#         self.helpButton.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
#         self.helpButton.setFlat(False)
#         self.helpButton.setObjectName("helpButton")
#         self.helpButton.setStyleSheet("border: 5px solid black")

#         self.goButton = QPushButton(self.centralwidget)
#         self.goButton.setGeometry(QtCore.QRect(250, 550, 231, 111))
#         self.goButton.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
#         self.goButton.setFlat(False)
#         self.goButton.setObjectName("goButton")
#         self.goButton.setStyleSheet("border: 5px solid black")

#         font = QtGui.QFont()
#         font.setFamily("Quicksand")
#         font.setBold(True)
#         font.setWeight(80)
#         font.setPointSize(48)
#         self.titleLabel.setFont(font)

#         font.setPointSize(20)
#         self.goButton.setFont(font)

#         font.setPointSize(14)
#         self.exitButton.setFont(font)

#         font.setBold(False)
#         self.option1.setFont(font)
#         self.option2.setFont(font)

#         self.setCentralWidget(self.centralwidget)
#         self.retranslateUi()
#         QtCore.QMetaObject.connectSlotsByName(self)

#     def retranslateUi(self):
#         _translate = QtCore.QCoreApplication.translate
#         self.setWindowTitle("mainWindow")

#         self.titleLabel.setText("Refresh Reminder")

#         self.exitButton.setText("  X  ")

#         self.option1.setText("Turn on reminder")
#         self.option2.setText("Turn on posture track")

#         self.aboutButton.setText("About")
#         self.helpButton.setText("Help")
#         self.goButton.setText("Lets go!")

#         self.update()

#         self.goButton.clicked.connect(self.closeWin)
#         self.exitButton.clicked.connect(self.exitWin)

#     def update(self):
#         self.titleLabel.adjustSize()

#     def closeWin(self):
#         self.close()

#     def exitWin(self):
#         sys.exit()


# def createMainWindow():
#     app = QtWidgets.QApplication(sys.argv)
#     ui = mainWindow()
#     # ui.setWindowFlag(Qt.FramelessWindowHint)
#     ui.show()
#     app.exec_()


# createMainWindow()

# # ____________________________________________________________________________________


# class refreshWindow(QMainWindow):
#     def __init__(self):
#         super(refreshWindow, self).__init__()
#         self.setGeometry(250, 250, 1000, 500)
#         self.setupUi()

#     def setupUi(self):
#         self.setStyleSheet("background-color: #ffbf00;")
#         self.setObjectName("refreshWindow")
#         self.setEnabled(True)
#         self.setCursor(QtGui.QCursor(Qt.ArrowCursor))
#         self.setWindowOpacity(0.75)
#         self.centralwidget = QWidget(self)
#         self.centralwidget.setObjectName("centralwidget")

#         self.okButton = QPushButton(self.centralwidget)
#         self.okButton.setGeometry(QtCore.QRect(380, 330, 231, 111))
#         self.okButton.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
#         self.okButton.setFlat(False)
#         self.okButton.setObjectName("okButton")
#         self.okButton.setStyleSheet("border: 5px solid black")

#         self.exitButton = QPushButton(self.centralwidget)
#         self.exitButton.setObjectName("exitButton")
#         self.exitButton.setStyleSheet("border: 5px solid black")
#         self.exitButton.setCursor(QtGui.QCursor(Qt.PointingHandCursor))

#         self.titleLabel = QLabel(self.centralwidget)
#         self.titleLabel.setGeometry(QtCore.QRect(170, 120, 371, 141))
#         self.titleLabel.setObjectName("titleLabel")

#         font = QtGui.QFont()
#         font.setFamily("Quicksand")
#         font.setBold(True)
#         font.setWeight(80)
#         font.setPointSize(48)
#         self.titleLabel.setFont(font)

#         font.setPointSize(20)
#         self.okButton.setFont(font)

#         font.setPointSize(14)
#         self.exitButton.setFont(font)

#         self.setCentralWidget(self.centralwidget)
#         self.retranslateUi()
#         QtCore.QMetaObject.connectSlotsByName(self)

#     def retranslateUi(self):
#         _translate = QtCore.QCoreApplication.translate
#         self.setWindowTitle("refreshWindow")
#         self.okButton.setText("Okay")
#         self.exitButton.setText("  X  ")
#         self.titleLabel.setText("Refresh time!!")
#         self.update()
#         self.okButton.clicked.connect(self.closeWin)
#         self.exitButton.clicked.connect(self.exitWin)

#     def update(self):
#         self.titleLabel.adjustSize()

#     def closeWin(self):
#         self.close()

#     def exitWin(self):
#         sys.exit()

#     def showWin(self):
#         self.setWindowOpacity(100)


# def createRefreshWin():
#     app = QApplication(sys.argv)
#     ui = refreshWindow()
#     ui.setWindowFlag(Qt.FramelessWindowHint)
#     ui.show()
#     app.exec_()


# # ____________________________________________________________________________________

# class postureWindow(QMainWindow):
#     def __init__(self, height, width):
#         super(postureWindow, self).__init__()
#         self.setWindowFlag(Qt.FramelessWindowHint)
#         self.setWindowFlag(Qt.WindowStaysOnTopHint)
#         # ui.setWindowOpacity(0)
#         # ui.setAttribute(Qt.WA_NoSystemBackground, True)
#         self.setAttribute(Qt.WA_TranslucentBackground, True)
#         self.setGeometry(0, 0, width, height)
#         self.setupUi()

#     def setupUi(self):
#         self.setStyleSheet("border: 10px solid red;")
#         self.setObjectName("postureWindow")
#         self.setEnabled(True)
#         self.setCursor(QtGui.QCursor(Qt.ArrowCursor))

#         self.centralwidget = QWidget(self)
#         self.centralwidget.setObjectName("centralwidget")

#         # self.okButton = QPushButton(self.centralwidget)
#         # self.okButton.setGeometry(QtCore.QRect(380, 330, 231, 111))
#         # self.okButton.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
#         # self.okButton.setFlat(False)
#         # self.okButton.setObjectName("okButton")
#         # self.okButton.setStyleSheet("border: 5px solid black")

#         self.exitButton = QPushButton(self.centralwidget)
#         self.exitButton.setObjectName("exitButton")
#         self.exitButton.setStyleSheet(
#             "border: 5px solid red; background-color: red;")
#         self.exitButton.setCursor(QtGui.QCursor(Qt.PointingHandCursor))

#         # self.titleLabel = QLabel(self.centralwidget)
#         # self.titleLabel.setGeometry(QtCore.QRect(170, 120, 371, 141))
#         # self.titleLabel.setObjectName("titleLabel")

#         font = QtGui.QFont()
#         font.setFamily("Quicksand")
#         font.setBold(True)
#         font.setWeight(80)
#         font.setPointSize(48)
#         # self.titleLabel.setFont(font)

#         # font.setPointSize(20)
#         # self.okButton.setFont(font)

#         font.setPointSize(14)
#         self.exitButton.setFont(font)

#         self.setCentralWidget(self.centralwidget)
#         self.retranslateUi()
#         QtCore.QMetaObject.connectSlotsByName(self)

#     def retranslateUi(self):
#         _translate = QtCore.QCoreApplication.translate
#         self.setWindowTitle("postureWindow")
#         # self.okButton.setText("Okay")
#         self.exitButton.setText("  X  ")
#         # self.titleLabel.setText("Sitting too close!!")
#         self.update()
#         # self.okButton.clicked.connect(self.closeWin)
#         self.exitButton.clicked.connect(self.closeWin)

#     # def update(self):
#     # 	self.titleLabel.adjustSize()

#     def closeWin(self):
#         self.close()

#     def exitWin(self):
#         sys.exit()

#     def showWin(self):
#         self.setWindowOpacity(100)


# def createPostureWin():
#     app = QtWidgets.QApplication(sys.argv)
#     screen = app.primaryScreen()
#     print('Screen: %s' % screen.name())
#     size = screen.size()
#     print('Size: %d x %d' % (size.width(), size.height()))
#     rect = screen.availableGeometry()
#     print('Available: %d x %d' % (rect.width(), rect.height()))

#     ui = postureWindow(size.height(), size.width())

#     ui.show()
#     app.exec_()

# # createPostureWin()

# # ____________________________________________________________________________________