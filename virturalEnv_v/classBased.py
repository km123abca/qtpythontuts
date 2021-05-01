from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow,self).__init__()
		self.setGeometry(200,200,300,300)
		self.setWindowTitle("Welcome")
		self.initUI()

	def initUI(self):
		self.label =QtWidgets.QLabel(self)
		self.label.setText("My First Label")
		self.label.move(50,50)

		self.button1=QtWidgets.QPushButton(self)
		self.button1.setText("Click")
		self.button1.clicked.connect(self.buttonClicked)

	def buttonClicked(self):
		self.label.setText("Button Pressed Button Pressed")
		self.update()

	def update(self):
		self.label.adjustSize()

def window():
	app=QApplication(sys.argv)
	win=MyWindow()
	win.show()
	sys.exit(app.exec_())

window()



	