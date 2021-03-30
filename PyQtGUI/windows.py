
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
		self.setStyleSheet("background-color: #ffbf00;")
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
	ui.setWindowFlag(Qt.FramelessWindowHint)
	ui.show()
	app.exec_()


class popupWindow(QMainWindow):
	def __init__(self):
		super(popupWindow, self).__init__()
		self.setGeometry(250,250,1000,500)
		self.setupUi()

	def setupUi(self):
		self.setStyleSheet("background-color: #ffbf00;")
		self.setObjectName("popupWindow")
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
		self.setWindowTitle("popupWindow")
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

def createPopup():
	app = QtWidgets.QApplication(sys.argv)
	ui = popupWindow()
	ui.setWindowFlag(Qt.FramelessWindowHint)
	ui.show()
	app.exec_()

# createPopup()

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
	createMainWindow()
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
				createPopup()
				work=0
			time.sleep(1)
	except KeyboardInterrupt:
		print('\n')

if __name__=="__main__":
	main()