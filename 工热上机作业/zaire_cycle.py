# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zaire_cycle.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ThermodynamicsAssignments(object):
    def setupUi(self, ThermodynamicsAssignments):
        ThermodynamicsAssignments.setObjectName("ThermodynamicsAssignments")
        ThermodynamicsAssignments.resize(784, 598)
        self.label1 = QtWidgets.QLabel(ThermodynamicsAssignments)
        self.label1.setGeometry(QtCore.QRect(250, 10, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label1_3 = QtWidgets.QLabel(ThermodynamicsAssignments)
        self.label1_3.setGeometry(QtCore.QRect(140, 290, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label1_3.setFont(font)
        self.label1_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label1_3.setObjectName("label1_3")
        self.pushButton = QtWidgets.QPushButton(ThermodynamicsAssignments)
        self.pushButton.setGeometry(QtCore.QRect(560, 120, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label1_4 = QtWidgets.QLabel(ThermodynamicsAssignments)
        self.label1_4.setGeometry(QtCore.QRect(560, 270, 61, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label1_4.setFont(font)
        self.label1_4.setObjectName("label1_4")
        self.textBrowser = QtWidgets.QTextBrowser(ThermodynamicsAssignments)
        self.textBrowser.setGeometry(QtCore.QRect(60, 350, 311, 211))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label1_2 = QtWidgets.QLabel(ThermodynamicsAssignments)
        self.label1_2.setGeometry(QtCore.QRect(70, 50, 441, 211))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label1_2.setFont(font)
        self.label1_2.setObjectName("label1_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(ThermodynamicsAssignments)
        self.textBrowser_2.setGeometry(QtCore.QRect(460, 351, 256, 211))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label = QtWidgets.QLabel(ThermodynamicsAssignments)
        self.label.setGeometry(QtCore.QRect(10, 350, 41, 241))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(ThermodynamicsAssignments)
        self.pushButton.clicked.connect(ThermodynamicsAssignments.calculate_answer)
        self.pushButton.clicked.connect(ThermodynamicsAssignments.summarize)
        QtCore.QMetaObject.connectSlotsByName(ThermodynamicsAssignments)

    def retranslateUi(self, ThermodynamicsAssignments):
        _translate = QtCore.QCoreApplication.translate
        ThermodynamicsAssignments.setWindowTitle(_translate("ThermodynamicsAssignments", "Form"))
        self.label1.setText(_translate("ThermodynamicsAssignments", "再热循环"))
        self.label1_3.setText(_translate("ThermodynamicsAssignments", "计算结果"))
        self.pushButton.setText(_translate("ThermodynamicsAssignments", "计算!"))
        self.label1_4.setText(_translate("ThermodynamicsAssignments", "分析"))
        self.textBrowser.setHtml(_translate("ThermodynamicsAssignments", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.label1_2.setText(_translate("ThermodynamicsAssignments", "已知:p1=12MPa,t1=500℃,p2=6kPa\n"
"Pa1=3MPa,Pa2=0.6MPa,Ta1=Ta2=450℃\n"
"①计算(忽略泵功)ηta1,ηta2,X2a1,X2a2\n"
"②计算对应朗肯循环的热效率并比较,分析再热\n"
"压力Pa的选择对循环热效率ηt和最终干度的影响\n"
"③当汽机绝热内效率ηex=0.85，求与题①所给相\n"
"同初终参数下的实际不可逆再热循环的热效率ηt"))
        self.label.setText(_translate("ThermodynamicsAssignments", "最\n"
"终\n"
"版\n"
"权\n"
"归\n"
"吴\n"
"洛\n"
"祥\n"
"所\n"
"有"))

