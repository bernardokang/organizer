# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'committerUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets







class Ui_MainWindow(object):


    ###버튼엮기 슬롯 ::recursion;;;
    def download(self):

        if self.pushButton_13.clicked:
            print('btn clicked!')
            self.completed = 0
            self.a = self.completed+15
            print(self.a)
            return self.a



        # return self.a






    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(522, 416)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 340, 491, 51))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(140, 20, 241, 16))
        self.label_9.setObjectName("label_9")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(170, 56, 57, 22))
        self.pushButton_13.setStyleSheet("QPushButton{\n"
"    border: 3px solid moccasin;\n"
"    border-radius: 5px;\n"
"    background-color: lightpink;\n"
"    text-align: center;\n"
"    color: white\n"
"}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(170, 220, 57, 22))
        self.pushButton_17.setStyleSheet("QPushButton{\n"
"    border: 3px solid moccasin;\n"
"    border-radius: 5px;\n"
"    background-color: lightpink;\n"
"    text-align: center;\n"
"    color: white\n"
"}")
        self.pushButton_17.setObjectName("pushButton_17")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(22, 56, 146, 22))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    border: 1px solid moccasin;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    background-color: powderblue;\n"
"    width: 14px;\n"
"    margin: 1px;\n"
"}")
        # self.progressBar.setProperty("value", 0)
        self.progressBar.setValue(self.download())
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(170, 138, 57, 22))
        self.pushButton_15.setStyleSheet("QPushButton{\n"
"    border: 3px solid moccasin;\n"
"    border-radius: 5px;\n"
"    background-color: lightpink;\n"
"    text-align: center;\n"
"    color: white\n"
"}")
        self.pushButton_15.setObjectName("pushButton_15")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(22, 97, 146, 22))
        self.progressBar_2.setAutoFillBackground(False)
        self.progressBar_2.setStyleSheet("QProgressBar{\n"
"    border: 1px solid moccasin;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    background-color: powderblue;\n"
"    width: 14px;\n"
"    margin: 1px;\n"
"}")
        self.progressBar_2.setProperty("value", 15)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_3.setGeometry(QtCore.QRect(22, 138, 146, 22))
        self.progressBar_3.setAutoFillBackground(False)
        self.progressBar_3.setStyleSheet("QProgressBar{\n"
"    border: 1px solid moccasin;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    background-color: powderblue;\n"
"    width: 14px;\n"
"    margin: 1px;\n"
"}")
        self.progressBar_3.setProperty("value", 15)
        self.progressBar_3.setTextVisible(False)
        self.progressBar_3.setObjectName("progressBar_3")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(170, 179, 57, 22))
        self.pushButton_16.setStyleSheet("QPushButton{\n"
"    border: 3px solid moccasin;\n"
"    border-radius: 5px;\n"
"    background-color: lightpink;\n"
"    text-align: center;\n"
"    color: white\n"
"}")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(170, 97, 57, 22))
        self.pushButton_14.setStyleSheet("QPushButton{\n"
"    border: 3px solid moccasin;\n"
"    border-radius: 5px;\n"
"    background-color: lightpink;\n"
"    text-align: center;\n"
"    color: white\n"
"}")
        self.pushButton_14.setObjectName("pushButton_14")
        self.progressBar_7 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_7.setGeometry(QtCore.QRect(22, 302, 146, 22))
        self.progressBar_7.setAutoFillBackground(False)
        self.progressBar_7.setStyleSheet("QProgressBar{\n"
"    border: 1px solid moccasin;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    background-color: powderblue;\n"
"    width: 14px;\n"
"    margin: 1px;\n"
"}")
        self.progressBar_7.setProperty("value", 15)
        self.progressBar_7.setTextVisible(False)
        self.progressBar_7.setObjectName("progressBar_7")
        self.progressBar_4 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_4.setGeometry(QtCore.QRect(22, 179, 146, 22))
        self.progressBar_4.setAutoFillBackground(False)
        self.progressBar_4.setStyleSheet("QProgressBar{\n"
"    border: 1px solid moccasin;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    background-color: powderblue;\n"
"    width: 14px;\n"
"    margin: 1px;\n"
"}")
        self.progressBar_4.setProperty("value", 15)
        self.progressBar_4.setTextVisible(False)
        self.progressBar_4.setObjectName("progressBar_4")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(170, 261, 57, 22))
        self.pushButton_18.setStyleSheet("QPushButton{\n"
"    border: 3px solid moccasin;\n"
"    border-radius: 5px;\n"
"    background-color: lightpink;\n"
"    text-align: center;\n"
"    color: white\n"
"}")
        self.pushButton_18.setObjectName("pushButton_18")
        self.progressBar_6 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_6.setGeometry(QtCore.QRect(22, 261, 146, 22))
        self.progressBar_6.setAutoFillBackground(False)
        self.progressBar_6.setStyleSheet("QProgressBar{\n"
"    border: 1px solid moccasin;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    background-color: powderblue;\n"
"    width: 14px;\n"
"    margin: 1px;\n"
"}")
        self.progressBar_6.setProperty("value", 15)
        self.progressBar_6.setTextVisible(False)
        self.progressBar_6.setObjectName("progressBar_6")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(170, 302, 57, 22))
        self.pushButton_19.setStyleSheet("QPushButton{\n"
"    border: 3px solid moccasin;\n"
"    border-radius: 5px;\n"
"    background-color: lightpink;\n"
"    text-align: center;\n"
"    color: white\n"
"}")
        self.pushButton_19.setObjectName("pushButton_19")
        self.progressBar_5 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_5.setGeometry(QtCore.QRect(22, 220, 146, 22))
        self.progressBar_5.setAutoFillBackground(False)
        self.progressBar_5.setStyleSheet("QProgressBar{\n"
"    border: 1px solid moccasin;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    background-color: powderblue;\n"
"    width: 14px;\n"
"    margin: 1px;\n"
"}")
        self.progressBar_5.setProperty("value", 15)
        self.progressBar_5.setTextVisible(False)
        self.progressBar_5.setObjectName("progressBar_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(231, 223, 281, 16))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(231, 182, 281, 16))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(231, 305, 281, 16))
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(231, 59, 271, 16))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(231, 141, 271, 16))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(231, 264, 281, 16))
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(231, 100, 271, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)







        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_13.clicked.connect(self.download)





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_8.setText(_translate("MainWindow", " $ready? motion, fcpx, logic by project44"))
        self.label_9.setText(_translate("MainWindow", "*--palette committer--* v1.0 project44"))
        self.pushButton_13.setText(_translate("MainWindow", "Commit!"))
        self.pushButton_17.setText(_translate("MainWindow", "Commit!"))
        self.pushButton_15.setText(_translate("MainWindow", "Commit!"))
        self.pushButton_16.setText(_translate("MainWindow", "Commit!"))
        self.pushButton_14.setText(_translate("MainWindow", "Commit!"))
        self.pushButton_18.setText(_translate("MainWindow", "Commit!"))
        self.pushButton_19.setText(_translate("MainWindow", "Commit!"))
        self.label_5.setText(_translate("MainWindow", "영최적화"))
        self.label_4.setText(_translate("MainWindow", "빛생명색채"))
        self.label_7.setText(_translate("MainWindow", "python&ruby cheatsheet"))
        self.label.setText(_translate("MainWindow", "maya cheatsheet"))
        self.label_3.setText(_translate("MainWindow", "논리학 cheatsheet"))
        self.label_6.setText(_translate("MainWindow", "Rigging cheatsheet"))
        self.label_2.setText(_translate("MainWindow", "SQL cheatsheet"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

