
# In the future I will import the .ui file instead of converting it to .py so that I can make changes to it

from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from main import Ui_main_window
from pynput import keyboard
# from keyboard import _listener
import time
code_line_placeholdertext = "Type in Code"
def wait(ms):
    QtTest.QTest.qWait(ms)



class Ui_login_window(object):

    code = "1234"

    def on_press(self, key):
        if key == keyboard.Key.esc:
            print("exited listener")
            return False  # stop listener
        if key == keyboard.Key.enter:
            self.openWindow()
            if self.code_line.text() == Ui_login_window.code:
                print("closed listener")
                return False

    def openWindow(self):
        if self.code_line.text() == Ui_login_window.code:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_main_window()
            self.ui.setupUi(self.window)
            self.window.show()
            login_window.destroy()
        else:
            self.code_line.clear()
            self.code_line.setPlaceholderText("Wrong")
            wait(1000)
            self.code_line.setPlaceholderText(code_line_placeholdertext)

    def setupUi(self, login_window):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()
        # listener.start()  # start to listen on a separate thread
        # listener.join()  # remove if main thread is polling self.keys
        login_window.setObjectName("login_window")
        login_window.resize(229, 108)
        self.centralwidget = QtWidgets.QWidget(login_window)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 230, 110))
        self.frame.setStyleSheet("background-color:rgb(113, 113, 113)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(120, 54, 60, 23))
        self.login_button.setObjectName("login_button")
        self.login_button.clicked.connect(self.openWindow)
        self.code_line = QtWidgets.QLineEdit(self.centralwidget)
        self.code_line.setGeometry(QtCore.QRect(50, 30, 130, 20))
        self.code_line.setText("")
        self.code_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.code_line.setObjectName("code_line")
        login_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(login_window)
        QtCore.QMetaObject.connectSlotsByName(login_window)

    def retranslateUi(self, login_window):
        _translate = QtCore.QCoreApplication.translate
        login_window.setWindowTitle(_translate("login_window", "Login"))
        self.login_button.setText(_translate("login_window", "Login"))
        self.code_line.setPlaceholderText(_translate("login_window", code_line_placeholdertext))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_window = QtWidgets.QMainWindow()
    ui = Ui_login_window()
    ui.setupUi(login_window)
    login_window.show()
    sys.exit(app.exec_())
