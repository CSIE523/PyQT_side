from PyQt5 import QtWidgets, QtGui, QtCore
from MainWindow import Ui_MainWindow
from lunchpart import Ui_lunchWindow
import sys
import random


class lunchWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(lunchWindow, self).__init__()
        self.ui = Ui_lunchWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('lunch')

        self.ui.pushButton_2.clicked.connect(self.addItem)

        self.ui.pushButton.clicked.connect(self.deleteItem)

        self.ui.pushButton_3.clicked.connect(self.drawitems)

        self.ui.pushButton_4.clicked.connect(self.backtoMain)


    def addItem(self):
        if not self.ui.lineEdit.text():
            return
        value = self.ui.lineEdit.text()
        self.ui.lineEdit.clear()
        self.ui.listWidget.addItem(value)

    def deleteItem(self):
        items=self.ui.listWidget.selectedItems()
        if not items:
            return
        for item in items:
            self.ui.listWidget.takeItem(self.ui.listWidget.row(item))

    def drawitems(self):
        if self.ui.listWidget.count() == 0 :
            return
        else:
            print(self.ui.listWidget.item(random.randint(1,1000000)%self.ui.listWidget.count()).text())

    def backtoMain(self):
        self.window1 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window1)
        window.hide()
        self.window1.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = lunchWindow()
    window.show()
    sys.exit(app.exec_())