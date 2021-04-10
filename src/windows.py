
import time
from ctypes import Structure, windll, c_uint, sizeof, byref

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class mainWindow(QMainWindow):
	def __init__(self):
		super(mainWindow, self).__init__()
		self.setGeometry(200,200,1000,800)
		self.setupUi()

	def setupUi(self):
		self.setStyleSheet("background-color: #00bfff;")
		self.setObjectName("mainWindow")
		self.setEnabled(True)
		self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		self.setWindowOpacity(1)
		self.centralwidget = QtWidgets.QWidget(self)
		self.centralwidget.setObjectName("centralwidget")

		self.titleLabel = QtWidgets.QLabel(self.centralwidget)
		self.titleLabel.setGeometry(QtCore.QRect(100, 100, 371, 141))
		self.titleLabel.setObjectName("titleLabel")

		self.exitButton = QtWidgets.QPushButton(self.centralwidget)
		self.exitButton.setObjectName("exitButton")
		self.exitButton.setStyleSheet("border: 5px solid black")
		self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

		self.option1 = QtWidgets.QLabel(self.centralwidget)
		self.option1.setGeometry(QtCore.QRect(200, 250, 371, 141))
		self.option1.setObjectName("option1")

		self.onSlider = QtWidgets.QSlider(self.centralwidget)
		self.onSlider.setObjectName("onSlider")
		self.onSlider.setGeometry(QtCore.QRect(550, 300, 91, 31))
		self.onSlider.setMaximum(1)
		self.onSlider.setPageStep(1)
		self.onSlider.setOrientation(Qt.Horizontal)
		self.onSlider.setTickPosition(QtWidgets.QSlider.NoTicks)

		self.option2 = QtWidgets.QLabel(self.centralwidget)
		self.option2.setGeometry(QtCore.QRect(200, 350, 371, 141))
		self.option2.setObjectName("option2")

		self.onSlider2 = QtWidgets.QSlider(self.centralwidget)
		self.onSlider2.setObjectName("onSlider2")
		self.onSlider2.setGeometry(QtCore.QRect(550, 400, 91, 31))
		self.onSlider2.setMaximum(1)
		self.onSlider2.setPageStep(1)
		self.onSlider2.setOrientation(Qt.Horizontal)
		self.onSlider2.setTickPosition(QtWidgets.QSlider.NoTicks)

		self.aboutButton = QtWidgets.QPushButton(self.centralwidget)
		self.aboutButton.setGeometry(QtCore.QRect(10, 100, 100, 80))
		self.aboutButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.aboutButton.setFlat(False)
		self.aboutButton.setObjectName("aboutButton")
		self.aboutButton.setStyleSheet("border: 5px solid black")

		self.helpButton = QtWidgets.QPushButton(self.centralwidget)
		self.helpButton.setGeometry(QtCore.QRect(10, 200, 100, 80))
		self.helpButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.helpButton.setFlat(False)
		self.helpButton.setObjectName("helpButton")
		self.helpButton.setStyleSheet("border: 5px solid black")

		self.goButton = QtWidgets.QPushButton(self.centralwidget)
		self.goButton.setGeometry(QtCore.QRect(250, 550, 231, 111))
		self.goButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.goButton.setFlat(False)
		self.goButton.setObjectName("goButton")
		self.goButton.setStyleSheet("border: 5px solid black")

		font = QtGui.QFont()
		font.setFamily("Quicksand")
		font.setBold(True)
		font.setWeight(80)
		font.setPointSize(48)
		self.titleLabel.setFont(font)

		font.setPointSize(20)
		self.goButton.setFont(font)

		font.setPointSize(14)
		self.exitButton.setFont(font)

		font.setBold(False)
		self.option1.setFont(font)
		self.option2.setFont(font)

		self.setCentralWidget(self.centralwidget)
		self.retranslateUi()
		QtCore.QMetaObject.connectSlotsByName(self)

	def retranslateUi(self):
		_translate = QtCore.QCoreApplication.translate
		self.setWindowTitle("mainWindow")

		self.titleLabel.setText("Refresh Reminder")

		self.exitButton.setText("  X  ")

		self.option1.setText("Turn on reminder")
		self.option2.setText("Turn on posture track")

		self.aboutButton.setText("About")
		self.helpButton.setText("Help")
		self.goButton.setText("Lets go!")

		self.update()

		self.goButton.clicked.connect(self.closeWin)
		self.exitButton.clicked.connect(self.exitWin)
	
	def update(self):
		self.titleLabel.adjustSize()

	def closeWin(self):
		self.close()
	
	def exitWin(self):
		sys.exit()


def createMainWindow():
	app = QtWidgets.QApplication(sys.argv)
	ui = mainWindow()
	# ui.setWindowFlag(Qt.FramelessWindowHint)
	ui.show()
	app.exec_()

# createMainWindow()

#____________________________________________________________________________________

class refreshWindow(QMainWindow):
	def __init__(self):
		super(refreshWindow, self).__init__()
		self.setGeometry(250,250,1000,500)
		self.setupUi()

	def setupUi(self):
		self.setStyleSheet("background-color: #ffbf00;")
		self.setObjectName("refreshWindow")
		self.setEnabled(True)
		self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		self.setWindowOpacity(0.75)
		self.centralwidget = QtWidgets.QWidget(self)
		self.centralwidget.setObjectName("centralwidget")

		self.okButton = QtWidgets.QPushButton(self.centralwidget)
		self.okButton.setGeometry(QtCore.QRect(380, 330, 231, 111))
		self.okButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.okButton.setFlat(False)
		self.okButton.setObjectName("okButton")
		self.okButton.setStyleSheet("border: 5px solid black")
		
		self.exitButton = QtWidgets.QPushButton(self.centralwidget)
		self.exitButton.setObjectName("exitButton")
		self.exitButton.setStyleSheet("border: 5px solid black")
		self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

		self.titleLabel = QtWidgets.QLabel(self.centralwidget)
		self.titleLabel.setGeometry(QtCore.QRect(170, 120, 371, 141))
		self.titleLabel.setObjectName("titleLabel")

		font = QtGui.QFont()
		font.setFamily("Quicksand")
		font.setBold(True)
		font.setWeight(80)
		font.setPointSize(48)
		self.titleLabel.setFont(font)

		font.setPointSize(20)
		self.okButton.setFont(font)

		font.setPointSize(14)
		self.exitButton.setFont(font)

		self.setCentralWidget(self.centralwidget)
		self.retranslateUi()
		QtCore.QMetaObject.connectSlotsByName(self)

	def retranslateUi(self):
		_translate = QtCore.QCoreApplication.translate
		self.setWindowTitle("refreshWindow")
		self.okButton.setText("Okay")
		self.exitButton.setText("  X  ")
		self.titleLabel.setText("Refresh time!!")
		self.update()
		self.okButton.clicked.connect(self.closeWin)
		self.exitButton.clicked.connect(self.exitWin)
	
	def update(self):
		self.titleLabel.adjustSize()

	def closeWin(self):
		self.close()
	
	def exitWin(self):
		sys.exit()

	def showWin(self):
		self.setWindowOpacity(100)

def createRefreshWin():
	app = QtWidgets.QApplication(sys.argv)
	ui = refreshWindow()
	ui.setWindowFlag(Qt.FramelessWindowHint)
	ui.show()
	app.exec_()


#____________________________________________________________________________________

class postureWindow(QMainWindow):
	def __init__(self, height, width):
		super(postureWindow, self).__init__()
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
		# ui.setWindowOpacity(0)
		# ui.setAttribute(Qt.WA_NoSystemBackground, True)
		self.setAttribute(Qt.WA_TranslucentBackground, True)
		self.setGeometry(0,0,width,height)
		self.setupUi()

	def setupUi(self):
		self.setStyleSheet("border: 10px solid red;")
		self.setObjectName("postureWindow")
		self.setEnabled(True)
		self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		
		self.centralwidget = QtWidgets.QWidget(self)
		self.centralwidget.setObjectName("centralwidget")

		# self.okButton = QtWidgets.QPushButton(self.centralwidget)
		# self.okButton.setGeometry(QtCore.QRect(380, 330, 231, 111))
		# self.okButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		# self.okButton.setFlat(False)
		# self.okButton.setObjectName("okButton")
		# self.okButton.setStyleSheet("border: 5px solid black")
		
		self.exitButton = QtWidgets.QPushButton(self.centralwidget)
		self.exitButton.setObjectName("exitButton")
		self.exitButton.setStyleSheet("border: 5px solid red; background-color: red;")
		self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

		# self.titleLabel = QtWidgets.QLabel(self.centralwidget)
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

		self.setCentralWidget(self.centralwidget)
		self.retranslateUi()
		QtCore.QMetaObject.connectSlotsByName(self)

	def retranslateUi(self):
		_translate = QtCore.QCoreApplication.translate
		self.setWindowTitle("postureWindow")
		# self.okButton.setText("Okay")
		self.exitButton.setText("  X  ")
		# self.titleLabel.setText("Sitting too close!!")
		self.update()
		# self.okButton.clicked.connect(self.closeWin)
		self.exitButton.clicked.connect(self.closeWin)
	
	# def update(self):
	# 	self.titleLabel.adjustSize()

	def closeWin(self):
		self.close()
	
	def exitWin(self):
		sys.exit()

	def showWin(self):
		self.setWindowOpacity(100)

def createPostureWin():
	app = QtWidgets.QApplication(sys.argv)
	screen = app.primaryScreen()
	print('Screen: %s' % screen.name())
	size = screen.size()
	print('Size: %d x %d' % (size.width(), size.height()))
	rect = screen.availableGeometry()
	print('Available: %d x %d' % (rect.width(), rect.height()))

	ui = postureWindow(size.height(), size.width())

	ui.show()
	app.exec_()

# createPostureWin()

#____________________________________________________________________________________