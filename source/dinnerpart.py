# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dinnerpart.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dinnerWindow(object):
    def setupUi(self, dinnerWindow):
        dinnerWindow.setObjectName("dinnerWindow")
        dinnerWindow.resize(586, 419)
        self.centralwidget = QtWidgets.QWidget(dinnerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 80, 161, 151))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 330, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 290, 281, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 330, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(490, 350, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(50, 50, 281, 201))
        self.listWidget.setObjectName("listWidget")
        dinnerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(dinnerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 586, 21))
        self.menubar.setObjectName("menubar")
        dinnerWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(dinnerWindow)
        self.statusbar.setObjectName("statusbar")
        dinnerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(dinnerWindow)
        QtCore.QMetaObject.connectSlotsByName(dinnerWindow)

    def retranslateUi(self, dinnerWindow):
        _translate = QtCore.QCoreApplication.translate
        dinnerWindow.setWindowTitle(_translate("dinnerWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("dinnerWindow", "Draw!!!"))
        self.pushButton_2.setText(_translate("dinnerWindow", "Enter"))
        self.pushButton.setText(_translate("dinnerWindow", "Delete"))
        self.pushButton_4.setText(_translate("dinnerWindow", "Exit"))