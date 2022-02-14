import runpy
import threading
from PyQt5 import QtWidgets, QtTest
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

def wait(ms):
    QtTest.QTest.qWait(ms)
code = "123"

class LoginScreen(QMainWindow):
    def __init__(self):
        super(LoginScreen, self).__init__()
        uic.loadUi("login.ui", self)

        # Define assets
        self.loginButton = self.findChild(QPushButton, "login_button")
        self.code_line = self.findChild(QLineEdit, "code_line")
        # self.bt1 = self.findChild(QPushButton, "pushButton")

        #Do stuff
        # self.bt1.clicked.connect(self.clicked)
        self.loginButton.clicked.connect(self.openWindow)
        # self.loginButton.clicked.connect(self.openWindow)

        # Render
        LoginScreen.show(self)
        # self.show()

    def openWindow(self):
        print(self.code_line.text())
        if self.code_line.text() == code:
            t1 = threading.Thread(target=self.importit())
            t2 = threading.Thread(target=self.destroy())
            t1.start()
            t2.start()
        else:
            self.code_line.clear()
            self.code_line.setPlaceholderText("Wrong")
            wait(1000)
            self.code_line.setPlaceholderText("Type in Code")

    def importit(self):
        import main

# initialize the app
app = QApplication(sys.argv)
# UIWindow = LoginScreen()
window = LoginScreen()
app.exec_()
