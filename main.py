import sys
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import sqlite3


class AddEditCoffeeForm(QDialog):
    def __init__(self, parent=None, dan=False):
        self.dan = dan
        super(AddEditCoffeeForm, self).__init__(parent)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(60, 20, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        if self.dan:
            self.pushButton.setText('Изменить')
        else:
            self.pushButton.setText('Добавить')

        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(370, 30, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(219, 82, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)

        self.label = QtWidgets.QLabel("название сорта", self)
        self.label.setGeometry(QtCore.QRect(42, 82, 171, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.label_2 = QtWidgets.QLabel("степень обжарки", self)
        self.label_2.setGeometry(QtCore.QRect(42, 166, 190, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)

        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(238, 166, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)

        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 250, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)

        self.label_3 = QtWidgets.QLabel("молотый/в зернах", self)
        self.label_3.setGeometry(QtCore.QRect(42, 250, 212, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)

        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(227, 334, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)

        self.label_4 = QtWidgets.QLabel("описание вкуса", self)
        self.label_4.setGeometry(QtCore.QRect(42, 334, 179, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)

        self.label_5 = QtWidgets.QLabel("цена", self)
        self.label_5.setGeometry(QtCore.QRect(42, 419, 53, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)

        self.lineEdit_5 = QtWidgets.QLineEdit(self)
        self.lineEdit_5.setGeometry(QtCore.QRect(101, 419, 651, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)

        self.label_6 = QtWidgets.QLabel("объем упаковки", self)
        self.label_6.setGeometry(QtCore.QRect(42, 503, 185, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)

        self.lineEdit_6 = QtWidgets.QLineEdit(self)
        self.lineEdit_6.setGeometry(QtCore.QRect(233, 503, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_6.setFont(font)
        self.buttons = [self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4,
                        self.lineEdit_5, self.lineEdit_6]
        self.add()
        self.pushButton.clicked.connect(self.rev)

    def add(self):
        if self.dan:
            for i in range(6):
                self.buttons[i].setText(str(self.dan[i]))

    def rev(self):
        self.dan = []
        for i in range(6):
            s = self.buttons[i].text()
            self.dan.append([])
            if (i < 4) or (i > 3 and s.isdigit()):
                self.dan[-1] = s
            else:
                print(i, s)
                self.label_7.setText('Ошибка заполнения формы')
                return
        self.close()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.update_result()
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.change)

    def add(self):
        ex2 = AddEditCoffeeForm(parent=self)
        ex2.exec_()
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        result = ex2.dan
        try:
            cur.execute(f"""INSERT INTO coffee('название сорта', 'степень обжарки',
'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки')
VALUES('{result[0]}', '{result[1]}', '{result[2]}', '{result[3]}', {int(result[4])}, {int(result[5])})""")
            con.commit()
        except Exception:
            pass
        con.close()
        self.update_result()

    def change(self):
        id = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        res = list(cur.execute(f'select * from coffee where id = {id}').fetchone())[1:]
        ex2 = AddEditCoffeeForm(parent=self, dan=res)
        ex2.exec_()
        result = ex2.dan
        cur.execute(f"""update coffee
set 'название сорта' = '{result[0]}', 'степень обжарки' = '{result[1]}', 'молотый/в зернах' = '{result[2]}',
'описание вкуса' = '{result[3]}', 'цена' = {result[4]}, 'объем упаковки' = {result[5]} where id = {id}""")
        con.commit()
        con.close()
        self.update_result()

    def update_result(self):
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee""").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        titles = [description[0] for description in cur.description]
        self.tableWidget.setHorizontalHeaderLabels(titles)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())

