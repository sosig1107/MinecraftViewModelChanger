import runpy
import threading
import time

import PyQt5
from PyQt5 import QtWidgets, QtTest
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PySide2.QtCore import QRect
import sys
from pynput import keyboard

def wait(ms):
    QtTest.QTest.qWait(ms)
code = "123"



class LoginScreen(QMainWindow):
    def __init__(self):
        super(LoginScreen, self).__init__()
        uic.loadUi("login.ui", self)

        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

        # Define assets
        self.loginButton = self.findChild(QPushButton, "login_button")
        self.code_line = self.findChild(QLineEdit, "code_line")
        self.lockPicture = self.findChild(QLabel, "lockpicture")
        # self.bt1 = self.findChild(QPushButton, "pushButton")

        #Do stuff
        # self.bt1.clicked.connect(self.clicked)
        self.loginButton.clicked.connect(self.openWindow)
        self.lockPicture.setPixmap(QPixmap("lockRed.ico"))
        self.lockpicture.setGeometry(0, 0, 30, 30)
        # self.lockpicture.setPixmap(QtGui.QPixmap("lockRed.ico"))
        self.lockPicture.setScaledContents(True)
        self.code_line.enterEvent(self.openWindow())

        # self.loginButton.clicked.connect(self.openWindow)

        # Render
        LoginScreen.show(self)
        # self.show()

    def openWindow(self):
        print(self.code_line.text())
        if self.code_line.text() == code:
            t1 = threading.Thread(target=self.importit())
            t2 = threading.Thread(target=self.destroy())
            t1, t2 .start()
        else:
            self.code_line.clear()
            self.code_line.setPlaceholderText("Wrong")
            wait(1000)
            self.code_line.setPlaceholderText("Type in Code")

    def importit(self):
        import main

    def on_press(self, key):
        if key == keyboard.Key.esc:
            print("Exiting...")
            return False
        if key == keyboard.Key.enter:
            if self.code_line.text() == code:
                print("Listener closed...")
                return False, self.openWindow()



# initialize the app
app = QApplication(sys.argv)
# UIWindow = LoginScreen()
window = LoginScreen()
app.exec_()
