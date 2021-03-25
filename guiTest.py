import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

def window():
	app = QApplication(sys.argv)

	win = QMainWindow()
	win.setGeometry(50,50,500,300)
	win.setWindowTitle("My Window123")
	
	label = QtWidgets.QLabel(win)
	label.setText("Something lorem ipsum")

	win.show()
	sys.exit(app.exec_())

window()