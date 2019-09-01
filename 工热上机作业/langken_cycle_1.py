# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'langken_cycle_1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ThermodynamicsAssignments(object):
    def setupUi(self, ThermodynamicsAssignments):
        ThermodynamicsAssignments.setObjectName("ThermodynamicsAssignments")
        ThermodynamicsAssignments.resize(659, 512)
        font = QtGui.QFont()
        font.setPointSize(18)
        ThermodynamicsAssignments.setFont(font)
        self.pushButton = QtWidgets.QPushButton(ThermodynamicsAssignments)
        self.pushButton.setGeometry(QtCore.QRect(440, 190, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label1 = QtWidgets.QLabel(ThermodynamicsAssignments)
        self.label1.setGeometry(QtCore.QRect(250, 20, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label1_2 = QtWidgets.QLabel(ThermodynamicsAssignments)
        self.label1_2.setGeometry(QtCore.QRect(100, 70, 401, 151))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label1_2.setFont(font)
        self.label1_2.setObjectName("label1_2")
        self.label1_3 = QtWidgets.QLabel(ThermodynamicsAssignments)
        self.label1_3.setGeometry(QtCore.QRect(440, 260, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label1_3.setFont(font)
        self.label1_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label1_3.setObjectName("label1_3")
        self.label1_4 = QtWidgets.QLabel(ThermodynamicsAssignments)
        self.label1_4.setGeometry(QtCore.QRect(100, 220, 241, 151))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label1_4.setFont(font)
        self.label1_4.setObjectName("label1_4")
        self.textBrowser = QtWidgets.QTextBrowser(ThermodynamicsAssignments)
        self.textBrowser.setGeometry(QtCore.QRect(400, 320, 211, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(ThermodynamicsAssignments)
        self.label.setGeometry(QtCore.QRect(10, 270, 41, 241))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(ThermodynamicsAssignments)
        self.pushButton.clicked.connect(ThermodynamicsAssignments.calculate_answer)
        QtCore.QMetaObject.connectSlotsByName(ThermodynamicsAssignments)

    def retranslateUi(self, ThermodynamicsAssignments):
        _translate = QtCore.QCoreApplication.translate
        ThermodynamicsAssignments.setWindowTitle(_translate("ThermodynamicsAssignments", "Form"))
        self.pushButton.setText(_translate("ThermodynamicsAssignments", "计算!"))
        self.label1.setText(_translate("ThermodynamicsAssignments", "朗肯循环"))
        self.label1_2.setText(_translate("ThermodynamicsAssignments", "            第一题\n"
"\n"
"已知:p1=4MPa,t1=450℃,p2=6kPa。\n"
"计算ηt(忽略泵功)"))
        self.label1_3.setText(_translate("ThermodynamicsAssignments", "计算结果"))
        self.label1_4.setText(_translate("ThermodynamicsAssignments", "查表可得：\n"
"h1=3331.2kJ/kg\n"
"h2=2136.8kJ/kg\n"
"h3=h2\'=151.85kJ/kg"))
        self.textBrowser.setHtml(_translate("ThermodynamicsAssignments", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
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

