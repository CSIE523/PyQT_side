from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import  QMessageBox
from MainWindow import Ui_MainWindow
from lunchpart import Ui_lunchWindow
from dinnerpart import Ui_dinnerWindow
import random
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.window1=lunchWindow()
        self.window2=dinnerWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('大神!請告訴我要吃什麼!')
        self.setWindowIcon(QtGui.QIcon('french.jpg'))
        self.ui.pushButton_2.clicked.connect(self.openlunch)
        self.ui.pushButton_3.clicked.connect(self.opendinner)

    def openlunch(self):
        window.hide()
        self.window1.show()

    def opendinner(self):
        window.hide()
        self.window2.show()


class lunchWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(lunchWindow, self).__init__()
        self.ui = Ui_lunchWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('lunch')
        self.save_file='lunch.txt'
        self.read_from_file(self.save_file)
        self.ui.pushButton_2.clicked.connect(self.addItem)
        self.ui.pushButton.clicked.connect(self.deleteItem)
        self.ui.pushButton_3.clicked.connect(self.drawitems)
        self.ui.pushButton_4.clicked.connect(self.backtomainl)


    def addItem(self):
        msg = QMessageBox()
        msg.setWindowTitle("錯誤")
        msg.setText("重複輸入!!!")
        number=self.ui.listWidget.count()
        if not self.ui.lineEdit.text():
            return
        value = self.ui.lineEdit.text()
        for i in range(number):
            if self.ui.listWidget.item(i).text() == value:
                msg.exec_()
                self.ui.lineEdit.clear()
                return
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
            msg = QMessageBox()
            msg.setWindowTitle("終於知道要吃什麼了!!!")
            number=random.randint(1,1000000)%self.ui.listWidget.count()
            msg.setText(self.ui.listWidget.item(number).text())
            msg.exec_()

    def backtomainl(self):
        self.ui.lineEdit.clear()
        self.close()
        window.show()

    def write_to_file(self, file):
        try:
            list_widget = self.ui.listWidget
            entries = '\n'.join(list_widget.item(i).text() for i in range(list_widget.count()))
            with open(file, 'w') as fout:
                fout.write(entries)
        except OSError as err:
            print(f"file {file} could not be written")

    def read_from_file(self, file):
        try:
            list_widget = self.ui.listWidget
            with open(file, 'r') as fin:
                entries = [e.strip() for e in fin.readlines()]
            list_widget.insertItems(0, entries)
        except OSError as err:
            with open(file, 'w'):
                pass

    def closeEvent(self, event):
        should_save = QtWidgets.QMessageBox.question(self, "檔案儲存",
                                                     "是否要儲存檔案?")
        if should_save == QtWidgets.QMessageBox.Yes:
            self.write_to_file(self.save_file)
        elif should_save == QtWidgets.QMessageBox.No:
            self.ui.listWidget.clear()
            self.read_from_file(self.save_file)


class dinnerWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(dinnerWindow, self).__init__()
        self.ui = Ui_dinnerWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('dinner')
        self.save_file = 'dinner.txt'
        self.read_from_file(self.save_file)
        self.ui.pushButton_2.clicked.connect(self.addItem)
        self.ui.pushButton.clicked.connect(self.deleteItem)
        self.ui.pushButton_3.clicked.connect(self.drawitems)
        self.ui.pushButton_4.clicked.connect(self.backtomaind)

    def addItem(self):
        msg = QMessageBox()
        msg.setWindowTitle("錯誤")
        msg.setText("重複輸入!!!")
        number = self.ui.listWidget.count()
        if not self.ui.lineEdit.text():
            return
        value = self.ui.lineEdit.text()
        for i in range(number):
            if self.ui.listWidget.item(i).text() == value:
                msg.exec_()
                self.ui.lineEdit.clear()
                return
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
            msg = QMessageBox()
            msg.setWindowTitle("終於知道要吃什麼了")
            number = random.randint(1, 1000000) % self.ui.listWidget.count()
            msg.setText(self.ui.listWidget.item(number).text())
            msg.exec_()

    def backtomaind(self):
        self.close()
        window.show()

    def write_to_file(self,file):
        try:
            list_widget = self.ui.listWidget
            entries= '\n'.join(list_widget.item(i).text() for i in range(list_widget.count()))
            with open(file,'w') as fout:
                fout.write(entries)
        except OSError as err:
            print(f"file {file} could not be written")

    def read_from_file(self, file):
        try:
            list_widget = self.ui.listWidget
            with open(file, 'r') as fin:
                entries = [e.strip() for e in fin.readlines()]
            list_widget.insertItems(0, entries)
        except OSError as err:
            with open(file, 'w'):
                pass

    def closeEvent(self,event):
        should_save = QtWidgets.QMessageBox.question(self, "檔案儲存",
                                                     "是否要儲存檔案?")
        if should_save == QtWidgets.QMessageBox.Yes:
            self.write_to_file(self.save_file)
        elif should_save == QtWidgets.QMessageBox.No:
            self.ui.listWidget.clear()
            self.read_from_file(self.save_file)



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())