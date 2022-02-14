from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.initme()

    def initme(self):
        self.setGeometry(0,0,900,600)
        # self.menuBar().findChild()


        # Load Ui
        uic.loadUi("main.ui", self)

        # Define assets
        self.bt1 = self.findChild(QPushButton, "pushButton")

        self.menuDatei = self.findChild(QMenu, "menuDatei")
        self.actionOpen = self.findChild(QAction, "actionOpen")
        self.actionSave = self.findChild(QAction, "actionSave")
        self.menuDatei.addAction(self.actionOpen)
        self.actionOpen.triggered.connect(self.openFile)
        self.menuDatei.addAction(self.actionSave)
        self.menubar.addAction(self.menuDatei.menuAction())

        #Do stuff
        self.bt1.clicked.connect(self.clicked)

        # Render
        self.show()

    def clicked(self):
        print("hi")

    def openFile(self):
        # QFileDialog.getOpenFileUrl(directory="C:\\Users\\sscholz\\AppData\\Roaming\\")
        # QFileDialog.getOpenFileNames(filter="All Files (*);;JSON (*.json)",
                                    # directory="C:\\Users\\sscholz\\AppData\\Roaming\\")
        fname = QFileDialog.getExistingDirectory(directory="C:\\Users\\sscholz\\AppData\\Roaming\\")
        if fname:
            print(fname)

# initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
