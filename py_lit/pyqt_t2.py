import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QVBoxLayout
class HLayout(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(self,parent)

        button1 = QtWidgets.QPushButton("1")
        button2 = QtWidgets.QPushButton("2")
        button3 = QtWidgets.QPushButton("3")
        button4 = QtWidgets.QPushButton("4")
        button5 = QtWidgets.QPushButton("5")

        hbox = QtWidgets.QHBoxLayout()
        hbox.addStretch(10)
        hbox.addWidget(button1)
        hbox.addWidget(button2)
        hbox.addWidget(button3)
        hbox.addWidget(button4)
        hbox.addWidget(button5)

        self.setLayout(hbox)
        self.setWindowTitle('box layout')
        self.resize(300, 400)

app = QtWidgets.QApplication(sys.argv)
ex = HLayout()
ex.show()
sys.exit(app.exec_())
