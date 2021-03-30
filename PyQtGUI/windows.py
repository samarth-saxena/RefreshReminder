


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys



class popupWindow(QMainWindow):
	def __init__(self):
		super(popupWindow, self).__init__()
		self.setGeometry(200,200,1000,500)
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
		self.okButton.setGeometry(QtCore.QRect(390, 330, 231, 111))
		self.okButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.okButton.setFlat(False)
		self.okButton.setObjectName("okButton")
		self.okButton.setStyleSheet("border: 5px solid black")
		
		self.hideButton = QtWidgets.QPushButton(self.centralwidget)
		self.hideButton.setObjectName("hideButton")
		self.hideButton.setStyleSheet("border: 5px solid black")
		self.hideButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

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
		
		self.setCentralWidget(self.centralwidget)
		self.retranslateUi()
		QtCore.QMetaObject.connectSlotsByName(self)

	def retranslateUi(self):
		_translate = QtCore.QCoreApplication.translate
		self.setWindowTitle("popupWindow")
		self.okButton.setText("Okay")
		self.hideButton.setText("hide")
		self.titleLabel.setText("Refresh time!!")
		self.update()
		self.okButton.clicked.connect(self.closeWin)
		self.hideButton.clicked.connect(self.hideWin)
	
	def update(self):
		self.titleLabel.adjustSize()

	def closeWin(self):
		self.close()
	
	def hideWin(self):
		self.setWindowOpacity(0)

	def showWin(self):
		self.setWindowOpacity(100)

def createWindow():
	app = QtWidgets.QApplication(sys.argv)
	ui = popupWindow()
	ui.setWindowFlag(Qt.FramelessWindowHint)
	ui.show()
	sys.exit(app.exec_())

createWindow()