
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(900, 600)
        main_window.setStyleSheet(".QPushButton\n"
"{\n"
"    transition-duration: 1s;\n"
"}\n"
"\n"
".QPushButton:hover\n"
"{\n"
"  box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);\n"
"    background-color:red;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 500, 201, 71))
        self.pushButton.setStyleSheet("")
        self.pushButton.setAutoDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clicker)
        self.zinput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.zinput.setGeometry(QtCore.QRect(60, 330, 62, 22))
        self.zinput.setObjectName("zinput")
        self.yInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.yInput.setGeometry(QtCore.QRect(60, 290, 62, 22))
        self.yInput.setObjectName("yInput")
        self.xInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.xInput.setGeometry(QtCore.QRect(60, 250, 62, 22))
        self.xInput.setObjectName("xInput")
        self.pickaxeLabel = QtWidgets.QLabel(self.centralwidget)
        self.pickaxeLabel.setGeometry(QtCore.QRect(400, 150, 270, 260))
        self.pickaxeLabel.setText("")
        self.pickaxeLabel.setPixmap(QtGui.QPixmap("./pickaxe.png"))
        self.pickaxeLabel.setScaledContents(True)
        self.pickaxeLabel.setObjectName("pickaxeLabel")
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        self.menuDatei = QtWidgets.QMenu(self.menubar)
        self.menuDatei.setObjectName("menuDatei")
        main_window.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(main_window)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(main_window)
        self.actionSave.setObjectName("actionSave")
        self.menuDatei.addAction(self.actionOpen)
        self.menuDatei.addAction(self.actionSave)
        self.menubar.addAction(self.menuDatei.menuAction())

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def clicker(self):
        tools = ["sword", "axe", "pickaxe", "shovel", "hoe"]
        types = ["wooden", "stone", "iron", "golden", "diamond", "netherite"]

        for x in types:
            for y in tools:
                print(f"{types[x]}_{tools[y]}")

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "MainWindow"))
        self.pushButton.setText(_translate("main_window", "Apply"))
        self.menuDatei.setTitle(_translate("main_window", "File"))
        self.actionOpen.setText(_translate("main_window", "Open"))
        self.actionOpen.setShortcut(_translate("main_window", "Ctrl+O"))
        self.actionSave.setText(_translate("main_window", "Save"))
        self.actionSave.setShortcut(_translate("main_window", "Ctrl+S"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(login_window)
    login_window.show()
    sys.exit(app.exec_())
