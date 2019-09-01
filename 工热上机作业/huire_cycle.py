# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'huire_cycle.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ThermodynamicsAssignments(object):
    def setupUi(self, ThermodynamicsAssignments):
        ThermodynamicsAssignments.setObjectName("ThermodynamicsAssignments")
        ThermodynamicsAssignments.resize(809, 637)
        self.label1_3 = QtWidgets.QLabel(ThermodynamicsAssignments)
        self.label1_3.setGeometry(QtCore.QRect(340, 340, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label1_3.setFont(font)
        self.label1_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label1_3.setObjectName("label1_3")
        self.label1_2 = QtWidgets.QLabel(ThermodynamicsAssignments)
        self.label1_2.setGeometry(QtCore.QRect(150, 60, 571, 211))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label1_2.setFont(font)
        self.label1_2.setObjectName("label1_2")
        self.pushButton = QtWidgets.QPushButton(ThermodynamicsAssignments)
        self.pushButton.setGeometry(QtCore.QRect(340, 270, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(ThermodynamicsAssignments)
        self.textBrowser.setGeometry(QtCore.QRect(240, 410, 311, 211))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label1 = QtWidgets.QLabel(ThermodynamicsAssignments)
        self.label1.setGeometry(QtCore.QRect(300, 20, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label = QtWidgets.QLabel(ThermodynamicsAssignments)
        self.label.setGeometry(QtCore.QRect(10, 390, 41, 241))
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
        self.label1_3.setText(_translate("ThermodynamicsAssignments", "计算结果"))
        self.label1_2.setText(_translate("ThermodynamicsAssignments", "已知：p1=5MPa,t1=450℃,pa=0.5MPa,p2=6kPa\n"
"①计算（忽略泵功）循环热效率ηt和耗汽率d与在\n"
"相同初参数下不采用回热的理想朗肯循环热效率\n"
"ηt和耗汽率相比；\n"
"②当绝热效率ηex=0.85，求题①所给相同参数下实\n"
"际不可逆回热循环的热效率ηt_real"))
        self.pushButton.setText(_translate("ThermodynamicsAssignments", "计算!"))
        self.textBrowser.setHtml(_translate("ThermodynamicsAssignments", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.label1.setText(_translate("ThermodynamicsAssignments", "一次抽汽回热循环"))
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

