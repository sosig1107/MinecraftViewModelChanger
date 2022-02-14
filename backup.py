from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        self.menuDatei = QtWidgets.QMenu(self.menubar)
        self.menuDatei.setObjectName("menuDatei")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setEnabled(True)
        self.statusbar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(main_window)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(main_window)
        self.actionSave.setObjectName("actionSave")
        self.menuDatei.addAction(self.actionOpen)
        self.actionOpen.triggered.connect(self.openFile)
        self.menuDatei.addAction(self.actionSave)
        self.menubar.addAction(self.menuDatei.menuAction())
        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)


    def openFile(self):
        # QFileDialog.getOpenFileUrl(directory="C:\\Users\\sscholz\\AppData\\Roaming\\")
        # QFileDialog.getOpenFileNames(filter="All Files (*);;JSON (*.json)",
                                    # directory="C:\\Users\\sscholz\\AppData\\Roaming\\")
        fname = QFileDialog.getExistingDirectory(directory="C:\\Users\\sscholz\\AppData\\Roaming\\")
        if fname:
            print(fname)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "MainWindow"))
        self.menuDatei.setTitle(_translate("main_window", "File"))
        self.actionOpen.setText(_translate("main_window", "Open"))
        self.actionOpen.setShortcut(_translate("main_window", "Ctrl+O"))
        self.actionSave.setText(_translate("main_window", "Save"))
        self.actionSave.setShortcut(_translate("main_window", "Ctrl+S"))


    def testing(self):
        print("ja")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
