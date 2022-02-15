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

        val = 1000

        self.PosX.setMinimum(val)
        self.PosX.setMaximum(val)
        self.PosY.setMinimum(val)
        self.PosY.setMaximum(val)
        self.PosZ.setMinimum(val)
        self.PosZ.setMaximum(val)

        self.RotX.setMinimum(val)
        self.RotX.setMaximum(val)
        self.RotY.setMinimum(val)
        self.RotY.setMaximum(val)
        self.RotZ.setMinimum(val)
        self.RotZ.setMaximum(val)

        self.ScaleX.setMinimum(val)
        self.ScaleX.setMaximum(val)
        self.ScaleY.setMinimum(val)
        self.ScaleY.setMaximum(val)
        self.ScaleZ.setMinimum(val)
        self.ScaleZ.setMaximum(val)

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
        self.fpath = QFileDialog.getExistingDirectory(directory=r"C:\Users\Stephen\AppData\Roaming\.minecraft\resourcepacks")
        self.editLine()
        # print(fname)

    def editLine(self):
        a_file = open(fr"{self.fpath}\assets\minecraft\models\item\diamond_axe.json", "r")
        lines = a_file.readlines()

        # self.xinput.value = lines[39]

        # Pos
        pos = lines[39].replace('"', "").replace("translation:", "").replace(',', "").replace("[", "") \
            .replace("]", "").lstrip().rstrip()
        posx = pos.split()[0]
        posy = pos.split()[1]
        posz = pos.split()[2]
        self.PosX.setValue(float(posx))
        self.PosY.setValue(float(posy))
        self.PosZ.setValue(float(posz))

        # Rot
        rot = lines[38].replace('"', "").replace("rotation:", "").replace(',', "").replace("[", "") \
            .replace("]", "").lstrip().rstrip()
        rotx = rot.split()[0]
        roty = rot.split()[1]
        rotz = rot.split()[2]
        self.RotX.setValue(float(rotx))
        self.RotY.setValue(float(roty))
        self.RotZ.setValue(float(rotz))

        # Scale
        print(lines[40].replace('"', ""))
        scale = lines[40].replace('"', "").replace("scale:", "").replace(',', "").replace("[", "") \
            .replace("]", "").lstrip().rstrip()
        scalex = scale.split()[0]
        scaley = scale.split()[1]
        scalez = scale.split()[2]
        self.ScaleX.setValue(float(scalex))
        self.ScaleY.setValue(float(scaley))
        self.ScaleZ.setValue(float(scalez))

# initialize the app
app = QApplication(sys.argv)
UIWindow = MainWindow()
app.exec_()
