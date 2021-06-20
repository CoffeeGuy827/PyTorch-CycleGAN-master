from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import glob
import os
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

#test

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        originalPath = "/home/daniel/Downloads/PyTorch-CycleGAN-master/datasets/train/a/*.jpg"
        self.originalImages = glob.glob(originalPath)
        self.countImage = 0;

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(10, 20, 761, 651))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.photo.setFont(font)
        self.photo.setFrameShape(QtWidgets.QFrame.Panel)
        self.photo.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.photo.setLineWidth(5)
        self.photo.setMidLineWidth(0)
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        self.browseFile = QtWidgets.QPushButton(self.centralwidget)
        self.browseFile.setGeometry(QtCore.QRect(350, 700, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.browseFile.setFont(font)
        self.browseFile.setObjectName("Next")
        self.browseFile.clicked.connect(self.browse_file)

        #category
        self.c1 = QtWidgets.QPushButton(self.centralwidget)
        self.c1.setGeometry(QtCore.QRect(1050, 700, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.c1.setFont(font)
        self.c1.setObjectName("Next")
        # self.c1.clicked.connect(self.browse_file)

        self.c2 = QtWidgets.QPushButton(self.centralwidget)
        self.c2.setGeometry(QtCore.QRect(1230, 700, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.c2.setFont(font)
        self.c2.setObjectName("Next")
        # self.c1.clicked.connect(self.browse_file)

        self.c3 = QtWidgets.QPushButton(self.centralwidget)
        self.c3.setGeometry(QtCore.QRect(1410, 700, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.c3.setFont(font)
        self.c3.setObjectName("Next")
        # self.c1.clicked.connect(self.browse_file)

        self.c4 = QtWidgets.QPushButton(self.centralwidget)
        self.c4.setGeometry(QtCore.QRect(1050, 750, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.c4.setFont(font)
        self.c4.setObjectName("Next")

        self.c5 = QtWidgets.QPushButton(self.centralwidget)
        self.c5.setGeometry(QtCore.QRect(1230, 750, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.c5.setFont(font)
        self.c5.setObjectName("Next")

        self.c6 = QtWidgets.QPushButton(self.centralwidget)
        self.c6.setGeometry(QtCore.QRect(1410, 750, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.c6.setFont(font)
        self.c6.setObjectName("Next")


        self.predict = QtWidgets.QPushButton(self.centralwidget)
        self.predict.setGeometry(QtCore.QRect(700, 750, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.predict.setFont(font)
        self.predict.setObjectName("Generation")
        self.predict.clicked.connect(self.show_predict)

        self.photo2 = QtWidgets.QLabel(self.centralwidget)
        self.photo2.setGeometry(QtCore.QRect(790, 20, 791, 651))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.photo2.setFont(font)
        self.photo2.setFrameShape(QtWidgets.QFrame.Panel)
        self.photo2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.photo2.setLineWidth(5)
        self.photo2.setScaledContents(True)
        self.photo2.setObjectName("photo2")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(520, 700, 521, 31))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.photo.setText(_translate("MainWindow", "INPUT"))
        self.browseFile.setText(_translate("MainWindow", "Next"))
        self.c1.setText(_translate("MainWindow", "Floral"))
        self.c2.setText(_translate("MainWindow", "Tiedye"))
        self.c3.setText(_translate("MainWindow", "Mesh"))
        self.c4.setText(_translate("MainWindow", "Denim"))
        self.c5.setText(_translate("MainWindow", "Baroque"))
        self.c6.setText(_translate("MainWindow", "Striped"))
        self.predict.setText(_translate("MainWindow", "Generation"))
        self.photo2.setText(_translate("MainWindow", "OUTPUT"))

    def browse_file(self):
        # directory = QtWidgets.QFileDialog.getOpenFileName(None, "Browse File", "", "PNG (*.PNG *.png")[0]
        # print(directory)
        # pixmap = QtGui.QPixmap(directory)
        # original
        directory = self.originalImages[self.countImage]
        pixmap = QtGui.QPixmap(directory)
        self.photo.setPixmap(pixmap.scaled(self.photo.size()))
        self.lineEdit.setText("Image : " + str(self.countImage))
        self.countImage += 1

        newPath = "/home/daniel/Downloads/PyTorch-CycleGAN-master/output/A/*.png"
        self.newImages = glob.glob(newPath)

        # generation
        directory = self.newImages[self.countImage]
        pixmap = QtGui.QPixmap(directory)
        self.photo2.setPixmap(pixmap.scaled(self.photo.size()))

    def floral(self):
        newPath = "/home/daniel/Downloads/PyTorch-CycleGAN-master/output/A/*.png"
        self.f = glob.glob(newPath)

        # generation
        directory = self.floral[self.countImage]
        pixmap = QtGui.QPixmap(directory)
        self.photo2.setPixmap(pixmap.scaled(self.photo.size()))

    def tiedie(self):
        newPath = "/home/daniel/Downloads/PyTorch-CycleGAN-master/output/B/*.png"
        self.t = glob.glob(newPath)

        # generation
        directory = self.floral[self.countImage]
        pixmap = QtGui.QPixmap(directory)
        self.photo2.setPixmap(pixmap.scaled(self.photo.size()))

    def mesh(self):
        newPath = "/home/daniel/Downloads/PyTorch-CycleGAN-master/output/C/*.png"
        self.m = glob.glob(newPath)

        # generation
        directory = self.floral[self.countImage]
        pixmap = QtGui.QPixmap(directory)
        self.photo2.setPixmap(pixmap.scaled(self.photo.size()))

    def denim(self):
        newPath = "/home/daniel/Downloads/PyTorch-CycleGAN-master/output/D/*.png"
        self.d = glob.glob(newPath)

        # generation
        directory = self.floral[self.countImage]
        pixmap = QtGui.QPixmap(directory)
        self.photo2.setPixmap(pixmap.scaled(self.photo.size()))

    def baroque(self):
        newPath = "/home/daniel/Downloads/PyTorch-CycleGAN-master/output/E/*.png"
        self.b = glob.glob(newPath)

        # generation
        directory = self.floral[self.countImage]
        pixmap = QtGui.QPixmap(directory)
        self.photo2.setPixmap(pixmap.scaled(self.photo.size()))

    def striped(self):
        newPath = "/home/daniel/Downloads/PyTorch-CycleGAN-master/output/F/*.png"
        self.s = glob.glob(newPath)

        # generation
        directory = self.floral[self.countImage]
        pixmap = QtGui.QPixmap(directory)
        self.photo2.setPixmap(pixmap.scaled(self.photo.size()))


    def _set_text(self, text):
        return text

    def show_predict(self):
        os.system("python3 ./test --dataroot datasets/ --cuda" )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())