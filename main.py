import threading
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
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
        fname = QFileDialog.getExistingDirectory(directory="C:\\Users\\sscholz\\AppData\\Roaming\\")
        # print(fname)

# initialize the app
app = QApplication(sys.argv)
UIWindow = MainWindow()
app.exec_()
