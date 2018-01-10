# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtpLabel.ui'
#
# Created by: PyQt5 UI code generator 5.9
# Designed by: Project44, open PyCharm by folder; not by file;
#
# WARNING! All changes made in this file will be lost!



# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QProgressBar, QPushButton, QApplication)
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QHBoxLayout
import sys


temp = 56.82

#init Number

#파이썬마야
mp = 47

#애프터이펙트
ae = 281

#아놀드
arnold = 50

#장고
dj =50

#영어
eng = 1000

#불어
fr = 200

#그릴걸스
grilgirl =300

#HUD
hud = 25

#마야파이썬
pythonmaya = 51

#후디니
hd = 1

#남국실강
#rigging 101
rgg = 23.51
#왕초보메뉴강의
cb = 100
#파이썬깐깐해
tg = 0
#자바스크립트
js = 100
#장고걸스
djg = 26.67
#두들낙서
dd= 7.04
#영상최적화(이건 계산없이 직접 써줌)
kv = 100
#자료구조
ds = 20
#칼라마스터
#라피드리그 튜토리얼
#논리학
lg = 100
#읽기
#소셜스터디
#중국어
#이태리어
#소요리
#보컬
#sqldb
sql = 100

#마리
ai = 100

#빛생명색체
lt= 100

#RUBY&PYTHON&PAYNE&기타등등
pr = 39.37

#이쁜iOS
os =0

#쏙청
ec=90.10

#글로벌 기능
# def showYourState():
#     f = open('db/pythonmayadb.py', 'r')
#     db = f.readlines()
#     lena =len(db)
#     return lena


#
# x = (showYourState()/pythonmaya)*100
# y = "%.2f" % x

# 버튼을 누를 때 일어나는 일들
# class Clickevent():
#     def updateDB(self):
#         f = open('db/pythonmayadb.py', 'a')
#         comment = input("덴버, 코멘트를 입력할 수 있어")
#         data = comment+"\n"
#         f.write(data)


#버튼을 누를 때 일어나는 일들 2017.12.15업뎃slot
# class buttonClicked():






# 엮는다 시그널조합
# self.pushButton.clicked.connect(self.updateDB)





#스타일시트
COMPLETED_STYLE = """
QProgressBar{
    border: 2px dotted white;
    border-radius: 5px;
    text-align: center
}

QProgressBar::chunk {
    background-color: lightpink;
    width: 1px;
    margin: 1px;
}
"""

COMPLETED_STYLE2 = """
QProgressBar{
    border: 2px dotted white;
    border-radius: 5px;
    text-align: center
}

QProgressBar::chunk {
    background-color: skyblue;
    width: 1px;
    margin: 1px;
}
"""


class Ui_MainWindow(object):
    def updateTable(*args): #악스는 진짜 신의 한수구나
        #self.pushButton_7했는데 셀프가 낫디파인드 문제가 생겼었음, 이것은 인스턴스의 문제다 고로,, 인스턴스를 제대로 써준다
        if ui.pushButton_7.clicked:
            global cb
            cb += 20
            #왜 이렇게 해도 안되는걸까, 근데 글로발 키워드라도 쓸 수 있게 됐네



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1057, 745)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")



        #maya python버튼이용
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setStyleSheet(COMPLETED_STYLE)

        #self.progressBar.setStyleSheet :: 원칙에 충실해. 스탯과 메쏘드를 가진다는 원칙이지!

        self.progressBar.setGeometry(QtCore.QRect(40, 66, 191, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")




        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 90, 200, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(34, 84, 60, 32))
        self.pushButton.setObjectName("pushButton")


        #엮는다
        # self.pushButton.clicked.connect(Clickevent.updateDB)
        #이 부분 클릭이벤트클라쓰랑 해서 바꿀필요가 있




###여긴 레이아웃
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 46, 160, 16))
        self.label.setObjectName("label")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(40, 118, 191, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 142, 170, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(34, 136, 60, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(34, 190, 60, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(99, 198, 160, 16))
        self.label_4.setObjectName("label_4")
        self.progressBar_3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_3.setGeometry(QtCore.QRect(40, 172, 191, 23))
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(35, 244, 60, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(99, 250, 160, 16))
        self.label_5.setObjectName("label_5")
        self.progressBar_4 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_4.setGeometry(QtCore.QRect(40, 226, 191, 23))
        self.progressBar_4.setProperty("value", 0)
        self.progressBar_4.setObjectName("progressBar_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(34, 301, 60, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 307, 160, 16))
        self.label_6.setObjectName("label_6")
        self.progressBar_5 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_5.setGeometry(QtCore.QRect(40, 283, 191, 23))
        self.progressBar_5.setProperty("value", mp)
        self.progressBar_5.setObjectName("progressBar_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(34, 360, 60, 32))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(100, 366, 170, 16))
        self.label_7.setObjectName("label_7")
        self.progressBar_6 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_6.setGeometry(QtCore.QRect(40, 342, 191, 23))
        self.progressBar_6.setProperty("value", rgg)
        self.progressBar_6.setObjectName("progressBar_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(34, 412, 60, 32))
        self.pushButton_7.setObjectName("pushButton_7")
        #버튼 7번과 엮기 슬랏시그널
        self.pushButton_7.clicked.connect(self.updateTable)


        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(100, 418, 160, 16))
        self.label_8.setObjectName("label_8")
        self.progressBar_7 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_7.setGeometry(QtCore.QRect(40, 394, 191, 23))
        self.progressBar_7.setProperty("value", cb)
        self.progressBar_7.setObjectName("progressBar_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(33, 465, 60, 32))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(99, 471, 160, 16))
        self.label_9.setObjectName("label_9")
        self.progressBar_8 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_8.setGeometry(QtCore.QRect(39, 447, 191, 23))
        self.progressBar_8.setProperty("value", sql)
        self.progressBar_8.setObjectName("progressBar_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(33, 515, 60, 32))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(99, 521, 160, 16))
        self.label_10.setObjectName("label_10")
        self.progressBar_9 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_9.setGeometry(QtCore.QRect(39, 497, 191, 23))
        self.progressBar_9.setProperty("value", ai)
        self.progressBar_9.setObjectName("progressBar_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(33, 566, 60, 32))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(99, 572, 220, 16))
        self.label_11.setObjectName("label_11")
        self.progressBar_10 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_10.setGeometry(QtCore.QRect(39, 548, 191, 23))
        self.progressBar_10.setProperty("value", lt)
        self.progressBar_10.setObjectName("progressBar_10")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(360, 42, 160, 16))
        self.label_12.setObjectName("label_12")
        self.progressBar_11 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_11.setGeometry(QtCore.QRect(360, 62, 191, 23))
        self.progressBar_11.setProperty("value", temp)
        self.progressBar_11.setObjectName("progressBar_11")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(354, 132, 60, 32))
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(420, 246, 180, 16))
        self.label_13.setObjectName("label_13")
        self.progressBar_12 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_12.setGeometry(QtCore.QRect(360, 492, 191, 23))
        self.progressBar_12.setProperty("value", js)
        self.progressBar_12.setObjectName("progressBar_12")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(420, 576, 170, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(420, 192, 150, 16))
        self.label_15.setObjectName("label_15")
        self.progressBar_13 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_13.setGeometry(QtCore.QRect(360, 222, 191, 23))
        self.progressBar_13.setProperty("value", os)
        self.progressBar_13.setObjectName("progressBar_13")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(354, 510, 60, 32))
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(420, 86, 200, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(420, 366, 200, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(420, 416, 180, 16))
        self.label_18.setObjectName("label_18")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(354, 80, 60, 32))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(354, 186, 60, 32))
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(420, 138, 170, 16))
        self.label_19.setObjectName("label_19")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(354, 461, 60, 31))
        self.pushButton_15.setObjectName("pushButton_15")
        self.progressBar_14 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_14.setGeometry(QtCore.QRect(360, 442, 191, 23))
        self.progressBar_14.setProperty("value", pr)
        self.progressBar_14.setObjectName("progressBar_14")
        self.progressBar_15 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_15.setGeometry(QtCore.QRect(360, 552, 191, 23))
        self.progressBar_15.setProperty("value", 100)
        self.progressBar_15.setObjectName("progressBar_15")
        self.progressBar_16 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_16.setGeometry(QtCore.QRect(360, 342, 191, 23))
        self.progressBar_16.setProperty("value", ds)
        self.progressBar_16.setObjectName("progressBar_16")
        self.progressBar_17 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_17.setGeometry(QtCore.QRect(360, 282, 191, 23))
        self.progressBar_17.setProperty("value", dd)
        self.progressBar_17.setObjectName("progressBar_17")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(354, 410, 60, 32))
        self.pushButton_16.setObjectName("pushButton_16")
        self.progressBar_18 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_18.setGeometry(QtCore.QRect(360, 392, 191, 23))
        self.progressBar_18.setProperty("value", djg)
        self.progressBar_18.setObjectName("progressBar_18")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(420, 466, 160, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(420, 516, 170, 16))
        self.label_21.setObjectName("label_21")
        self.progressBar_19 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_19.setGeometry(QtCore.QRect(360, 114, 191, 23))
        self.progressBar_19.setProperty("value", 0)
        self.progressBar_19.setObjectName("progressBar_19")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(354, 240, 60, 32))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(354, 360, 60, 32))
        self.pushButton_18.setObjectName("pushButton_18")
        self.progressBar_20 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_20.setGeometry(QtCore.QRect(360, 168, 191, 23))
        self.progressBar_20.setProperty("value", 0)
        self.progressBar_20.setObjectName("progressBar_20")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(354, 570, 60, 32))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(354, 300, 60, 32))
        self.pushButton_20.setObjectName("pushButton_20")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(420, 306, 190, 16))
        self.label_22.setObjectName("label_22")
        self.progressBar_21 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_21.setGeometry(QtCore.QRect(690, 282, 191, 23))
        self.progressBar_21.setProperty("value", 0)
        self.progressBar_21.setObjectName("progressBar_21")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(684, 240, 60, 32))
        self.pushButton_21.setObjectName("pushButton_21")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(690, 42, 160, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(750, 576, 150, 16))
        self.label_24.setObjectName("label_24")
        self.progressBar_22 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_22.setGeometry(QtCore.QRect(690, 442, 191, 23))
        self.progressBar_22.setProperty("value", 0)
        self.progressBar_22.setObjectName("progressBar_22")
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(684, 570, 60, 32))
        self.pushButton_22.setObjectName("pushButton_22")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(750, 366, 170, 16))
        self.label_25.setObjectName("label_25")
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(684, 132, 60, 32))
        self.pushButton_23.setObjectName("pushButton_23")
        self.progressBar_23 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_23.setGeometry(QtCore.QRect(690, 114, 191, 23))
        self.progressBar_23.setProperty("value", 1)
        self.progressBar_23.setObjectName("progressBar_23")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(750, 192, 210, 16))
        self.label_26.setObjectName("label_26")
        self.progressBar_24 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_24.setGeometry(QtCore.QRect(690, 62, 191, 23))
        self.progressBar_24.setProperty("value", 0)
        self.progressBar_24.setObjectName("progressBar_24")
        self.progressBar_25 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_25.setGeometry(QtCore.QRect(690, 492, 191, 23))
        self.progressBar_25.setProperty("value", ec)
        self.progressBar_25.setObjectName("progressBar_25")
        self.progressBar_26 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_26.setGeometry(QtCore.QRect(690, 552, 191, 23))
        self.progressBar_26.setProperty("value", lg)
        self.progressBar_26.setObjectName("progressBar_26")
        self.progressBar_27 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_27.setGeometry(QtCore.QRect(690, 342, 191, 23))
        self.progressBar_27.setProperty("value", 10)
        self.progressBar_27.setObjectName("progressBar_27")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(750, 306, 240, 16))
        self.label_27.setObjectName("label_27")
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(684, 510, 60, 32))
        self.pushButton_24.setObjectName("pushButton_24")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(750, 416, 170, 16))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(750, 86, 170, 16))
        self.label_29.setObjectName("label_29")
        self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_25.setGeometry(QtCore.QRect(684, 300, 60, 32))
        self.pushButton_25.setObjectName("pushButton_25")
        self.progressBar_28 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_28.setGeometry(QtCore.QRect(690, 392, 191, 23))
        self.progressBar_28.setProperty("value", 0)
        self.progressBar_28.setObjectName("progressBar_28")
        self.progressBar_29 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_29.setGeometry(QtCore.QRect(690, 168, 191, 23))
        self.progressBar_29.setProperty("value", 0)
        self.progressBar_29.setObjectName("progressBar_29")
        self.progressBar_30 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_30.setGeometry(QtCore.QRect(690, 222, 191, 23))
        self.progressBar_30.setProperty("value", 0)
        self.progressBar_30.setObjectName("progressBar_30")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(750, 246, 190, 16))
        self.label_30.setObjectName("label_30")
        self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_26.setGeometry(QtCore.QRect(684, 410, 60, 32))
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_27.setGeometry(QtCore.QRect(684, 360, 60, 32))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_28.setGeometry(QtCore.QRect(684, 186, 60, 32))
        self.pushButton_28.setObjectName("pushButton_28")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(750, 138, 190, 16))
        self.label_31.setObjectName("label_31")
        self.pushButton_29 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_29.setGeometry(QtCore.QRect(684, 460, 60, 32))
        self.pushButton_29.setObjectName("pushButton_29")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(750, 466, 180, 16))
        self.label_32.setObjectName("label_32")
        self.pushButton_30 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_30.setGeometry(QtCore.QRect(684, 80, 60, 32))
        self.pushButton_30.setObjectName("pushButton_30")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(750, 516, 170, 16))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(240, 69, 120, 20))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(240, 120, 120, 20))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(240, 180, 120, 20))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setGeometry(QtCore.QRect(240, 230, 120, 20))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        self.label_38.setGeometry(QtCore.QRect(240, 290, 120, 20))
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        self.label_39.setGeometry(QtCore.QRect(240, 340, 120, 20))
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        self.label_40.setGeometry(QtCore.QRect(240, 400, 120, 20))
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.centralwidget)
        self.label_41.setGeometry(QtCore.QRect(240, 450, 120, 20))
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.centralwidget)
        self.label_42.setGeometry(QtCore.QRect(239, 500, 120, 20))
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.centralwidget)
        self.label_43.setGeometry(QtCore.QRect(240, 550, 120, 20))
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.centralwidget)
        self.label_44.setGeometry(QtCore.QRect(560, 60, 120, 20))
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.centralwidget)
        self.label_45.setGeometry(QtCore.QRect(562, 117, 120, 20))
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.centralwidget)
        self.label_46.setGeometry(QtCore.QRect(560, 172, 120, 20))
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.centralwidget)
        self.label_47.setGeometry(QtCore.QRect(560, 223, 120, 20))
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.centralwidget)
        self.label_48.setGeometry(QtCore.QRect(560, 283, 120, 20))
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.centralwidget)
        self.label_49.setGeometry(QtCore.QRect(560, 343, 120, 20))
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.centralwidget)
        self.label_50.setGeometry(QtCore.QRect(560, 393, 120, 20))
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self.centralwidget)
        self.label_51.setGeometry(QtCore.QRect(560, 444, 130, 20))
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.centralwidget)
        self.label_52.setGeometry(QtCore.QRect(560, 498, 130, 20))
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.centralwidget)
        self.label_53.setGeometry(QtCore.QRect(559, 555, 130, 20))
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.centralwidget)
        self.label_54.setGeometry(QtCore.QRect(890, 62, 140, 20))
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.centralwidget)
        self.label_55.setGeometry(QtCore.QRect(895, 115, 140, 20))
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(self.centralwidget)
        self.label_56.setGeometry(QtCore.QRect(893, 170, 140, 20))
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(self.centralwidget)
        self.label_57.setGeometry(QtCore.QRect(893, 223, 140, 20))
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(self.centralwidget)
        self.label_58.setGeometry(QtCore.QRect(894, 284, 160, 20))
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.centralwidget)
        self.label_59.setGeometry(QtCore.QRect(893, 345, 140, 20))
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(self.centralwidget)
        self.label_60.setGeometry(QtCore.QRect(894, 392, 140, 20))
        self.label_60.setObjectName("label_60")
        self.label_61 = QtWidgets.QLabel(self.centralwidget)
        self.label_61.setGeometry(QtCore.QRect(896, 443, 140, 20))
        self.label_61.setObjectName("label_61")
        self.label_62 = QtWidgets.QLabel(self.centralwidget)
        self.label_62.setGeometry(QtCore.QRect(897, 495, 140, 20))
        self.label_62.setObjectName("label_62")
        self.label_63 = QtWidgets.QLabel(self.centralwidget)
        self.label_63.setGeometry(QtCore.QRect(899, 554, 140, 20))
        self.label_63.setObjectName("label_63")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1057, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)



        #인스턴스를 만들기도 전에 스타일시트를 먹이면 에러가 난다구! 인스턴스가 없다구 그런단말이야!
        self.progressBar_2.setStyleSheet(COMPLETED_STYLE)
        self.progressBar_3.setStyleSheet(COMPLETED_STYLE)
        self.progressBar_4.setStyleSheet(COMPLETED_STYLE)
        self.progressBar_5.setStyleSheet(COMPLETED_STYLE)
        self.progressBar_6.setStyleSheet(COMPLETED_STYLE)
        self.progressBar_7.setStyleSheet(COMPLETED_STYLE2)
        self.progressBar_8.setStyleSheet(COMPLETED_STYLE2)
        self.progressBar_9.setStyleSheet(COMPLETED_STYLE2)
        self.progressBar_10.setStyleSheet(COMPLETED_STYLE2)

        self.progressBar_11.setStyleSheet(COMPLETED_STYLE)
        self.progressBar_12.setStyleSheet(COMPLETED_STYLE2)
        self.progressBar_13.setStyleSheet(COMPLETED_STYLE)
        self.progressBar_14.setStyleSheet(COMPLETED_STYLE)
        self.progressBar_15.setStyleSheet(COMPLETED_STYLE2)
        self.progressBar_16.setStyleSheet(COMPLETED_STYLE)
        self.progressBar_17.setStyleSheet(COMPLETED_STYLE)
        self.progressBar_18.setStyleSheet(COMPLETED_STYLE)
        self.progressBar_19.setStyleSheet(COMPLETED_STYLE)
        self.progressBar_20.setStyleSheet(COMPLETED_STYLE)

        self.progressBar_21.setStyleSheet(COMPLETED_STYLE)
        self.progressBar_22.setStyleSheet(COMPLETED_STYLE)
        self.progressBar_23.setStyleSheet(COMPLETED_STYLE)
        self.progressBar_24.setStyleSheet(COMPLETED_STYLE2)
        self.progressBar_25.setStyleSheet(COMPLETED_STYLE)
        self.progressBar_26.setStyleSheet(COMPLETED_STYLE2)
        self.progressBar_27.setStyleSheet(COMPLETED_STYLE)
        self.progressBar_28.setStyleSheet(COMPLETED_STYLE)
        self.progressBar_29.setStyleSheet(COMPLETED_STYLE)
        self.progressBar_30.setStyleSheet(COMPLETED_STYLE)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
#여기까지 레이아웃


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "*----palette progress bar v1.0 ----*"))
        self.label_2.setText(_translate("MainWindow", "Arnold Renderer"))
        self.pushButton.setText(_translate("MainWindow", "Push"))
        self.label.setText(_translate("MainWindow", "*- project44 VFX Label -*"))
        self.label_3.setText(_translate("MainWindow", "Adobe illustrator+HUD"))
        self.pushButton_2.setText(_translate("MainWindow", "Push"))
        self.pushButton_3.setText(_translate("MainWindow", "Push"))
        self.label_4.setText(_translate("MainWindow", "After Effect의 대가"))
        self.pushButton_4.setText(_translate("MainWindow", "Push"))
        self.label_5.setText(_translate("MainWindow", "Houdini 눈오는날 만들기"))
        self.pushButton_5.setText(_translate("MainWindow", "Push"))
        self.label_6.setText(_translate("MainWindow", "python+mel 수료증"))
        self.pushButton_6.setText(_translate("MainWindow", "Push"))
        self.label_7.setText(_translate("MainWindow", "rigging"+str(rgg)+"% 수료증"))
        self.pushButton_7.setText(_translate("MainWindow", "Push"))
        self.label_8.setText(_translate("MainWindow", "Maya메뉴: 써치바로 제작"))
        self.pushButton_8.setText(_translate("MainWindow", "Push"))
        self.label_9.setText(_translate("MainWindow", "db사용sql + MySQL"))
        self.pushButton_9.setText(_translate("MainWindow", "Push"))
        self.label_10.setText(_translate("MainWindow", "MARI multiple UV"))
        self.pushButton_10.setText(_translate("MainWindow", "Push"))
        self.label_11.setText(_translate("MainWindow", "빛, 생명, 색체 -KAIST:메시지 처리"))
        self.label_12.setText(_translate("MainWindow", "*- project44 TD Label -*"))
        self.pushButton_11.setText(_translate("MainWindow", "Push"))
        self.label_13.setText(_translate("MainWindow", "iOS11,swift4:Angela"))
        self.label_14.setText(_translate("MainWindow", "카이스트 영상최적화기법: 코드1회분"))
        self.label_15.setText(_translate("MainWindow", "html/css/js/vue.js"))
        self.pushButton_12.setText(_translate("MainWindow", "Push"))
        self.label_16.setText(_translate("MainWindow", "간이 테이블"))
        self.label_17.setText(_translate("MainWindow", "kaist 자료구조"+str(ds)+"%"))
        self.label_18.setText(_translate("MainWindow", "django "+str(djg)+"% 수료증"))
        self.pushButton_13.setText(_translate("MainWindow", "Push"))
        self.pushButton_14.setText(_translate("MainWindow", "Push"))
        self.label_19.setText(_translate("MainWindow", "js:functional programming"))
        self.pushButton_15.setText(_translate("MainWindow", "Push"))
        self.pushButton_16.setText(_translate("MainWindow", "Push"))
        self.label_20.setText(_translate("MainWindow", "Python& 폐인+팀랩+생활코딩+깐파"))
        self.label_21.setText(_translate("MainWindow", "javasript:치트시트제작!"))
        self.pushButton_17.setText(_translate("MainWindow", "Push"))
        self.pushButton_18.setText(_translate("MainWindow", "Push"))
        self.pushButton_19.setText(_translate("MainWindow", "완료"))
        self.pushButton_20.setText(_translate("MainWindow", "Push"))
        self.label_22.setText(_translate("MainWindow", "c/c++두들낙서 혹은 bucky!"))
        self.pushButton_21.setText(_translate("MainWindow", "Push"))
        self.label_23.setText(_translate("MainWindow", "*- project44 Main Label -*"))
        self.label_24.setText(_translate("MainWindow", "논리학 필로지아(정리필)"))
        self.pushButton_22.setText(_translate("MainWindow", "Push"))
        self.label_25.setText(_translate("MainWindow", "중국어"))
        self.pushButton_23.setText(_translate("MainWindow", "Push"))
        self.label_26.setText(_translate("MainWindow", "project:그릴걸고고학자녀,핏폴,아이돌트"))
        self.label_27.setText(_translate("MainWindow", "empty"))
        self.pushButton_24.setText(_translate("MainWindow", "Push"))
        self.label_28.setText(_translate("MainWindow", "이탈리아어"))
        self.label_29.setText(_translate("MainWindow", "empty"))
        self.pushButton_25.setText(_translate("MainWindow", "Push"))
        self.label_30.setText(_translate("MainWindow", "social+, male+"))
        self.pushButton_26.setText(_translate("MainWindow", "Push"))
        self.pushButton_27.setText(_translate("MainWindow", "Push"))
        self.pushButton_28.setText(_translate("MainWindow", "Push"))
        self.label_31.setText(_translate("MainWindow", "게임 이론 - KAIST"))
        self.pushButton_29.setText(_translate("MainWindow", "Push"))
        self.label_32.setText(_translate("MainWindow", "프랑스어"))
        self.pushButton_30.setText(_translate("MainWindow", "Push"))
        self.label_33.setText(_translate("MainWindow", "for TEPS"))
        self.label_34.setText(_translate("MainWindow", ""))
        self.label_35.setText(_translate("MainWindow", ""))
        self.label_36.setText(_translate("MainWindow", ""))
        self.label_37.setText(_translate("MainWindow", ""))
        self.label_38.setText(_translate("MainWindow", "maximum flow"))
        self.label_39.setText(_translate("MainWindow", "짧고 몇 강의 안됨!!"))
        self.label_40.setText(_translate("MainWindow", ""))
        self.label_41.setText(_translate("MainWindow", "DB써그냥 -최성철교수"))
        self.label_42.setText(_translate("MainWindow", ""))
        self.label_43.setText(_translate("MainWindow", str(lt)+"%"))
        self.label_44.setText(_translate("MainWindow", ""))
        self.label_45.setText(_translate("MainWindow", ""))
        self.label_46.setText(_translate("MainWindow", ""))
        self.label_47.setText(_translate("MainWindow", ""))
        self.label_48.setText(_translate("MainWindow", ""))
        self.label_49.setText(_translate("MainWindow", ""))
        self.label_50.setText(_translate("MainWindow", ""))
        self.label_51.setText(_translate("MainWindow", ""))
        self.label_52.setText(_translate("MainWindow", ""))
        self.label_53.setText(_translate("MainWindow", ""))
        self.label_54.setText(_translate("MainWindow", ""))
        self.label_55.setText(_translate("MainWindow", ""))
        self.label_56.setText(_translate("MainWindow", ""))
        self.label_57.setText(_translate("MainWindow", ""))
        self.label_58.setText(_translate("MainWindow", ""))
        self.label_59.setText(_translate("MainWindow", ""))
        self.label_60.setText(_translate("MainWindow", ""))
        self.label_61.setText(_translate("MainWindow", ""))
        self.label_62.setText(_translate("MainWindow", ""))
        self.label_63.setText(_translate("MainWindow", ""))


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

