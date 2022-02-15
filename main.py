import json
import threading
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon
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
        self.pickaxeLabel = self.findChild(QLabel, "pickaxeLabel")
        self.PosX = self.findChild(QDoubleSpinBox, "PosX")
        self.PosY = self.findChild(QDoubleSpinBox, "PosY")
        self.PosZ = self.findChild(QDoubleSpinBox, "PosZ")
        self.RotX = self.findChild(QDoubleSpinBox, "RotX")
        self.RotY = self.findChild(QDoubleSpinBox, "RotY")
        self.RotZ = self.findChild(QDoubleSpinBox, "RotZ")
        self.ScaleX = self.findChild(QDoubleSpinBox, "ScaleX")
        self.ScaleY = self.findChild(QDoubleSpinBox, "ScaleY")
        self.ScaleZ = self.findChild(QDoubleSpinBox, "ScaleZ")

        self.PosX.setMinimum(-500)
        self.PosX.setMaximum(500)
        self.PosY.setMinimum(-500)
        self.PosY.setMaximum(500)
        self.PosZ.setMinimum(-500)
        self.PosZ.setMaximum(500)

        self.RotX.setMinimum(-500)
        self.RotX.setMaximum(500)
        self.RotY.setMinimum(-500)
        self.RotY.setMaximum(500)
        self.RotZ.setMinimum(-500)
        self.RotZ.setMaximum(500)

        self.ScaleX.setMinimum(-500)
        self.ScaleX.setMaximum(500)
        self.ScaleY.setMinimum(-500)
        self.ScaleY.setMaximum(500)
        self.ScaleZ.setMinimum(-500)
        self.ScaleZ.setMaximum(500)

        self.menuDatei.addAction(self.actionOpen)
        self.actionOpen.triggered.connect(self.openFile)
        self.menuDatei.addAction(self.actionSave)
        self.menubar.addAction(self.menuDatei.menuAction())
        #Do stuff
        self.bt1.clicked.connect(self.clicked)
        self.pickaxeLabel.setPixmap(QPixmap("pickaxe.png"))
        # self.lockpicture.setGeometry(0, 0, 30, 30)
        self.pickaxeLabel.setScaledContents(True)
        # Render
        self.show()

        self.fpath = ""

    def clicked(self):

        tools = ["sword", "axe", "pickaxe", "shovel", "hoe"]
        types = ["wooden", "stone", "iron", "golden", "diamond", "netherite"]
        files = []

        for x in types:
            for y in tools:
                files.append(rf"{self.fpath}\assets\minecraft\models\item\{x}_{y}.json")
                # print(x + y)
        for x in files:
            a_file = open(x, "r")
            lines = a_file.readlines()
            # Position
            lines[
                39] = f"            \"translation\": 	[ {self.PosX.value()}, {self.PosY.value()}, {self.PosZ.value()}],\n"
            # Rotation
            lines[
                38] = f"            \"rotation\": 	[ {self.RotX.value()}, {self.RotY.value()}, {self.RotZ.value()} ],\n"
            # Scale
            lines[
                40] = f"            \"scale\": 		[ {self.ScaleX.value()}, {self.ScaleY.value()}, {self.ScaleZ.value()} ]\n"

            a_file = open(x, "w")
            a_file.writelines(lines)
            a_file.close()


    def openFile(self):
        self.fpath = QFileDialog.getExistingDirectory(directory=r"C:\Users\sscho\Downloads")
        self.editLine()
        # print(fname)

    def editLine(self):
        a_file = open(fr"{self.fpath}\assets\minecraft\models\item\diamond_axe.json", "r")
        lines = a_file.readlines()

        # self.xinput.value = lines[39]

        # Pos
        pos = lines[39].replace('"', "").replace("            translation: 	", "").replace(',', "").replace("[", "") \
            .replace("]", "").lstrip().rstrip()
        posx = pos[0:4]
        posy = pos[5:9]
        posz = pos[10:14]
        self.PosX.setValue(float(posx))
        self.PosY.setValue(float(posy))
        self.PosZ.setValue(float(posz))

        # Rot
        rot = lines[38].replace('"', "").replace("            rotation: 	", "").replace(',', "").replace("[", "") \
            .replace("]", "").lstrip().rstrip()

        self.RotX.setMinimum(-200)
        self.RotY.setMinimum(-200)
        self.RotZ.setMinimum(-200)

        rotx = rot.split()[0]
        roty = rot.split()[1]
        rotz = rot.split()[2]
        self.RotX.setValue(int(rotx))
        self.RotY.setValue(int(roty))
        self.RotZ.setValue(int(rotz))

        # Scale
        print(lines[40].replace('"', ""))
        scale = lines[40].replace('"', "").replace("            scale: 	", "").replace(',', "").replace("[", "") \
            .replace("]", "").lstrip().rstrip()
        scalex = scale[0:4]
        scaley = scale[5:9]
        scalez = scale[10:14]
        self.ScaleX.setValue(float(scalex))
        self.ScaleY.setValue(float(scaley))
        self.ScaleZ.setValue(float(scalez))

# initialize the app
app = QApplication(sys.argv)
UIWindow = MainWindow()
app.exec_()
