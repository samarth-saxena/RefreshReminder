import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFile, Qt, pyqtSignal, QObject
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QDialog, QDialogButtonBox, QFormLayout, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QStackedLayout, QSystemTrayIcon, QVBoxLayout, QWidget

class postureWindow(QMainWindow):
    def __init__(self, height, width):
        super(postureWindow, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        # ui.setWindowOpacity(0)
        # ui.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setGeometry(0, 0, width, height)
        self.setupUi()

    def setupUi(self):
        self.setStyleSheet("border: 10px solid red;")
        self.setObjectName("postureWindow")
        self.setEnabled(True)
        self.setCursor(QtGui.QCursor(Qt.ArrowCursor))

        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # self.okButton = QPushButton(self.centralwidget)
        # self.okButton.setGeometry(QtCore.QRect(380, 330, 231, 111))
        # self.okButton.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        # self.okButton.setFlat(False)
        # self.okButton.setObjectName("okButton")
        # self.okButton.setStyleSheet("border: 5px solid black")

        self.exitButton = QPushButton(self.centralwidget)
        self.exitButton.setObjectName("exitButton")
        self.exitButton.setStyleSheet(
            "border: 5px solid red; background-color: red;")
        self.exitButton.setCursor(QtGui.QCursor(Qt.PointingHandCursor))

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

createPostureWin()