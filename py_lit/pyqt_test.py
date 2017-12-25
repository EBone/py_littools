from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QHBoxLayout,QDialog,QWidget,QTabWidget,QTabBar
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor
#from PyQt5.QtGui import

class window(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

        dialog=QDialog(self)

        self.setGeometry(200,200,1000,1000)
        tab=QTabWidget()
        tab.setWindowTitle("hahah")
        button=QPushButton("fuck")
        button2=QPushButton("fuckthat")
        #tab.addTab(button,"Button")
        tab.addTab(button, "Button2")
        t=QTabBar()
        t.setTabTextColor(0,QColor(0,0,0))
        t.setTabText(0,"fsdfasdfasf")
        tab.addTab(t,'asdfas')
        tab.addTab(button2,"fucktaht")
        # tab2 = QTabWidget()
        # tab2.setWindowTitle("hahah")
        # button2 = QPushButton("fuck2")
        # tab2.addTab(button2, "Button")


        #button.setGeometry(100,100,500,500)
        button.clicked.connect(self.onclick)
        layout=QHBoxLayout()
       # layout.addStretch(10)
        layout.addWidget(tab)
        # layout.addWidget(tab2)

        self.setLayout(layout)
        #self.setCentralWidget(button)
        self.setWindowTitle("fsdfasdfsf")

    @pyqtSlot()
    def onclick(self):
        print("dfasdfasfas")
        self.setGeometry(200, 200, 500, 500)

if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)

    w=window()
    w.show()
    sys.exit(app.exec_())

