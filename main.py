import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLabel, QShortcut
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence


class MyWindow(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super(MyWindow, self).__init__(parent)

		# setting title 
		self.setWindowTitle("Python ") 
  
		# setting geometry 
		self.setGeometry(100, 100, 800, 600) 

		self.model = QtGui.QStandardItemModel(self)

		self.filenameView = QLabel()
		self.filenameView.setAlignment(Qt.AlignCenter)
		self.filenameView.setStyleSheet("QLabel {background-color: green; font-weight: bold; font-size: 18px; border-radius: 3px; padding:10px; color: #ffffff}")
		self.filenameView.hide()

		self.tableView = QtWidgets.QTableView(self)
		self.tableView.setModel(self.model)
		self.tableView.horizontalHeader().setStretchLastSection(True)

		self.pushButtonLoad = QtWidgets.QPushButton(self)
		self.pushButtonLoad.setText("Open CSV File (Ctrl+O)")
		self.pushButtonLoad.clicked.connect(self.openFileNameDialog)

		shortcut = QShortcut(QKeySequence("Ctrl+O"), self)
		shortcut.activated.connect(self.openFileNameDialog)

		self.layoutVertical = QtWidgets.QVBoxLayout(self)
		self.layoutVertical.addWidget(self.filenameView)
		self.layoutVertical.addWidget(self.tableView)
		self.layoutVertical.addWidget(self.pushButtonLoad)

	def openFileNameDialog(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Comma Separated Value Files (*.csv)", options=options)
		if fileName:
			self.clear_table()
			self.loadCsv(fileName)
			self.filenameView.setText(fileName)
			self.filenameView.show()

	def clear_table(self):
		self.model.clear()

	def loadCsv(self, fileName):
		with open(fileName, "r") as fileInput:
			for row in csv.reader(fileInput):    
				items = [
					QtGui.QStandardItem(field)
					for field in row
				]
				self.model.appendRow(items)

if __name__ == "__main__":
	import sys

	app = QtWidgets.QApplication(sys.argv)
	app.setApplicationName('MyWindow')

	main = MyWindow()
	main.show()

	sys.exit(app.exec_())