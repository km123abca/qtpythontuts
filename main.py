from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys


def buttonClicked():
	print("button was clicked")
def window():
	app =QApplication(sys.argv)
	win =QMainWindow()
	win.setGeometry(200,200,300,300)
	win.setWindowTitle("Welcome")

	label =QtWidgets.QLabel(win)
	label.setText("My First Label")
	label.move(50,50)

	button1=QtWidgets.QPushButton(win)
	button1.setText("Click")
	button1.clicked.connect(buttonClicked)

	win.show()
	sys.exit(app.exec_())

window()
	