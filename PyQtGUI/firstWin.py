# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys



class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.setEnabled(True)
		MainWindow.resize(776, 635)
		MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		MainWindow.setWindowOpacity(0.7)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.onButton = QtWidgets.QPushButton(self.centralwidget)
		self.onButton.setGeometry(QtCore.QRect(240, 330, 231, 111))
		self.onButton.setCursor(QtGui.QCursor(QtCore.Qt.SizeAllCursor))
		self.onButton.setFlat(False)
		self.onButton.setObjectName("onButton")
		self.titleLabel = QtWidgets.QLabel(self.centralwidget)
		self.titleLabel.setGeometry(QtCore.QRect(200, 120, 371, 141))
		font = QtGui.QFont()
		font.setFamily("Quicksand")
		font.setPointSize(48)
		self.titleLabel.setFont(font)
		self.titleLabel.setObjectName("titleLabel")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 776, 22))
		self.menubar.setObjectName("menubar")
		self.menufile = QtWidgets.QMenu(self.menubar)
		self.menufile.setObjectName("menufile")
		self.menutest = QtWidgets.QMenu(self.menubar)
		self.menutest.setObjectName("menutest")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
		self.statusbar.setAcceptDrops(False)
		self.statusbar.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.menutest.addSeparator()
		self.menubar.addAction(self.menufile.menuAction())
		self.menubar.addAction(self.menutest.menuAction())

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.onButton.setText(_translate("MainWindow", "PushButton"))
		self.titleLabel.setText(_translate("MainWindow", "Test label"))
		self.menufile.setTitle(_translate("MainWindow", "file"))
		self.menutest.setTitle(_translate("MainWindow", "test"))
		self.update()
	
	def update(self):
		self.titleLabel.adjustSize()


def createWindow():
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

# createWindow()