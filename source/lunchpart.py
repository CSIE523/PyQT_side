# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lunchpart.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_lunchWindow(object):
    def setupUi(self, lunchWindow):
        lunchWindow.setObjectName("lunchWindow")
        lunchWindow.resize(586, 420)
        self.centralwidget = QtWidgets.QWidget(lunchWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 290, 281, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 330, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 330, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 80, 161, 151))
        self.pushButton_3.setObjectName("pushButton_3")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(50, 50, 281, 201))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(490, 350, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        lunchWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(lunchWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 586, 21))
        self.menubar.setObjectName("menubar")
        lunchWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(lunchWindow)
        self.statusbar.setObjectName("statusbar")
        lunchWindow.setStatusBar(self.statusbar)

        self.retranslateUi(lunchWindow)
        QtCore.QMetaObject.connectSlotsByName(lunchWindow)

    def retranslateUi(self, lunchWindow):
        _translate = QtCore.QCoreApplication.translate
        lunchWindow.setWindowTitle(_translate("lunchWindow", "MainWindow"))
        self.pushButton.setText(_translate("lunchWindow", "Delete"))
        self.pushButton_2.setText(_translate("lunchWindow", "Enter"))
        self.pushButton_3.setText(_translate("lunchWindow", "Draw!!!"))
        self.pushButton_4.setText(_translate("lunchWindow", "Exit"))
